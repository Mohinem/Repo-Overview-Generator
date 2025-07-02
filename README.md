# Repo Overview Generator

A simple Python utility to bundle an entire Git repository into one ChatGPT-friendly Markdown file. It collects:

- **Metadata** (latest commit SHA, message, date)  
- **File tree** (via `git ls-files`)  
- **Contents** of each tracked file in fenced code blocks  
- **Language hints** based on file extension  
- **Automatic truncation** of very large files  

---

## 📖 Table of Contents

- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Options](#options)  
- [How It Works](#how-it-works)  
- [Customization](#customization)  
- [Contributing](#contributing)  
- [License](#license)  

---

## 🚀 Features

- **Zero dependencies** beyond Git & Python 3.6+  
- **Runs anywhere**—point it at any local clone  
- **YAML front-matter** with commit info for easy parsing  
- **Language-aware** code blocks (`.py` → `python`, `.sh` → `bash`, etc.)  
- **Truncation** of files larger than 30 000 characters  

---

## 🛠 Prerequisites

- Python **3.6** or newer  
- A working **Git** installation  
- A **Git repository** you have read access to  

---

## 📥 Installation

Clone this repository (or copy the script) anywhere you like:

```bash
git clone https://github.com/your-username/repo-overview-generator.git
cd repo-overview-generator
chmod +x gen_overview.py

