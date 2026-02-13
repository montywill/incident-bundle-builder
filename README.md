# Incident Bundle Builder (Python CLI)

A lightweight Python CLI tool that helps create an “incident bundle” for troubleshooting by:
- scanning a log for high-signal keywords
- saving keyword matches to a file
- saving the last N lines (tail) to a file
- generating a timestamped folder containing a report + artifacts

## What it Generates
Each run creates a folder like:
`incident_bundle_YYYYMMDD-HHMMSS/`

Containing:
- `report.txt` (summary + stats)
- `matches.txt` (lines containing keywords)
- `tail.txt` (last N lines of the log)

## Keywords Scanned
`ERROR, WARNING, CRITICAL, FAIL, TIMEOUT, EXCEPTION, DENIED`

## How to Run
```bash
python incident_bundle_builder.py

You will be prompted for:

log filename (example: app.log)

how many last lines to include (default 20)


Commit message: `Add README documentation`
---
## Step 5 — Clean repo (recommended)
Don’t upload generated folders (all your `incident_bundle_...` outputs).  
Instead, add a `.gitignore`:

1. **Add file → Create new file**
2. Name it: `.gitignore`
3. Paste:
4. Commit: `Add gitignore for generated bundles`

---

## Step 6 — Quick “resume-ready” polish
In GitHub repo settings:
- Add **About** description:  
  “Python CLI tool that bundles incident logs (matches/tail/report) into timestamped troubleshooting folders.”
- Add topics/tags: `python`, `cli`, `devops`, `sysadmin`, `logging`

---

### Do this now and tell me:
✅ “Repo created” + paste the repo name  
and I’ll give you the exact copy/paste for your **resume project section** and then we roll straight into **Project #3**.
