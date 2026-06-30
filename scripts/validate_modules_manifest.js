#!/usr/bin/env node

const fs = require("node:fs");
const path = require("node:path");

const repoRoot = path.resolve(__dirname, "..");
const manifestPath = path.join(repoRoot, "modules.manifest.json");

const REQUIRED_KEYS = [
  "id",
  "title",
  "file",
  "thumb",
  "authorship",
  "listedInHome",
  "enabledInShell",
  "status",
];

const ID_PATTERN = /^[a-z0-9]+(?:_[a-z0-9]+)*$/;
const FILE_PATTERN = /^[a-z0-9_]+\/noixzy_[a-z0-9_]+\.html$/;
const THUMB_PATTERN = /^home\/thumbs\/[a-z0-9_]+\.png$/;

function readJson(filePath) {
  try {
    return JSON.parse(fs.readFileSync(filePath, "utf8"));
  } catch (error) {
    fail(`Could not read JSON at ${relative(filePath)}: ${error.message}`);
  }
}

function relative(filePath) {
  return path.relative(repoRoot, filePath) || ".";
}

function fileExists(relPath) {
  return fs.existsSync(path.join(repoRoot, relPath));
}

function fail(message) {
  console.error(`ERROR: ${message}`);
  process.exitCode = 1;
}

function warn(message) {
  console.warn(`WARN: ${message}`);
}

function validateModule(mod, index, seenIds) {
  const label = `modules[${index}]`;

  for (const key of REQUIRED_KEYS) {
    if (!(key in mod)) {
      fail(`${label} is missing required key "${key}"`);
    }
  }

  if (typeof mod.id !== "string" || !ID_PATTERN.test(mod.id)) {
    fail(`${label}.id must match ${ID_PATTERN} (got "${mod.id}")`);
  }

  if (seenIds.has(mod.id)) {
    fail(`${label}.id "${mod.id}" is duplicated`);
  }
  seenIds.add(mod.id);

  if (typeof mod.title !== "string" || mod.title.trim() === "") {
    fail(`${label}.title must be a non-empty string`);
  }

  if (typeof mod.file !== "string" || !FILE_PATTERN.test(mod.file)) {
    fail(`${label}.file must match ${FILE_PATTERN} (got "${mod.file}")`);
  }

  if (typeof mod.thumb !== "string" || !THUMB_PATTERN.test(mod.thumb)) {
    fail(`${label}.thumb must match ${THUMB_PATTERN} (got "${mod.thumb}")`);
  }

  if (typeof mod.authorship !== "string" || mod.authorship.trim() === "") {
    fail(`${label}.authorship must be a non-empty string`);
  }

  if (typeof mod.listedInHome !== "boolean") {
    fail(`${label}.listedInHome must be boolean`);
  }

  if (typeof mod.enabledInShell !== "boolean") {
    fail(`${label}.enabledInShell must be boolean`);
  }

  if (mod.status !== "listed") {
    warn(`${label}.status is "${mod.status}" (expected "listed" for active modules)`);
  }

  const expectedFile = `${mod.id}/noixzy_${mod.id}.html`;
  if (mod.file !== expectedFile) {
    fail(`${label}.file should be "${expectedFile}" for id "${mod.id}"`);
  }

  const expectedThumb = `home/thumbs/${mod.id}.png`;
  if (mod.thumb !== expectedThumb) {
    fail(`${label}.thumb should be "${expectedThumb}" for id "${mod.id}"`);
  }

  if (!fileExists(mod.file)) {
    fail(`${label}.file does not exist on disk: ${mod.file}`);
  }

  if (!fileExists(mod.thumb)) {
    fail(`${label}.thumb does not exist on disk: ${mod.thumb}`);
  }
}

function validateSummary(manifest) {
  if (!manifest.summary || typeof manifest.summary !== "object") {
    fail("summary object is missing");
    return;
  }

  const listedCount = manifest.modules.length;
  const reportedListed = manifest.summary.listedCount;

  if (reportedListed !== listedCount) {
    fail(
      `summary.listedCount (${reportedListed}) does not match modules.length (${listedCount})`
    );
  }
}

function main() {
  const manifest = readJson(manifestPath);

  if (!Array.isArray(manifest.modules)) {
    fail("modules.manifest.json must contain a top-level modules array");
    return;
  }

  const seenIds = new Set();
  manifest.modules.forEach((mod, index) => validateModule(mod, index, seenIds));
  validateSummary(manifest);

  if (process.exitCode && process.exitCode !== 0) {
    return;
  }

  console.log(`OK: validated ${manifest.modules.length} modules in modules.manifest.json`);
}

main();
