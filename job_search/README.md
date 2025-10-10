# Job Search Automation

This folder contains scripts and files used to maintain structured job title lists, track tags in your master resume, and prepare data for future automation of job searches. The two subtasks are **Job title search list** and **Master Resume tag counter.**

## Folder Contents

| File | Subtask | Purpose |
|------|---------|---------|
| `job_titles_master.md` | Job title search list | Editable master list of job titles, organized by category. This is the single source of truth. |
| `job_titles_master.csv` | Job title search list | Generated CSV from the Markdown list, including a timestamp comment. Ready for automation scripts. |
| `md_to_csv.py` | Job title search list | Python script to convert the Markdown master list into the CSV. Run this after editing the Markdown. |
| `jobsearch_automation.py` | Job title search list | *(Optional / Future)* Placeholder for scripts that use the CSV(s) to automate job search queries. |
| `tag_counter.py` | Master Resume tag counter | Python script that counts tags in your master resume. Useful for tracking changes you make to tag usage over time. |
| `tag_counts.csv` | Master Resume tag counter | `tag_counter.py`, showing counts of each tag. |
| `tracker.md` | Manual List | Manual list ofjobs applied for, containing Date, Company, Job #, Resume File, Status. |


## How to Use

### Job Title Search List
*Maintain a list of job titles I can search for that interest me and apply to my skill set.*

1. Edit `job_titles_master.md` to add, remove, or reorganize job titles.
2. Run `convert_md_to_csv.py` to regenerate `job_titles_master.csv`
3. Optionally, add tags to any job title using the `#` symbol:

```markdown
- Associate DevOps Engineer #automation #entrylevel
- Systems Support Engineer #support #systems
```
#### Notes
- **CSV files are overwritten on each run.** GitHub version history preserves past versions.

- `job_titles_master.csv` includes a timestamp comment in the first row for reference.

- Markdown **formatting for job titles must use ## for categories and - for list items.**

- **Tags in job titles must start with #. Multiple tags can be separated by spaces.**
  The script converts them to a comma-separated string in the CSV.
  
- FUTURE: CSV output can be used to automate job search.
### Master Resume Tag Counter
*Count and then output a list of unique tags in use and how many times used in my Master Resume file. Appends tags in use with date stamp into `tag_counts.csv` so that in the future I can do further analysis of how tags have changed overtime. Outputs changes since last run to console:
``` markdown
Total unique tags: 114

Tags changed since last run:

ProcessDefinition: Δ +1

Tags added or removed since last run:

Added tags:
 + ProcessDefinition
Removed tags:
 - Editing
 - Jellybeans
 ```

1. Edit `\resumes\Master_Resume.md` to add, remove, or reorganize tags on items.
2. Run `tag_counter.py` to generate `tag_counts.csv`

#### Notes

- `tag_counter.py` assumes a **consistent tagging format in your master resume.** 
  *ensure tags are formatted consistently for accurate counts.*

