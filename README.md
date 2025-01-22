# magazine-merge

A Python script to merge a large number of periodical PDFs into multi-issue volumes.

In addition to `sys`, `re`, and `os`, this script uses the following modules:

* [pypdf](https://pypi.org/project/pypdf/)
* [natsort](https://pypi.org/project/natsort/)

The script as written assumes that you have a directory containing multiple PDFs, each of which has some kind of volume number in the filename (such as a year). I wrote it with the following file structure in mind:

```bash
|--magazine-merge.py
| magazines
    |--issue1feb2006.pdf
    |--issue2march2006.pdf
    |--...
```

All that being said, the regex pattern for file titles, path, and naming conventions are all easily modified to suit your needs.

## Original use case

I had purchased 72 PDF issues of a magazine (*The Gift of Stitching*, or TGOSM) in PDF format and wanted to browse them more conveniently. I decided to merge them into PDFs by year.

Before:

[List of many files: issue1feb2006, issue2march2006, issue3april2006, and so on](img/01-before.png)

After:

[List of 7 files: TGOSM-2006 to TGOSM-2012](img/02-after.png)
