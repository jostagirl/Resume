import csv
import re
from datetime import datetime

# Paths
input_file = r"C:\Users\Anna\Documents\job-search-repo\job_search\job_titles_master.md"
output_file = r"C:\Users\Anna\Documents\job-search-repo\job_search\job_titles_master.csv"

# Read Markdown master list
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

category = None
rows = []

for line in lines:
    line = line.strip()

    # Skip main title line or empty lines
    if line.startswith("# ") or not line:
        continue

    # Detect category headers (## Header)
    header_match = re.match(r"^##\s+(.+)", line)
    if header_match:
        category = header_match.group(1)
        continue

    # Detect list items (- Job Title [#tags])
    list_match = re.match(r"^[-*+]\s+(.+)", line)
    if list_match and category:
        full_text = list_match.group(1).strip()
        
        # Split out tags (assumes tags start with #)
        parts = full_text.split("#")
        title = parts[0].strip()
        tags = ",".join(f"#{p.strip()}" for p in parts[1:]) if len(parts) > 1 else ""
        
        rows.append({"Category": category, "Job Title": title, "Tags": tags})

# Generate timestamp for CSV comment
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Write to CSV
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["Category", "Job Title", "Tags"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Add timestamp comment
    writer.writerow({"Category": f"# Generated on {timestamp}", "Job Title": "", "Tags": ""})
    
    # Write header row
    writer.writeheader()
    
    # Write job title rows
    writer.writerows(rows)

print(f"✅ Updated {output_file} with {len(rows)} job titles (generated on {timestamp}).")
