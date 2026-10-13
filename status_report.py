from datetime import date


def ask_list(question):
    answer = input(question).strip()

    if not answer:
        return []

    return [item.strip() for item in answer.split(",") if item.strip()]


def main():
    print("Weekly Project Status Report")
    print("----------------------------")

    project_name = input("Project name: ").strip()
    if not project_name:
        project_name = "Unnamed project"

    owner = input("Project manager: ").strip()
    if not owner:
        owner = "Not specified"

    completed = ask_list("Completed work (separate items with commas): ")
    delayed = ask_list("Delayed or blocked work (separate items with commas): ")
    risks = ask_list("Risks (separate items with commas): ")
    next_steps = ask_list("Next steps (separate items with commas): ")

    if delayed or risks:
        status = "At risk"
    else:
        status = "On track"

    report = [
        f"# Weekly Status: {project_name}",
        "",
        f"- **Date:** {date.today().isoformat()}",
        f"- **Project manager:** {owner}",
        f"- **Status:** {status}",
        "",
        "## Completed this week",
    ]

    report.extend(format_items(completed))
    report.extend(["", "## Delayed or blocked"])
    report.extend(format_items(delayed))
    report.extend(["", "## Risks"])
    report.extend(format_items(risks))
    report.extend(["", "## Next steps"])
    report.extend(format_items(next_steps))
    report.append("")

    with open("weekly_status.md", "w", encoding="utf-8") as file:
        file.write("\n".join(report))

    print("\nReport saved as weekly_status.md")


def format_items(items):
    if not items:
        return ["- None reported"]

    return [f"- {item}" for item in items]


if __name__ == "__main__":
    main()