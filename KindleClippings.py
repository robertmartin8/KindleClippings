import re
import os
from shutil import copyfile

# Change these as appropriate
src = '/Volumes/Kindle/documents/My Clippings.txt'
dst = '/Users/User/clippings.txt'
copyfile(src, dst)

# The clippings file
filename = "clippings.txt"

# Firewood will output into a directory with this name
dirname = "kindle_clippings"

# Each clipping always consists of 5 lines:
# - title line
# - clipping info/metadata
# - a blank line
# - clipping text
# - a divider made up of equals signs

# so we track the index of the lines we care about, and use MOD to extract the
# "type" of the line from the absolute line number of the file


# check that file exists, otherwise exit
if not os.path.isfile(filename):
    print("ERROR: cannot find " + filename)
    print("Please make sure it is in the same folder as this script.")


def remove_chars(s):
    """
    Remove special characters from the string
    :param s: input string
    """
    # Replace colons with a hyphen so "A: B" becomes "A - B"
    s = re.sub(' *: *', ' - ', s)
    s = s.replace('?', '').replace('&', 'and')
    # Replace ( ) with a hyphen so "this (text)" becomes "this - text"
    s = re.sub(r'\((.+?)\)', r'- \1', s)
    # delete filename chars tht are not alphanumeric or ; , _ -
    s = re.sub(r'[^a-zA-Z\d\s;,_-]+', '', s)
    # trim off anything that isn't a word at the start & end
    s = re.sub(r'^\W+|\W+$', '', s)
    return s


# Create the output directory if it doesn't exist
if not os.path.exists(dirname):
    os.makedirs(dirname)

output_files = set()  # set of titles already processed
title = ''

# Open clippings textfile and read data in lines
f = open(filename)

for highlight in f.read().split("=========="):
    lines = highlight.split('\n')[1:]
    # Don't try to write if we have no body
    if len(lines) < 3 or lines[3] == '':
        continue

    # Set title and trim hex
    title = lines[0]
    if title[0] == '\ufeff':
        title = title[1:]

    clipping_text = lines[3]

    # Trim filename-unfriendly chars for outfile name
    outfile_name = remove_chars(title) + '.txt'

    # If we haven't seen title yet, set mode to write. Else, set to append
    if outfile_name not in output_files:
        mode = 'w'
        output_files.add(outfile_name)
    else:
        mode = 'a'

    path = dirname + '/' + outfile_name
    with open(path, mode) as outfile:
        # write out the current line (the clippings text)
        outfile.write("%s\n\n...\n\n" % clipping_text)

f.close()

print("\nExported titles:\n")
for i in output_files:
    print("%s" % i)
