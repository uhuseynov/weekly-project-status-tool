# Weekly Project Status Report Tool

A small command-line tool that collects weekly project updates and saves them as a Markdown status report.

## What it does

The tool asks for a project name, project manager, completed work, delayed or blocked work, risks, and next steps. It then:

- Sets the status to **At risk** when delays or risks are reported.
- Sets the status to **On track** when no delays or risks are reported.
- Writes the report to `weekly_status.md`.
- Shows `None reported` for sections left empty.

## Requirements

- Python 3. Basic functionality uses only Python's standard library; no extra packages are required.

## Run it

Open a terminal in the project folder and run:

```powershell
python status_report.py
```

Answer the prompts. For multiple items in a section, separate them with commas. The generated report will be saved as `weekly_status.md` in the current folder.

## Example input

```text
Project name: Website launch
Project manager: Alex
Completed work: Homepage design approved, Content drafted
Delayed or blocked work: Payment integration
Risks: Payment provider access is pending
Next steps: Follow up with provider, Test checkout
```

## Example output

```markdown
# Weekly Status: Website launch

- **Date:** YYYY-MM-DD
- **Project manager:** Alex
- **Status:** At risk

## Completed this week
- Homepage design approved
- Content drafted

## Delayed or blocked
- Payment integration

## Risks
- Payment provider access is pending

## Next steps
- Follow up with provider
- Test checkout
```

## Project files

- `status_report.py` — the report generator.
- `weekly_status.md` — generated report (created when the tool runs).

## Current limitations

- Status is determined by simple rules: any delay or risk makes the project **At risk**.
- Items are entered as comma-separated text.
- The tool does not store project history or send reports automatically.

## Possible next improvements

- Ask for a reporting period and project owner details.
- Add more status choices and let the user confirm the suggested status.
- Save reports in a separate folder with unique filenames so earlier reports are preserved.
- Add input validation for commas within an individual item.
