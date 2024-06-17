import os
import hashlib

PREFIX = 'https://raw.githubusercontent.com/cd-public/books/main/'  # Base URL for the files on GitHub
BK_DIR = '../books/'  # Local directory containing the files

def calculate_md5(file_path): # source: https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file
    """Calculate the MD5 checksum of a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def create_tsv(bk_dir, prefix):
    """Create a TSV file with URL, file size, and MD5 checksum for each file in the directory."""
    with open("books.tsv", "w") as tsv_file:
        tsv_file.write("url\tsize\tmd5\n")  # Write the header row
        for root, _, files in os.walk(bk_dir):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                file_size = os.path.getsize(file_path)  # Get file size
                file_md5 = calculate_md5(file_path)  # Get MD5 checksum
                url = prefix + file_name  # Construct the URL
                tsv_file.write(f"{url}\t{file_size}\t{file_md5}\n")  # Write data row

if __name__ == "__main__":
    create_tsv(BK_DIR, PREFIX)
