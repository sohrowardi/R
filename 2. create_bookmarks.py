import subprocess
import sys

# Ensure required modules are installed
required_modules = ['tkinter']
for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])

import tkinter as tk
from tkinter import filedialog

def create_bookmarks(input_file, output_file):
    with open(input_file, 'r') as infile:
        urls = infile.readlines()

    with open(output_file, 'w') as outfile:
        outfile.write('<!DOCTYPE NETSCAPE-Bookmark-file-1>\n')
        outfile.write('<!-- This is an automatically generated file.\n')
        outfile.write('     It will be read and overwritten.\n')
        outfile.write('     DO NOT EDIT! -->\n')
        outfile.write('<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">\n')
        outfile.write('<TITLE>Bookmarks</TITLE>\n')
        outfile.write('<H1>Bookmarks</H1>\n')
        outfile.write('<DL><p>\n')

        for url in urls:
            url = url.strip()
            if url:
                subreddit_name = url.split('reddit.com/r/')[-1].strip('/')
                outfile.write(f'    <DT><A HREF="{url}">r/{subreddit_name}</A></DT>\n')

        outfile.write('</DL><p>\n')

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    input_file = filedialog.askopenfilename(title="Select the text file with subreddit links", filetypes=[("Text files", "*.txt")])
    if input_file:
        output_file = input_file.replace('.txt', '.html')
        create_bookmarks(input_file, output_file)
    else:
        print("No file selected.")
