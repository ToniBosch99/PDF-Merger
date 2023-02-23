from PyPDF2 import PdfMerger
from searcher import open_window

pdf_list, out_path = open_window()
print(pdf_list, out_path)


merger = PdfMerger()

for pdf in pdf_list:
    merger.append(pdf)

merger.write(out_path)
merger.close()