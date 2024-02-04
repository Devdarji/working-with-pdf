import PyPDF2


# Function to create a new PDF file from existing content
def create_pdf(output_path, content):
    # Create a PdfWriter object from PyPDF2
    pdf_writer = PyPDF2.PdfWriter()

    # Add a page to the PdfWriter using the first page of the existing PDF content
    pdf_writer.add_page(PyPDF2.PdfReader(content).pages[0])

    # Open the output PDF file in binary write mode
    with open(output_path, "wb") as new_pdf:
        # Write the modified content to the new PDF file
        pdf_writer.write(new_pdf)


# Path to the existing PDF file
content = "example.pdf"

# Output path for the new PDF file
output_path = "new_pdf.pdf"

# Call the function to create a new PDF file
create_pdf(output_path=output_path, content=content)
