import re
from collections import Counter

# Path to your Master Resume
file_path = r"C:\Users\Anna\Documents\job-search-repo\resumes\Master_Resume.md"

# Regular expression to match hashtags
tag_pattern = r"#\w[\w-]*"

# Read the file and extract tags
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

tags = re.findall(tag_pattern, content)

# Remove leading '#' from each tag
tags_clean = [tag[1:] for tag in tags]

# Count occurrences of each unique tag
tag_counts = Counter(tags_clean)

# Sort tags alphabetically
sorted_tags = sorted(tag_counts.items())

# Output results
print("Unique tag counts in Master_Resume.md (alphabetical):")
for tag, count in sorted_tags:
    print(f"{tag}: {count}")

# Total number of unique tags
unique_tag_count = len(tag_counts)
print(f"\nTotal number of unique tags: {unique_tag_count}")

# Optional: write to a file for record-keeping
output_file = r"C:\Users\Anna\Documents\job-search-repo\job_search\unique_tag_counts.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write("Unique tag counts in Master_Resume.md (alphabetical):\n")
    for tag, count in sorted_tags:
        f.write(f"{tag}: {count}\n")
    f.write(f"\nTotal number of unique tags: {unique_tag_count}\n")
