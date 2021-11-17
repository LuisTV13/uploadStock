import os
import glob


def eliminarxlsx():
    files = glob.glob('adjunto/*.xlsx', recursive=True)

    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s: %s" % (f, e.strerror))