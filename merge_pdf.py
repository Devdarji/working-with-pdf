import PyPDF2


# Function to merge multiple PDF files into a single PDF
def merge_pdf_files(pdf_list, output_path):
    # Create a PdfMerger object from PyPDF2
    pdf_merger = PyPDF2.PdfMerger()

    # Iterate through the list of PDF files and append them to the PdfMerger
    for pdf in pdf_list:
        pdf_merger.append(pdf)

    # Open the output PDF file in binary write mode
    with open(output_path, "wb") as merged_pdf:
        # Write the merged content to the output PDF file
        pdf_merger.write(merged_pdf)


# List of PDF files to be merged
pdf_list = ["example.pdf", "example2.pdf"]

# Output path for the merged PDF file
output_path = "merged.pdf"

# Call the function to merge PDF files
merge_pdf_files(pdf_list=pdf_list, output_path=output_path)
