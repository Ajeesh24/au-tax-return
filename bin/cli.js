#!/usr/bin/env node
"use strict";

/**
 * Installer for the `au-tax-return` Claude skill.
 *
 * Copies the skill folder into a Claude skills directory. Zero dependencies —
 * uses only the Node standard library so it runs via `npx` with nothing to build.
 *
 *   npx github:Ajeesh24/au-tax-return            # install for current user
 *   npx github:Ajeesh24/au-tax-return --project  # install into ./.claude/skills
 *   npx github:Ajeesh24/au-tax-return --dir <path>
 *   npx github:Ajeesh24/au-tax-return --help
 */

const fs = require("fs");
const os = require("os");
const path = require("path");

const SKILL_NAME = "au-tax-return";
const SRC = path.join(__dirname, "..", SKILL_NAME);

function log(msg) {
  process.stdout.write(msg + "\n");
}

function parseArgs(argv) {
  const opts = { scope: "user", dir: null, force: false, help: false };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--help" || a === "-h") opts.help = true;
    else if (a === "--project" || a === "-p") opts.scope = "project";
    else if (a === "--user" || a === "-u") opts.scope = "user";
    else if (a === "--force" || a === "-f") opts.force = true;
    else if (a === "--dir" || a === "-d") {
      opts.dir = argv[++i];
      opts.scope = "custom";
    } else {
      log(`Unknown option: ${a}`);
      opts.help = true;
    }
  }
  return opts;
}

function printHelp() {
  log(`
au-tax-return — Claude skill installer

Installs the "au-tax-return" skill (helps individuals in Australia prepare their
own tax return: PAYG, investment property, CGT) into a Claude skills directory.

Usage:
  npx github:Ajeesh24/au-tax-return [options]

Options:
  -u, --user        Install for the current user (default):
                      ~/.claude/skills/${SKILL_NAME}
  -p, --project     Install into the current project:
                      ./.claude/skills/${SKILL_NAME}
  -d, --dir <path>  Install into a custom skills directory
  -f, --force       Overwrite an existing install without prompting
  -h, --help        Show this help

After installing, restart Claude Code (or reload skills) and ask, e.g.
  "Help me do my 2025-26 tax return — here are my documents."
`);
}

function resolveTarget(opts) {
  if (opts.scope === "custom") {
    return path.resolve(opts.dir, SKILL_NAME);
  }
  if (opts.scope === "project") {
    return path.resolve(process.cwd(), ".claude", "skills", SKILL_NAME);
  }
  return path.join(os.homedir(), ".claude", "skills", SKILL_NAME);
}

const SKIP = new Set(["__pycache__", ".DS_Store", ".git"]);

function copyDir(src, dest) {
  fs.mkdirSync(dest, { recursive: true });
  for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
    if (SKIP.has(entry.name) || entry.name.endsWith(".pyc")) continue;
    const s = path.join(src, entry.name);
    const d = path.join(dest, entry.name);
    if (entry.isDirectory()) copyDir(s, d);
    else if (entry.isFile()) fs.copyFileSync(s, d);
  }
}

function main() {
  const opts = parseArgs(process.argv.slice(2));
  if (opts.help) return printHelp();

  if (!fs.existsSync(path.join(SRC, "SKILL.md"))) {
    log(`Error: could not find the skill source at ${SRC}`);
    log("This installer must run from the au-tax-return package.");
    process.exit(1);
  }

  const target = resolveTarget(opts);

  if (fs.existsSync(target)) {
    if (!opts.force) {
      log(`A skill already exists at:\n  ${target}`);
      log("Re-run with --force to overwrite it.");
      process.exit(1);
    }
    fs.rmSync(target, { recursive: true, force: true });
  }

  try {
    copyDir(SRC, target);
  } catch (err) {
    log(`Error installing skill: ${err.message}`);
    process.exit(1);
  }

  log(`✅ Installed the "${SKILL_NAME}" skill to:`);
  log(`   ${target}`);
  log("");
  log("Restart Claude Code (or reload skills), then ask:");
  log('   "Help me do my 2025-26 tax return — here are my documents."');
  log("");
  log("⚠️  Tax rates in the skill are marked unverified — confirm figures on");
  log("   ato.gov.au before lodging. This is decision-support, not tax advice.");
}

main();
