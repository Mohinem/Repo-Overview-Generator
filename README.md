# Repo Overview Generator

A simple Python utility to bundle an entire Git repository into one ChatGPT-friendly Markdown file. It collects:

- **Metadata** (latest commit SHA, message, date)  
- **File tree** (via `git ls-files`)  
- **Contents** of each tracked file in fenced code blocks  
- **Language hints** based on file extension  
- **Automatic truncation** of very large files  

## Table of Contents

- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Options](#options)  
- [How It Works](#how-it-works)  
- [Customization](#customization)  
- [Contributing](#contributing)  
- [License](#license)  

## Features

- Zero dependencies beyond Git & Python 3.6+  
- Runs anywhere—point it at any local clone  
- YAML front-matter with commit info for easy parsing  
- Language-aware code blocks (`.py` → `python`, `.sh` → `bash`, etc.)  
- Truncation of files larger than 30 000 characters  

## Prerequisites

- Python 3.6 or newer  
- Git installed and on your `PATH`  
- A Git repository to document  

## Installation

```bash
git clone https://github.com/your-username/repo-overview-generator.git
cd repo-overview-generator
chmod +x gen_overview.py
```

## Usage

```bash
./gen_overview.py REPO_PATH [--output OUTPUT_PATH]
```

- `REPO_PATH` (required): Path to your Git repo root.  
- `-o, --output` (optional): Path for the output Markdown file.  
  Defaults to `project-overview.md` in your current directory.

### Examples

```bash
# Default output
./gen_overview.py ~/projects/my-repo

# Custom output
./gen_overview.py ~/projects/my-repo -o ~/Desktop/summary.md

# Using Python directly
python3 gen_overview.py /path/to/repo --output ./overview.md
```

## Options

| Flag             | Description               | Default               |
|------------------|---------------------------|-----------------------|
| `-o`, `--output` | Output Markdown file path | `project-overview.md` |
| `-h`, `--help`   | Show help message         |                       |

## How It Works

1. **Metadata**: `git rev-parse` & `git log` for SHA, message, date.  
2. **File List**: `git ls-files` enumerates tracked files.  
3. **Content Dump**:
   - Detects language from extension.  
   - Reads UTF-8 text.  
   - Truncates files > 30 000 chars.  
   - Wraps in fenced code blocks.  
4. **Front-Matter**: Prepends YAML header (project name, commit info, file count).

## Customization

- **Truncation Limit**: Change the `30_000` threshold in the script.  
- **File Filters**: Add conditions to skip paths in the loop.  
- **Language Map**: Update the `ext → lang` dict for new extensions.

## Contributing

1. Fork this repo.  
2. Create a branch: `git checkout -b feature/xyz`.  
3. Commit: `git commit -m "Add xyz"`.  
4. Push: `git push origin feature/xyz`.  
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

