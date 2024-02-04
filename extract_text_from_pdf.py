import PyPDF2


def extract_text_from_pdf(file):
    # creating a pdf file object
    pdf_file_obj = open(file, "rb")

    # creating a pdf reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)

    # printing the number of pages in the pdf
    print(len(pdf_reader.pages))

    # creating a page object
    page_obj = pdf_reader.pages[0]

    # extracting text from page
    text = page_obj.extract_text()

    pdf_file_obj.close()

    return text


# PDF file path
pdf_file = "example.pdf"

# extract text from the pdf
text = extract_text_from_pdf(pdf_file)

# print text
print(text)
