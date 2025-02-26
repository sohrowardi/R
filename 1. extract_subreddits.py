from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog
import os

# Prompt user to select an HTML file
root = tk.Tk()
root.withdraw()
html_file_path = filedialog.askopenfilename(title="Select HTML file", filetypes=[("HTML files", "*.html")])

if html_file_path:
    # Path to the output text file
    output_file_path = os.path.join(os.path.dirname(html_file_path), 'subreddit_links.txt')

    # Read the HTML file
    with open(html_file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Find all subreddit links
    subreddit_links = set()
    for link in soup.find_all('a', href=True):
        href = link['href']
        if 'reddit.com/r/' in href:
            subreddit_links.add(href)

    # Write the links to a text file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for link in subreddit_links:
            file.write(link + '\n')

    print(f"Extracted {len(subreddit_links)} subreddit links to {output_file_path}")
else:
    print("No file selected.")