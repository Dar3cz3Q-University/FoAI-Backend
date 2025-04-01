import subprocess
import sys

def lint():
    sys.exit(subprocess.call(["poetry", "run", "pylint", "foai_backend/"]))
