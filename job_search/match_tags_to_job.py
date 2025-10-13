# match_tags_to_job.py

import re

def get_matching_tags(master_resume_file, job_description_file):
    """
    Scans the master resume for tags and matches them to keywords in the job description.
    
    Returns:
        matching_tags (list): List of tags found in both the resume and job description.
    """
    # Load Master Resume
    with open(master_resume_file, 'r', encoding='utf-8') as f:
        resume_content = f.read()

    # Extract tags from resume (assumes #tag format)
    tags = re.findall(r'#(\w+)', resume_content)
    unique_tags = set(tags)

    # Load Job Description
    with open(job_description_file, 'r', encoding='utf-8') as f:
        job_desc_content = f.read().lower()

    # Match tags to job description
    matching_tags = [tag for tag in unique_tags if tag.lower() in job_desc_content]

    return matching_tags


if __name__ == "__main__":
    # Allow running as standalone script
    master_resume_file = input("Enter path to Master Resume (.md): ").strip()
    job_description_file = input("Enter path to Job Description (.txt): ").strip()

    matches = get_matching_tags(master_resume_file, job_description_file)

    print("\nMatching tags found:")
    for tag in sorted(matches):
        print(tag)

    print(f"\nTotal matching tags: {len(matches)}")
