import re
import csv
from collections import Counter
from datetime import datetime
import os

# File paths
md_file_path = r"C:\Users\Anna\Documents\job-search-repo\resumes\Master_Resume.md"
csv_file_path = r"C:\Users\Anna\Documents\job-search-repo\job_search\tag_counts.csv"

# Get current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Read Markdown file and extract tags
with open(md_file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Regex to find tags (#TagName)
tags = re.findall(r"#(\w+)", content)
tag_counts = Counter(tags)

# Sort tags alphabetically
sorted_tags = dict(sorted(tag_counts.items()))

# Load previous run if CSV exists
previous_counts = {}
if os.path.exists(csv_file_path):
    with open(csv_file_path, "r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            previous_counts[row["Tag"]] = int(row["Count"])

# Print current counts and diffs
print(f"\nTag counts for {timestamp}:\n")
for tag, count in sorted_tags.items():
    prev = previous_counts.get(tag, 0)
    diff = count - prev
    diff_str = f" (Δ {diff:+})" if prev != 0 else ""
    print(f"{tag}: {count}{diff_str}")

total_unique_tags = len(sorted_tags)
print(f"\nTotal unique tags: {total_unique_tags}")

# Append current counts to CSV
file_exists = os.path.exists(csv_file_path)
with open(csv_file_path, "a", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["Timestamp", "Tag", "Count"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write header only if file didn't exist
    if not file_exists:
        writer.writeheader()

    for tag, count in sorted_tags.items():
        writer.writerow({"Timestamp": timestamp, "Tag": tag, "Count": count})
