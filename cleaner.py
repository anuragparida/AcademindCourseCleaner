import os
#dir_list = [f.path for f in os.scandir(os.path.dirname(os.path.realpath(__file__))) if f.is_dir()]
dir_list = [f.path for f in os.scandir() if f.is_dir()]

main_path = os.getcwd()

for dir in dir_list:
    # CHANGES PATH TO CURRENT DIRECTORY
    os.chdir(main_path + dir)

    # CREATES HTML AND ZIPS DIRECTORIES
    if 'html' not in [f.name for f in os.scandir() if f.is_dir()]:
        os.mkdir("html")
    if 'zips' not in [f.name for f in os.scandir() if f.is_dir()]:
        os.mkdir("zips")

    # CHECKS FILE FOR RELEVANT EXTENSION AND MOVES(RENAMES) IT
    for file in [f.name for f in os.scandir() if f.is_file()]:
        ext = os.path.splitext(file)[1]
        if ext == ".srt":
            os.remove(file)
        elif ext == ".html" or ext == ".htm":
            os.rename(file, 'html/' + file)
        elif ext == ".zip" or ext == ".rar" or ext == ".7z":
            os.rename(file, "zips/" + file)

    # DELETES HTML AND ZIPS DIRECTORIES IF THEY ARE EMPTY AT THE END
    if len(os.listdir("html")) == 0:
        os.rmdir("html")
    if len(os.listdir("zips")) == 0:
        os.rmdir("zips")
