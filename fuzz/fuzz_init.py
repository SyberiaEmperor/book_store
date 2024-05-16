
import os
import fnmatch
import coverage

if __name__ == '__main__':
    for f in os.listdir('./fuzz'):
        if fnmatch.fnmatch(f,'*_fuzz.py'):
            os.system(f"coverage run --branch -a ./fuzz/{f} --runs 1000")
