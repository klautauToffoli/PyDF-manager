'''
    pdfFusion.py

    This script merges all the PDF files placed in the 
    folder PDFfiles into one merged file.

    Jose Antonio Klautau Toffoli 
    2023-09-09
'''

# Import libraries.
import os
import PyPDF2 as pdf

# Get list of PDF files in PDFfiles folder.
pdfFiles = os.listdir('PDFfiles')

for i in range(len(pdfFiles)):
    pdfFiles[i] = "PDFfiles/" + pdfFiles[i]


# Initialize merger object.
merger = pdf.PdfMerger()

# Iterate through pdf list merging files.
for file in pdfFiles:
    merger.append(file)

# Save merged file version.
merger.write('merged_file.pdf')

# Shut all file descriptors (input and output) and clear all memory usage.
merger.close()