# pull_content_by_tags_sections.py

import re
from match_tags_to_job import get_matching_tags
import os

# ======= OPTION 1: Define file paths here (no prompts) =======
REPO_ROOT = "C:/Users/Anna/Documents/job-search-repo"
MASTER_RESUME = os.path.join(REPO_ROOT, "resumes", "Master_Resume.md")
JOB_DESCRIPTION = os.path.join(REPO_ROOT, "job_descriptions", "3083159_Amz_TS_Eng.txt")
OUTPUT_FILE = os.path.join(REPO_ROOT, "resumes", "Amazon_3083159.md")
# ============================================================

def extract_content_by_sections(master_resume_file, tags_to_include):
    """
    Extracts content from the master resume organized by headings, including only lines with matching tags.
    Sections with no matching lines are kept with a placeholder.
    """
    with open(master_resume_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    tag_patterns = [re.compile(r'#' + re.escape(tag) + r'\b', re.IGNORECASE) for tag in tags_to_include]

    tailored_lines = []
    current_section = []
    section_has_content = False

    for line in lines:
        # Detect headings (## or ###)
        if re.match(r'^(##+)\s', line):
            # Flush the previous section
            if current_section:
                if not section_has_content:
                    current_section.append("  _No matched content_\n")
                tailored_lines.extend(current_section)
            # Start new section
            current_section = [line]
            section_has_content = False
        else:
            # Check for matching tags in the line
            if any(pattern.search(line) for pattern in tag_patterns):
                current_section.append(line)
                section_has_content = True
            elif section_has_content:
                # Preserve the line if already matched content in this section
                current_section.append(line)

    # Flush last section
    if current_section:
        if not section_has_content:
            current_section.append("  _No matched content_\n")
        tailored_lines.extend(current_section)

    return tailored_lines


def create_tailored_resume(master_resume_file, job_description_file, output_file):
    matching_tags = get_matching_tags(master_resume_file, job_description_file)

    if not matching_tags:
        print("No matching tags found. Tailored resume will be mostly empty.")
    
    print(f"Matching tags found: {', '.join(sorted(matching_tags))}")

    matched_content = extract_content_by_sections(master_resume_file, matching_tags)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Tailored Resume\n\n")
        f.write(f"**Job Description Tags:** {', '.join(sorted(matching_tags))}\n\n")
        for line in matched_content:
            f.write(line)

    print(f"Tailored resume created: {output_file}")


if __name__ == "__main__":
    # Print paths for confirmation
    print("The script will use the following files:")
    print(f"Master Resume:      {MASTER_RESUME}")
    print(f"Job Description:    {JOB_DESCRIPTION}")
    print(f"Output Tailored MD: {OUTPUT_FILE}\n")
    
    input("Press Enter to run the script with these files...")

    create_tailored_resume(MASTER_RESUME, JOB_DESCRIPTION, OUTPUT_FILE)
