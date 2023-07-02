import PyPDF2

pdf_files = ['sample_1.pdf', 'sample_2.pdf', 'sample_3.pdf']
merger = PyPDF2.PdfMerger()

for filename in pdf_files:
    pdfFiles = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFiles)
    merger.append(pdfReader)
pdfFiles.close()
merger.write('final_merge.pdf')