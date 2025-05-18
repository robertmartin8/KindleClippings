# KindleClippings

<p align="center">
    <img width=60% src="https://github.com/robertmartin8/KindleClippings/blob/master/media/logo.png">
</p>

<!-- buttons -->
<p align="center">
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/python-v2,3-blue.svg" alt="python"></a> &nbsp;
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT license"></a> &nbsp;
    <a href="https://github.com/robertmartin8/PyPortfolioOpt/graphs/commit-activity">
        <img src="https://img.shields.io/badge/Maintained%3F-yes-blue.svg" alt="maintained"></a> &nbsp;
</p>

KindleClippings extracts your notes and highlights from the Kindle `My Clippings.txt` file and organises them into one file per book. Optionally, it can also create PDF or DOCX versions.

## Background

When you add highlights or bookmarks on your Kindle they are stored in `My Clippings.txt`. The file has a predictable structure, so it can be parsed automatically:

```txt
==========
The Selfish Gene: 30th Anniversary Edition (Richard Dawkins)
- Your Highlight on page 92 | location 1406-1407 | Added on Saturday, 26 March 2016 14:59:39

Perhaps consciousness arises when the brain's simulation of the world becomes so complete that it must include a model of itself.(4)

==========
Fahrenheit 451 (Ray Bradbury)
- Your Bookmark at location 346 | Added on Saturday, 26 March 2016 15:46:21


==========
Fahrenheit 451 (Ray Bradbury)
- Your Highlight at location 784-785 | Added on Saturday, 26 March 2016 18:37:26

Who knows who might be the target of the well-read man?
==========
```

## Prerequisites

Any version of Python 2 or 3 will work. On macOS Python is preinstalled and on Windows you can follow the [official instructions](http://docs.python-guide.org/en/latest/starting/install3/win/).

To enable PDF or DOCX conversion, install the required packages:

```bash
pip install -r requirements.txt
```

## Basic usage

1. Download `KindleClippings.py` and place it somewhere convenient (for example your home directory).
2. Connect your Kindle so that the device appears in your filesystem.
3. Run the script, specifying the path to your Kindle if necessary:

```bash
python KindleClippings.py -source /Volumes/Kindle/
```

By default the highlights are exported into a new `KindleClippings` folder in the current directory. Use the `-destination` option to choose a different output location.

Add the `-format` flag to also create PDF or DOCX versions:

```bash
python KindleClippings.py -source /Volumes/Kindle/ -format pdf
```

If the parsing is successful, the script prints all exported titles.

## About

This project began as a fork of [`firewood`](https://github.com/sebpearce/firewood) but has since diverged into its own solution. KindleClippings is more tolerant of irregularities in the clippings file because it splits the file into individual entries before processing them.

Occasionally deleted highlights still appear in `My Clippings.txt`, so duplicate entries may occur. In most workflows this is not a significant problem.
