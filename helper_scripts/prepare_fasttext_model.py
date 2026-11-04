import os
import gzip
import shutil

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def prep_embedding_model(gz_filename='cc.en.300.bin.gz', out_filename='cc.en.300.bin'):
    # Look in current working directory first, then root directory
    gz_path = gz_filename if os.path.exists(gz_filename) else os.path.join(ROOT_DIR, gz_filename)
    out_path = os.path.join(ROOT_DIR, out_filename)

    if not os.path.exists(gz_path):
        print(f"Error: Archive '{gz_filename}' not found.")
        print("Please download it from https://fasttext.cc/docs/en/crawl-vectors.html")
        return

    print(f"Extracting {gz_path} to {out_path} (this may take several minutes)...")
    with gzip.open(gz_path, 'rb') as f_in:
        with open(out_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print(f"Successfully extracted model to {out_path}")


if __name__ == '__main__':
    prep_embedding_model()
