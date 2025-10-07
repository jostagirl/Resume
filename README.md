# Career Documents Repository

This repository is a personal hub for managing all my professional career materials, including resumes, cover letters, and job search resources. All documents are maintained in **Markdown (`.md`)** as the source of truth, with exports to PDF or Word (`.docx`) for applications. Git is used for version control to track edits, maintain history, and back up work.

---

## Repository Structure

<pre>
career-docs/
├── README.md                 ← This file
├── resumes/                  ← Master and tailored resumes
│   ├── Master_Resume.md      ← Comprehensive source of truth resume
│   ├── Resume_<Company>_<JobID>.md ← Tailored resume for specific job
│   └── Archive/              ← Older resume versions
├── cover_letters/            ← Templates and tailored letters
│   ├── Template_CoverLetter.md
│   ├── CoverLetter_<Company>_<JobID>.md
├── job_search/               ← Application tracker and notes
│   ├── tracker.md
│   └── resources.md
└── assets/                   ← Optional images or logos
</pre>

---

## Workflow

1. **Master Resume**
   - `Master_Resume.md` is the complete record of experience, skills, projects, and keywords.
   - Never submit this version directly; it is the foundation for tailored resumes.

2. **Creating Tailored Resumes**
   - Copy the master resume for each job:
     ```bash
     cp resumes/Master_Resume.md resumes/Resume_<Company>_<JobID>.md
     ```
   - Edit the copy to emphasize relevant experience, add keywords, and remove unrelated content.
   - Stage, commit, and push changes to GitHub.

3. **Cover Letters**
   - Start from `Template_CoverLetter.md` and create job-specific versions.
   - Tailor content for each application and track versions in Git.

4. **Exporting for Submission**
   - Convert Markdown files to PDF or Word:
     ```bash
     pandoc resumes/Resume_<Company>_<JobID>.md -o resumes/Resume_<Company>_<JobID>.pdf
     ```
   - Upload the exported file to the job portal.

5. **Application Tracking**
   - Log submissions in `job_search/tracker.md` with dates, company, job ID, and status.

---

## Notes

- Always update the master resume first when adding new experience or skills.
- Tailored resumes are derived copies; do not overwrite the master.
- Git tracks all changes, allowing you to revert or review previous versions.
