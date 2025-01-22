import re
import os

import sys
sys.path.append("path/to/your/local/modules")
# ensures that the script can find these modules:

import pypdf
import natsort

# Arguments:
# file_path: Path to the source PDF files.
# vol_num: Criterion by which input PDFs will be grouped in the output PDF.
#   May be year, quarter, volume number, etc.
# title_string: String to be prepended to the filename of the output PDF.

def file_list(file_path, vol_num):
    result = []
    pattern = rf"custom_string.*{vol_num}\.pdf"

    for filename in os.listdir(f"{file_path}"):
        if re.search(pattern, filename):
            result.append(file_path + "/" + filename)

    result = natsort.natsorted(result) 
    # This worked in the original use case, because the filenames were all issue1, issue2, etc.
    # You may need to find a different sorting solution for your use case.
    return result

def pdf_merge(file_path, vol_num, title_string):
    merger = pypdf.PdfWriter()
    pdf_list = file_list(file_path, vol_num)

    print("=== Merging the following files: ===")
    for pdf in pdf_list:
        print(pdf)
        input_file = open(pdf, "rb")
        merger.append(input_file)
        output_file = open(f"{title_string}-v{vol_num}.pdf", "wb")
        merger.write(output_file)
        merger.close()
        output_file.close()
    print("=== Merge complete ===\n")

fpath = "path/to/files"
volume = range(a, b)
tstring = "title_string"

# Example:
# fpath = "mymagazine"
# volume = range(2010, 2020)
# tstring = "My_Magazine"

for x in volume:
    pdf_merge(fpath, x, tstring)

