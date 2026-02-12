# This script updates the README.md file with TryHackMe stats
# It replaces the content between THM_STATS_START and THM_STATS_END

from pathlib import Path

README_PATH = Path("README.md")

NEW_CONTENT = """
Rank: Example Rank
Global Ranking: Example Number
Rooms Completed: Example Number
""".strip()


def update_readme():
    readme_text = README_PATH.read_text(encoding="utf-8")

    start_tag = "<!-- THM_STATS_START -->"
    end_tag = "<!-- THM_STATS_END -->"

    if start_tag not in readme_text or end_tag not in readme_text:
        raise Exception("THM markers not found in README.md")

    before = readme_text.split(start_tag)[0]
    after = readme_text.split(end_tag)[1]

    updated_readme = (
        before
        + start_tag
        + "\n"
        + NEW_CONTENT
        + "\n"
        + end_tag
        + after
    )

    README_PATH.write_text(updated_readme, encoding="utf-8")


if __name__ == "__main__":
    update_readme()
    print("README.md updated successfully")
