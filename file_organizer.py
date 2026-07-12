# updated
import os, shutil

def organize(folder):
    for f in os.listdir(folder):
        ext = f.split(".")[-1].lower()
        dest = os.path.join(folder, ext)
        os.makedirs(dest, exist_ok=True)
        shutil.move(os.path.join(folder, f), dest)

if __name__ == "__main__":
    organize(os.path.expanduser("~/Downloads"))
