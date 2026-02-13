import os
from datetime import datetime

print("=== Incident Bundle Builder ===")

#------INPUTS---------
log_file = input("Log filename (example: app.log): ").strip()
tail_n = input("Show last how many lines? (deafult 20): ").strip()

if tail_n == "":
   tail_n = 20
else: 
   tail_n = int(tail_n)
 
 #----- Initialize always-defined variables ----
lines = []
tail_lines = []
matches = []

KEYWORDS = ["ERROR", "WARNING", "CRITICAL", "FAIL", "TIMEOUT", "EXCEPTION", "DENIED"]

 #---------- CREATE BUNDLE FOLDER --------------
stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
bundle_dir = f"incident_bundle_{stamp}"
os.mkdir(bundle_dir)

report_path = os.path.join(bundle_dir, "report.txt")
matches_path = os.path.join(bundle_dir, "matches.txt")
tail_path = os.path.join(bundle_dir, "tail.txt")

 #------------- READ LOG_----------- 
try:
  with open(log_file, "r") as f:
    lines = f.readlines()

except FileNotFoundError:
  print("❌ File not found:", log_file)
  print("Create it in the left sidebar and run again.")
  raise SystemExit

  #---------- PROCESS ----------
  tail_lines = lines[-tail_n:] if len(lines) >= tail_n else lines

  matches = []
  for line in lines:
    up = line.upper()
    if any(k in up for k in KEYWORDS):
      matches.append(line)

#-------- WRITE OUTPUT FILES -----------
with open(report_path, "w") as r:
  r.write("=== Incident Bundle Report ===\n")
  r.write(f"Log file: {log_file}\n")
  r.write(f"Total lines: {len(lines)}\n")
  r.write(f"Matches: {len(matches)}\n")
  r.write(f"Keywords: {', '.join(KEYWORDS)}\n")

with open(matches_path, "w")as n:
  n.write("".join(matches))

with open(tail_path, "w") as t:
  t.write("".join(tail_lines))

#--------- PRINT SUMMARY --------
print("\n=== Bundle Created ===")
print("Folder:", bundle_dir)
print("Total lines:", len(lines))
print("Keyword matches:", len(matches))

print("\n--- Last Lines ---")
for line in tail_lines:
  print(line.rstrip())

print("\n--- First 5 Matches ---")
for line in matches[:5]:
  print("🚨", line.rstrip())
