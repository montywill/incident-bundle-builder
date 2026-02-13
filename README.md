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
