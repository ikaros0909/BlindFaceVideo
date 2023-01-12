import PyPDF2

def read_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file) # 이부분을 수정
        num_pages = pdf_reader.numPages
        text = ''
        for i in range(num_pages):
            page = pdf_reader.getPage(i)
            text += page.extractText()
        return text

pdf_text = read_pdf("./pdf/hsb.pdf")
print(pdf_text)
