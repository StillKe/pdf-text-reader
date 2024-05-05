from PyPDF2 import PdfReader

def print_pdf_contents(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PdfReader(file)
            for page in reader.pages:
                text = page.extract_text()
                print(text)
    except FileNotFoundError:
        print(f"Error: PDF file '{pdf_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    pdf_path = "Resume_Checklist.pdf"  # Replace with the actual path to your PDF file
    print_pdf_contents(pdf_path)
