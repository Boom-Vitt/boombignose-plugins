# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

A **Claude Code plugin marketplace** owned by BoomBigNose (`vittawat.soo@boombignose.org`). It currently contains one plugin — `thai-quotation` — which generates Thai-language quotation documents as print-ready HTML files.

Published at: `https://github.com/Boom-Vitt/boombignose-plugins`

## Validation Commands

There is no build system or test suite. Use these to validate manifest files:

```bash
# Validate marketplace manifest
python3 -m json.tool .claude-plugin/marketplace.json > /dev/null && echo "OK"

# Validate plugin manifest
python3 -m json.tool plugins/thai-quotation/.claude-plugin/plugin.json > /dev/null && echo "OK"

# Validate using Claude Code CLI (if installed)
claude plugin validate .
claude plugin validate ./plugins/thai-quotation

# Reload after editing plugin files (inside a Claude Code session)
/reload-plugins
```

**Testing `baht_text.py` directly:**
```bash
python3 plugins/thai-quotation/skills/quotation/scripts/baht_text.py 10700
# Expected output: หนึ่งหมื่นเจ็ดร้อยบาทถ้วน
```

## Local Installation for Development

The marketplace uses relative `source` paths and requires a git context:

```bash
git init && git add -A && git commit -m "init"
/plugin marketplace add /absolute/path/to/boombignose-plugins
/plugin install thai-quotation@boombignose-plugins
```

## Plugin Architecture

The repository follows the Claude Code plugin marketplace structure:

```
.claude-plugin/marketplace.json       ← marketplace manifest
plugins/thai-quotation/
  .claude-plugin/plugin.json          ← plugin manifest (version, author, license)
  commands/quote.md                   ← slash command: /thai-quotation:quote
  skills/quotation/
    SKILL.md                          ← authoritative skill logic (9-step workflow)
    assets/template.html              ← read-only HTML template (25 {{TOKEN}} slots)
    assets/example.html               ← rendered reference output
    scripts/baht_text.py              ← Thai currency-to-words converter
    references/baht-text.md           ← algorithm docs for baht_text.py
```

**How the layers connect:** The slash command (`quote.md`) is the user entry point. It delegates all logic to the `quotation` skill by directing Claude to read `SKILL.md`. The skill reads `template.html` (never modifying it), runs `baht_text.py` for currency conversion, then writes the output file to the user's working directory.

## thai-quotation Skill — Critical Rules

These rules apply whenever working on or invoking the `quotation` skill:

### 1. `baht_text.py` is the sole source of truth for `{{AMOUNT_IN_WORDS}}`
Never compute Thai currency words manually or infer them. Always run:
```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/quotation/scripts/baht_text.py" <grand_total_raw_number>
```
If `$CLAUDE_PLUGIN_ROOT` is unset, find the absolute path of `baht_text.py` via `find` and pass it directly. The script takes a raw number (no commas) and prints one line of Thai text.

### 2. `template.html` is immutable
Read it as a string, substitute all 25 `{{TOKEN}}` placeholders, then write to the user's working directory as `ใบเสนอราคา-{DOC_NO}.html`. Never modify `assets/template.html` itself.

### 3. No hallucination of business data
Seller fields not listed in CLAUDE.md (address, tax ID, phone) must remain as visible placeholders — `[ที่อยู่บริษัท — โปรดระบุ]`, `[เลขประจำตัวผู้เสียภาษี 13 หลัก — โปรดระบุ]`, `[เบอร์โทร — โปรดระบุ]` — unless the user provides the real values.

### 4. DRAFT watermark policy
All output files carry `<div class="draft-watermark">` from the template. Do not remove it unless the user explicitly approves the document. When removing (to produce the final version), delete the entire `<div class="draft-watermark">...</div>` element and save as `ใบเสนอราคา-{DOC_NO}-final.html`.

### 5. Money formatting
Every monetary value in the output must be formatted with comma thousands separator and exactly 2 decimal places: `1500` → `1,500.00`. This applies to all token slots including per-item `{{qty}}`, `{{unit_price}}`, `{{amount}}`, and all totals.

## Default Seller Information (Single Source of Truth)

```
SELLER_NAME    = BoomBigNose
SELLER_EMAIL   = vittawat.soo@boombignose.org
SELLER_WEBSITE = https://boombignose.org
```

These three fields are always pre-populated. Address, tax ID, and phone are always placeholders unless the user provides them.

## Adding a New Plugin

1. Create `plugins/<plugin-name>/` following the same structure as `thai-quotation`.
2. Add a `plugin.json` manifest under `plugins/<plugin-name>/.claude-plugin/`.
3. Register the plugin in `.claude-plugin/marketplace.json` under the `"plugins"` array with a relative `source` path.
4. Bump the `version` in `marketplace.json`.
