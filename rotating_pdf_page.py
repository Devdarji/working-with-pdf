import PyPDF2


def rotate_pdf_pages(original_file, new_file, rotation):
    # Creating a pdf file object of original file
    pdf_file_obj = open(original_file, "rb")

    # Creating a pdf Reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)

    # Creating a pdf writer object for new pdf
    pdf_writer = PyPDF2.PdfWriter()

    # rotating each pages
    for page in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[page]
        page_obj.rotate(rotation)

        pdf_writer.add_page(page_obj)

    with open(new_file, "wb") as rotate_file:
        pdf_writer.write(rotate_file)

    pdf_file_obj.close()


original_file = "example.pdf"
new_file = "rotate_file.pdf"

# Rotation angle must be a multiple of 90
rotation = 270

rotate_pdf_pages(original_file=original_file, new_file=new_file, rotation=rotation)
