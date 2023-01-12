from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    # device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str

def extract_table_text(pdf_text):
    # 테이블 텍스트를 저장할 리스트
    table_text_list = []
    # pdf_text를 한 줄씩 읽어들인다
    for line in pdf_text.split('\n'):
        # 테이블 행을 판별하는 키워드를 포함하는 경우
        if '|' in line:
            table_text_list.append(line)
    return table_text_list


if __name__ == '__main__':
    pdf_text = convert_pdf_to_txt("./pdf/hsb.pdf")
    print("로딩성공!")
    table_text_list = extract_table_text(pdf_text)
    print("목록성공!", table_text_list)
    for text in table_text_list:
        print(text)


