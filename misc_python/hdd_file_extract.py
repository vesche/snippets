
# shitty python script for extracting files from a hdd on a windows system

import os
import win32api

filetypes = ['jpg', 'jpeg' 'bmp', 'pdf', 'doc', 'docx', 'xls', 'rtf', 'zip']

def list_available_drives():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    return drives

def file_count(txt_file):
    with open(txt_file) as f:
        return str(sum(1 for _ in f))

def create_batch_script(ext, txt_file):
    data = open(txt_file).read().splitlines()
    with open("{}.bat".format(ext), 'a') as f:
        f.write("@echo off\n")
        for fpath in data:
            f.write('copy "{}" {}\\{}\n'.format(fpath, os.getcwd(), ext))

def main():
    print ' '.join(list_available_drives())
    drive = raw_input("Drive letter? ")[0].upper() + ":\\"

    for ext in filetypes:
        print "Searching for {} files...".format(ext)
        os.system("dir /s /b /a {0}*.{1} >> {1}.txt".format(drive, ext, ext))
        print "{} {} files found!".format(file_count("{}.txt".format(ext)), ext)
        create_batch_script(ext, "{}.txt".format(ext))
        os.remove("{}.txt".format(ext))

        os.mkdir(ext)
        print "Extracting {} files...".format(ext)
        os.system("{}.bat >nul".format(ext))
        os.remove("{}.bat".format(ext))
        print "Finished extracting {} files!".format(ext)

if __name__ == "__main__":
    main()
