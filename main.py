import fitz  # PyMuPDF
from googletrans import Translator

def translate_pdf_to_turkish(pdf_path, output_path):
    # Initialize PyMuPDF
    doc = fitz.open(pdf_path)
    
    # Initialize Google Translator
    translator = Translator()
    
    translated_text = ""
    
    # Iterate through the pages
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text = page.get_text()
        
        # Translate the text to Turkish
        translated = translator.translate(text, src='auto', dest='tr').text
        translated_text += translated + "\n\n"
        
    # Save the translated text to a new file
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(translated_text)
    
    print(f"Translation completed! The translated file is saved as '{output_path}'.")

# Example usage
pdf_path = "Vex V5 GameManual 24-25.pdf"  # Path to your PDF file
output_path = "translated_to_turkish.txt"  # Output file path
translate_pdf_to_turkish(pdf_path, output_path)
