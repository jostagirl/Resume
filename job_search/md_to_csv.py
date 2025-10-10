import csv
import re
from datetime import datetime

input_file = "job_titles_master.md"
output_file = "job_titles_master.csv"

# Read the Markdown master list
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

category = None
rows = []

for line in lines:
    line = line.strip()
    # Detect category headers (## Header)
    header_match = re.match(r"^## (.+)", line)
    if header_match:
        category = header_match.group(1)
    # Detect list items (- Job Title)
    elif line.startswith("- "):
        title = line[2:].strip()
        rows.append({"Category": category, "Job Title": title})

# Generate timestamp for CSV comment
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Write to CSV
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["Category", "Job Title"])
    
    # Add timestamp comment as first row
    writer.writerow({"Category": f"# Generated on {timestamp}", "Job Title": ""})
    
    # Write header row
    writer.writeheader()
    
    # Write the job title rows
    writer.writerows(rows)

print(f"✅ Updated {output_file} with {len(rows)} job titles (generated on {timestamp}).")
