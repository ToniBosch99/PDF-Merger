from PyPDF2 import PdfMerger
from searcher import open_window

pdf_list, out_folder, out_name = open_window()
print(pdf_list, out_folder, out_name)

# pdfs = [r"C:\Users\Toni\OneDrive\Escriptori\ETSEIB\MUEI\Q3\Tecnologia Energètica\Topic_2.pdf",
#  r"C:\Users\Toni\OneDrive\Escriptori\ETSEIB\MUEI\Q3\Tecnologia Energètica\Topic_3.pdf"]

# merger = PdfMerger()

# for pdf in pdfs:
#     merger.append(pdf)

# merger.write(r"C:\Users\Toni\OneDrive\Escriptori\ETSEIB\MUEI\Q3\Tecnologia Energètica\Merged.pdf")
# merger.close()