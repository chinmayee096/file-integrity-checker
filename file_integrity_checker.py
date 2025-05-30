import hashlib
import json
import os
import argparse

# Function to compute SHA256 hash of a file
def compute_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for block in iter(lambda: f.read(4096), b""):
            sha256.update(block)
    return sha256.hexdigest()

# Function to create hash records for all files in a directory
def create_hashes(directory, output_file='hashes.json'):
    hashes = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            file_hash = compute_hash(full_path)
            hashes[full_path] = file_hash

    # Save hashes to JSON file
    with open(output_file, 'w') as f:
        json.dump(hashes, f, indent=4)
    print(f"Hashes saved to {output_file}")

# Function to verify current files against saved hashes
def verify_hashes(directory, hash_file='hashes.json'):
    if not os.path.exists(hash_file):
        print(f"Hash file {hash_file} does not exist. Please create hashes first.")
        return

    with open(hash_file, 'r') as f:
        saved_hashes = json.load(f)

    changed_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            current_hash = compute_hash(full_path)
            saved_hash = saved_hashes.get(full_path)
            if saved_hash != current_hash:
                changed_files.append(full_path)

    missing_files = [file for file in saved_hashes.keys() if not os.path.exists(file)]

    if changed_files or missing_files:
        print("WARNING: The following files have changed or are missing:")
        for file in changed_files:
            print(file)
        for file in missing_files:
            print(file + " (missing)")
    else:
        print("All files are intact.")

# Command-line interface setup
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Integrity Checker")
    parser.add_argument('action', choices=['create', 'verify'], help="Action to perform")
    parser.add_argument('--dir', required=True, help="Directory to scan")

    args = parser.parse_args()

    if args.action == 'create':
        create_hashes(args.dir)
    elif args.action == 'verify':
        verify_hashes(args.dir)
