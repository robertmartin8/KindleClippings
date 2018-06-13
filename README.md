<p align="center">
    <img width=60% src="https://github.com/robertmartin8/KindleClippings/blob/master/media/logo.png">
</p>

<!-- buttons -->
<p align="center">
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/python-v2,3-blue.svg"
            alt="python"></a> &nbsp;
    <!-- <a href="https://pypi.org/project/PyPortfolioOpt/">
        <img src="https://img.shields.io/badge/pypi-v0.1.0rc1-brightgreen.svg?style=flat-square"
            alt="python"></a> &nbsp; -->
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/license-MIT-blue.svg"
            alt="MIT license"></a> &nbsp;
    <a href="https://github.com/robertmartin8/PyPortfolioOpt/graphs/commit-activity">
        <img src="https://img.shields.io/badge/Maintained%3F-yes-blue.svg"
            alt="maintained"></a> &nbsp;
</p>

One of the many great things about kindles is that you can highlight parts of your book to go back to later. However, it is perhaps surprising that there is no good way of aggregating the highlights (even per book).

KindleClippings is a utility born out of personal need, which fetches any highlights that you have made on your kindle, and organises them into plain text files per book. It is run from the command line using:

```bash
python KindleClippings.py
```

The result is a new folder with individual text files per book:

<p align="center">
    <img width=60% src="https://github.com/robertmartin8/KindleClippings/blob/master/media/screenshot.png">
</p>

In my workflow, I then copy these into Evernote, but the whole point is that you are now free to do whatever you want.

## Background

When you make highlights or add bookmarks on your kindle, they are stored to a text file on the kindle called `My Clippings.txt`. This has a regular format, which means that it can be parsed:

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

The only requirement for this project is to have python (either python 2 or python 3) installed on your system. For users on macOS, you don't have to worry about this because it is already installed. On Windows, python can be installed following the instructions [here](http://docs.python-guide.org/en/latest/starting/install3/win/).

## Basic usage

It is recommended that you download the `KindleClippings.py` and place it either in your home directory or the desktop. Connect your kindle, and make sure it exists in your filesystem. Then, open up your terminal/shell.

If you're on a mac, you *might* just be able to run

```bash
python KindleClippings.py
```

However, most users will need to specify the path to the kindle and optionally the path to the destination. By default, the script will create a folder called `KindleClippings` in the current directory, and place the resulting text files there (though this likely only works on mac). For example

```bash
python KindleClippings.py -source /Volumes/Kindle/
```

On windows, this might look something like:

```bash
python KindleClippings.py -source C:\Kindle -destination \
```

If the parsing is succesful, the script will print all of the exported titles

```txt
Exported titles:

To Kill a Mockingbird - Harper Lee.txt
A Clockwork Orange - 50th Anniversary Edition - Anthony Burgess.txt
The Road - Cormac McCarthy.txt
Fahrenheit 451 - Ray Bradbury.txt
Heart of Darkness - Joseph Conrad.txt
The Meaning of It All - Richard P Feynman.txt
The Selfish Gene - 30th Anniversary Edition - Richard Dawkins.txt
```

## About

I originally forked [`firewood`](https://github.com/sebpearce/firewood), but I realised that my fork was fundamentally different to firewood – to the extent that it has become a different solution.

If you play around with `firewood` enough, you'll find that sometimes it can just completely break.
This is because firewood relies on the regular order of the `My  Clippings.txt` file from the kindle. For the most part, this is a fair assumption. However, I have found that very occasionally, kindle will insert an extra blank line that will prevent the whole program from functioning.

My solution does require regularity, but it is a lot more robust to irregularity. We first split the text file into individual highlights, then proceed from there.

Sometimes when you make a highlight on kindle, then delete it, it still gets stored into clippings. So if you make a wrong highlight and redo it, you'll end up with multiple very similar highlights. I haven't yet decided whether this is worth fixing, but in my workflow it's not very important.
