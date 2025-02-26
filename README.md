# Reddit Bookmark Scripts

This project contains two scripts to help manage and create bookmarks for subreddits.

## 1. extract_subreddits.py

This script extracts subreddit URLs from a given source and saves them into a text file.

### Usage
1. Download the HTML file from the web that contains all the subreddit links.
2. Run the script.
3. Follow the prompts to provide the necessary input.
4. The script will save the extracted subreddit URLs into a text file.

## 2. create_bookmarks.py

This script reads a text file containing subreddit URLs and creates an HTML file with bookmarks.

### Usage
1. Run the script.
2. Select the text file with subreddit links when prompted.
3. The script will generate an HTML file with bookmarks in the same directory as the input file.

### Example
If the input file is `subreddits.txt`, the output file will be `subreddits.html`.