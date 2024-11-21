import os

fpath = input("Enter the path to the folder: ").strip()

if not os.path.exists(fpath):
    print("Error: The folder does not exist.")
else:
    files = []
    for f in os.listdir(fpath):
        if os.path.isfile(os.path.join(fpath, f)):
            files.append(f)

    if not files:
        print("The folder is empty. No files to rename.")
    else:
        files.sort() # Sort files alphabetically

        # Rename files sequentially
        for i, fname in enumerate(files, start=1):
            opath = os.path.join(fpath, fname)
            fextension = os.path.splitext(fname)[1]
            nname = f"{i}{fextension}"
            npath = os.path.join(fpath, nname)

            try:
                os.rename(opath, npath)
                print("Renamed",fname,"to",nname)
            except PermissionError:
                print("Error: Permission denied for",fname)
            except Exception as e:
                print("Error: Could not rename",fname,". Reason:",e)
