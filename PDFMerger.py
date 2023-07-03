# PROJECT 04 : PDF MERGER

# modules to be installed:
# 1. pip install pypdf2 (this is installing name) and import as "PyPDF2"

import PyPDF2
# with this module we can do slicing,merging of PDFs

pdfiles=["1.pdf", "2.pdf"]   #can add any no. of PDFs
merger=PyPDF2.PdfMerger()
for filename in pdfiles:
        pdfFile = open(filename, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFile)
        merger.append(pdfReader)
pdfFile.close()
merger.write('merged.pdf')

#here the two pdfs "1.pdf" and "2.pdf" have been successfully merged i.e. "merged.pdf" ; we can check it in the 5 projects section