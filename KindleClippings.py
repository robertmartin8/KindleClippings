from __future__ import print_function
import re
import os

# Change this depending on your computer / kindle version
SOURCE_FILE = "/Volumes/Kindle/documents/My Clippings.txt"


def remove_chars(s):
    """
    This is a utility function that removes special characters from the string, so that it can
    become a valid filename.
    :param s: input string
    :return: the input string, stripped of special characters
    """
    # Replace colons with a hyphen so "A: B" becomes "A - B"
    s = re.sub(" *: *", " - ", s)
    # Remove question marks or ampersands
    s = s.replace("?", "").replace("&", "and")
    # Replace ( ) with a hyphen so "this (text)" becomes "this - text"
    s = re.sub(r"\((.+?)\)", r"- \1", s)
    # Delete filename chars tht are not alphanumeric or ; , _ -
    s = re.sub(r"[^a-zA-Z\d\s;,_-]+", "", s)
    # Trim off anything that isn't a word at the start & end
    s = re.sub(r"^\W+|\W+$", "", s)
    return s


def parse_highlights(dirname="kindle_clippings"):
    """
    Each clipping always consists of 5 lines:
    - title line
    - clipping info/metadata
    - a blank line
    - clipping text
    - a divider made up of equals signs
    Thus we can parse the clippings, and organise them by book.

    :param dirname: the output directory where all of organised highlights will go
    :type dirname: str
    :return: organises kindle highlights by book .
    """
    # Check that the source file (on the kindle) exists
    if not os.path.isfile(SOURCE_FILE):
        raise IOError("ERROR: cannot find " + SOURCE_FILE)

    # Create the output directory if it doesn't exist
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    # This will keep track of the titles that we have already processed
    output_files = set()
    title = ""

    # Open clippings textfile and read data in lines
    with open(SOURCE_FILE, "r") as f:
        # Individual highlights within clippings are separated by ==========
        for highlight in f.read().split("=========="):
            # For each highlight, we split it into the lines
            lines = highlight.split("\n")[1:]
            # Don't try to write if we have no body
            if len(lines) < 3 or lines[3] == "":
                continue
            # Set title and trim the hex character
            title = lines[0]
            if title[0] == "\ufeff":
                title = title[1:]

            # Remove characters and create path
            outfile_name = remove_chars(title) + ".txt"
            path = dirname + "/" + outfile_name

            # If we haven't seen title yet, set mode to write. Else, set to append.
            if outfile_name not in (list(output_files) + os.listdir(dirname)):
                mode = "w"
                output_files.add(outfile_name)
            else:
                # If the title exists, read it as text so that we won't append duplicates
                mode = "a"
                with open(path, "r") as textfile:
                    current_text = textfile.read()

            clipping_text = lines[3]

            with open(path, mode) as outfile:
                # Write out the the clippings text if it's not already there
                if clipping_text not in current_text:
                    outfile.write(f"{clipping_text}\n\n...\n\n")

    print_function("\nExported titles:\n")
    for i in output_files:
        print_function(i)
