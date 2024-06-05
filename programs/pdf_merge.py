from pypdf import PdfMerger
import os

pdfs = os.listdir("pdf_files")

merger = PdfMerger()

for pdf in pdfs:
    merger.append("pdf_files\\" + pdf)
   
with open("new.pdf", "wb") as f:
    merger.write("new.pdf")
