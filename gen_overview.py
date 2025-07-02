#!/usr/bin/env python3
import argparse
import subprocess
import pathlib
import textwrap

def run_git(cmd, cwd):
    return subprocess.check_output(["git"] + cmd, cwd=cwd).decode().strip()

def main():
    p = argparse.ArgumentParser(
        description="Generate a single markdown overview of a git repo."
    )
    p.add_argument(
        "repo_path",
        help="Path to the root of your git repository"
    )
    p.add_argument(
        "-o", "--output",
        default="project-overview.md",
        help="Where to write the generated markdown"
    )
    args = p.parse_args()

    ROOT = pathlib.Path(args.repo_path).expanduser().resolve()
    OUT  = pathlib.Path(args.output).expanduser().resolve()

    # sanity check
    if not (ROOT / ".git").exists():
        print(f"⚠️  {ROOT} does not look like a git repo.")
        return

    # 1) Metadata
    sha   = run_git(["rev-parse", "--short", "HEAD"], cwd=ROOT)
    msg   = run_git(["log", "-1", "--pretty=%s"], cwd=ROOT)
    when  = run_git(["log", "-1", "--date=iso", "--pretty=%cd"], cwd=ROOT)
    files = run_git(["ls-files"], cwd=ROOT).splitlines()

    # 2) Write front­-matter + file list
    with OUT.open("w") as f:
        f.write(textwrap.dedent(f"""\
        ---
        project: {ROOT.name}
        commit: {sha!r} (“{msg}”)
        date: {when}
        files: {len(files)}
        ---

        # {ROOT.name}

        ## 📦 File structure
        ```
        {"  \n".join(files)}
        ```

        ## 🔍 Files
        """))

        # 3) Dump each file
        for path in files:
            p = ROOT / path
            ext = p.suffix.lower().lstrip(".")
            lang = {
                "py": "python",
                "sh": "bash",
                "md": "markdown",
                "yml": "yaml",
                "yaml": "yaml",
                "dockerfile": "dockerfile",
                "bat": "batch"
            }.get(ext, ext or "text")

            f.write(f"\n### `{path}`\n```{lang}\n")
            try:
                text = p.read_text(encoding="utf-8")
                if len(text) > 30_000:
                    text = text[:30_000] + "\n...[truncated]...\n"
                f.write(text)
            except Exception as e:
                f.write(f"...could not read ({e})...\n")
            f.write("```\n")

    print(f"✅ Generated {OUT}")

if __name__ == "__main__":
    main()

