

# file-integrity-checker  
Simple Python file integrity checker

# File Integrity Checker

This is a simple Python script that helps verify the integrity of files by generating and comparing SHA256 hash values. It can be used to detect if a file has been changed or tampered with.

---

## Features

- Calculate SHA256 hash of a file  
- Save hash to a file for future verification  
- Verify if the current file matches the saved hash  

---

## How to Use

1. Run the script to generate the hash of the file you want to monitor:

```bash
python file_integrity_checker.py --create <file_path> --hashfile <hash_file>
````

2. Later, verify the file integrity using:

```bash
python file_integrity_checker.py --verify <file_path> --hashfile <hash_file>
```

---

## Requirements

Python 3.x

---

## How It Works

The script uses the SHA256 cryptographic hash function to generate a unique hash value for the contents of a file. This hash is saved to a separate file. When verifying, the script recalculates the hash of the current file and compares it with the saved hash to check if the file has been altered.

