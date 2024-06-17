import os
import hashlib
import base64

# Constants
PREFIX = 'https://raw.githubusercontent.com/cd-public/books/main/'
BK_DIR = './books/'  # Updated path

def get_file_size(file_path):
    """Returns the size of the file in bytes."""
    return os.path.getsize(file_path)

# md5 source: https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file


def get_md5(file_path):
    """Returns the base64-encoded MD5 checksum of the file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return base64.b64encode(hash_md5.digest()).decode('utf-8')

def create_tsv():
    """Creates a TSV file with file URLs, sizes, and MD5 checksums."""
    with open('books.tsv', 'w') as tsv_file:
        tsv_file.write('TsvHttpData-1.0\n')
        for file_name in os.listdir(BK_DIR):
            file_path = os.path.join(BK_DIR, file_name)
            if os.path.isfile(file_path):
                file_url = PREFIX + file_name
                file_size = get_file_size(file_path)
                file_md5 = get_md5(file_path)
                tsv_file.write(f"{file_url}\t{file_size}\t{file_md5}\n")

create_tsv()

