# ----- Imports ----- #

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import shutil
import os


# ----- Functions and procedures ----- #

def get_dir_name(entry):
    dir_name = filedialog.askdirectory(initialdir=os.getcwd(), title='Please select a directory') + os.sep
    entry.delete(0, 'end')
    entry.insert(0, dir_name)


def create_and_move(path, name, f, source):
    new_path = create(path, name)
    shutil.move(source + f, new_path)


def create(path, name):
    new_path = path + os.sep + name
    if not os.path.exists(new_path):
        try:
            os.mkdir(new_path)
        except OSError:
            print("Creation of the directory failed")
    return new_path


def sort(source, destination):
    files = os.listdir(source)

    for f in files:
        if f.lower().endswith((
                '.ai', '.bmp', '.gif', '.ico', '.jpeg', '.jpg', '.png', '.ps', '.psd', '.svg', '.tif',
                '.tiff')):  # pictures
            create_and_move(destination, 'Pictures', f, source)
        elif f.lower().endswith(
                ('.aif', '.cda', '.mid', '.midi', '.mp3', '.mpa', '.ogg', '.wav', '.wma', '.wpl')):  # audio
            create_and_move(destination, 'Audio', f, source)
        elif f.lower().endswith(
                ('.7z', '.arj', '.deb', '.pkg', '.rar', '.rpm', '.tar.gz', '.z', '.zip')):  # compressed
            create_and_move(destination, 'Compressed', f, source)
        elif f.lower().endswith(('.bin', '.dmg', '.iso', '.toast', '.vcd')):  # discs
            create_and_move(destination, 'Disks', f, source)
        elif f.lower().endswith(
                ('.csv', '.dat', '.db', '.dbf', '.log', '.mdb', '.sav', '.sql', '.tar', '.xml')):  # data
            create_and_move(destination, 'Databases', f, source)
        elif f.lower().endswith(('.apk', '.bat', '.bin', '.cgi', '.pl', '.com', '.exe', '.gadget', '.jar', '.py',
                                 '.wsf')):  # executables
            create_and_move(destination, 'Executables', f, source)
        elif f.lower().endswith(('.fnt', '.fon', '.otf', '.ttf')):  # fonts
            create_and_move(destination, 'Fonts', f, source)
        elif f.lower().endswith(('.asp', '.aspx', '.cer', '.cfm', '.css', '.htm', '.html', '.js', '.jsp', '.part',
                                 '.php', '.rss', '.xhtml')):  # internet
            create_and_move(destination, 'Internet', f, source)
        elif f.lower().endswith(('.key', '.odp', '.pps', '.ppt', '.pptx')):  # presentations
            create_and_move(destination, 'Presentations', f, source)
        elif f.lower().endswith(
                ('.c', '.class', '.cpp', '.cs', '.h', '.java', '.sh', '.swift', '.vb')):  # programming files
            create_and_move(destination, 'Programming Files', f, source)
        elif f.lower().endswith(('.ods', '.xlr', '.xls', '.xlsx')):  # spreadsheets
            create_and_move(destination, 'Spreadsheets', f, source)
        elif f.lower().endswith(('.3gp', '.avi ', '.flv', '.h264', '.m4v', '.mkv', '.mov', '.mp4', '.mpg', '.mpeg',
                                 '.rm', '.swf', '.vob', '.wmv')):  # videos
            create_and_move(destination, 'Videos', f, source)
        elif f.lower().endswith(
                ('.doc', '.docx ', '.odt', '.pdf', '.rtf', '.tex', '.txt', '.wks', '.wps', '.wpd')):  # text files
            create_and_move(destination, 'Text Files', f, source)
        elif f.lower().endswith(('.bak', '.cab ', '.cfg', '.cpl', '.cur', '.dll', '.dmp', '.drv', '.icns', '.ini',
                                 '.lnk', '.msi', '.sys', '.tmp')):  # system files
            create_and_move(destination, 'System Files', f, source)

    messagebox.showinfo("Message", "Files have been successfully sorted!")


source_path = ""
destination_path = ""

# ----- Frame configurations ----- #
root = Tk()
root.title("File Sorter 1.2.2")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# ----- Entry forms ----- #

# Source entry form
source_entry = ttk.Entry(mainframe, width=25, text=source_path)
source_entry.grid(column=2, row=1, sticky=W)

# Destination entry form
destination_entry = ttk.Entry(mainframe, width=25, text=destination_path)
destination_entry.grid(column=2, row=2, sticky=W)

ttk.Label(mainframe, text="Source: ").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Destination: ").grid(column=1, row=2, sticky=W)

# ----- Buttons ----- #

# Search buttons
ttk.Button(mainframe, text="Search",
           command=lambda: get_dir_name(source_entry)).grid(column=3, row=1, sticky=W)
ttk.Button(mainframe, text="Search",
           command=lambda: get_dir_name(destination_entry)).grid(column=3, row=2, sticky=W)

# Sort buttons
ttk.Button(mainframe, text="Sort", command=lambda: sort(source_entry.get(),
                                                        create(destination_entry.get(),
                                                               "Sorted"))).grid(column=2, row=3, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
root.mainloop()
