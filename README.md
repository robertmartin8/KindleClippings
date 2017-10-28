# KindleClippings

KindleClippings is a utility to fetch any highlights that you have made on your kindle, and organise them into plain text files per book.

I originally forked [firewood](https://github.com/sebpearce/firewood), but I realised that my fork was fundamentally different to firewood – to the extent that it has become a different solution.

If you play around with firewood enough, you'll find that sometimes it can just completely break.
This is because firewood relies on the regular order of the `My  Clippings.txt` file from the kindle. For the most part, this is a fair assumption. However, I have found that very occasionally, kindle will insert an extra blank line that will prevent the whole program from functioning.

My solution does require regularity, but it is a lot more robust to irregularity. We first split the text file into individual highlights, then proceed from there.

## Issues

When you make a highlight on kindle, then delete it, it still gets stored into clippings. So if you make a wrong highlight and redo it, you'll end up with multiple very similar highlights. I haven't yet decided whether this is worth fixing, but in my workflow it's not very important. 