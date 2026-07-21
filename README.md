# File Integrity Monitor

A Python-based File Integrity Monitor that detects changes in files by comparing SHA-256 hashes between consecutive scans.

This project was developed as part of my software engineering learning journey, with an emphasis on understanding the underlying concepts instead of relying on existing security tools.

## Features

- Recursively scans all files in a selected directory.
- Generates SHA-256 hashes for every file.
- Stores scan results in a JSON file.
- Compares the current scan with the previous scan.
- Detects:
  - New files
  - Modified files
  - Deleted files

## Technologies Used

- Python 3
- `os`
- `hashlib`
- `json`

## Project Structure

```text
file-integrity-monitor/
├── data/
│   └── scan_results.json
├── .gitignore
├── LICENSE
├── README.md
└── main.py
```

## How It Works

1. Loads the previous scan from `data/scan_results.json` (if available).
2. Prompts the user to enter a folder path.
3. Validates the provided path.
4. Recursively scans all files inside the folder.
5. Generates a SHA-256 hash for every file.
6. Compares the current scan with the previous scan.
7. Reports:
   - New files
   - Modified files
   - Deleted files
8. Saves the current scan for future comparisons.

## Installation

1. Clone the repository.

```bash
git clone <repository-url>
```

2. Open the project directory.

```bash
cd file-integrity-monitor
```

3. Run the program.

```bash
python main.py
```

## Running the Program

Execute the program and enter the path of the folder you want to monitor when prompted.

## Example Output

```text
Enter folder path:
C:\Users\Example\Documents

Valid Folder!

New files detected: 2
Modified files detected: 1
Deleted files detected: 0
```

## Current Limitations

- Reads the entire file into memory before generating its hash.
- Stores only the latest scan.
- Does not yet support command-line arguments.
- Error handling can be further improved.

## Next Version (v1.1)

The next update will focus on improving usability and code quality.

Planned improvements:

- Better folder validation.
- Cleaner console output.
- Improved exception handling.
- General code cleanup and refactoring.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.