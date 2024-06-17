import os
import hashlib
import base64

# Constants
PREFIX = 'https://raw.githubusercontent.com/cd-public/books/main/'
BK_DIR = '../books/'

def get_file_size(filepath):
    return os.path.getsize(filepath)

# md5 source: https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file
def get_md5_checksum(filepath):
    hash_md5 = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return base64.b64encode(hash_md5.digest()).decode('utf-8')

def generate_tsv(directory, prefix):
    tsv_lines = ["url\tsize\tmd5"]
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            url = f"{prefix}{filename}"
            size = get_file_size(filepath)
            md5 = get_md5_checksum(filepath)
            tsv_lines.append(f"{url}\t{size}\t{md5}")
    return tsv_lines

def save_tsv(tsv_lines, output_file):
    with open(output_file, 'w') as f:
        for line in tsv_lines:
            f.write(line + "\n")

if __name__ == "__main__":
    tsv_lines = generate_tsv(BK_DIR, PREFIX)
    save_tsv(tsv_lines, 'books.tsv')
