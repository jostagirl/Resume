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

# 1️⃣ Print all tags and counts
print(f"\nTag counts for {timestamp} (all tags):\n")
for tag, count in sorted_tags.items():
    print(f"{tag}: {count}")

total_unique_tags = len(sorted_tags)
print(f"\nTotal unique tags: {total_unique_tags}")

# 2️⃣ Print only changed tags with delta
changed_tags = {tag: (count - previous_counts.get(tag, 0)) 
                for tag, count in sorted_tags.items() 
                if count != previous_counts.get(tag, 0)}

if changed_tags:
    print("\nTags changed since last run:\n")
    for tag, delta in sorted(changed_tags.items()):
        print(f"{tag}: Δ {delta:+}")
else:
    print("\nNo tag changes since last run.")

# 3️⃣ Print tags added or removed entirely
previous_tags_set = set(previous_counts.keys())
current_tags_set = set(sorted_tags.keys())

added_tags = current_tags_set - previous_tags_set
removed_tags = previous_tags_set - current_tags_set

if added_tags or removed_tags:
    print("\nTags added or removed since last run:\n")
    if added_tags:
        print("Added tags:")
        for tag in sorted(added_tags):
            print(f" + {tag}")
    if removed_tags:
        print("Removed tags:")
        for tag in sorted(removed_tags):
            print(f" - {tag}")
else:
    print("\nNo tags added or removed since last run.")

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
