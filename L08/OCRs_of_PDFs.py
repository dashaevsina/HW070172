### Libraries ###
import os, json
import pdf2image, pytesseract # Python tesseract is a wrapper for Google’s Tesseract-OCR Engine.
import functions
import PIL # Python Imaging Library (PIL) that adds image processing
from PIL import Image

def ocrPublication(pathToMemex, citationKey, language):
    publPath = functions.generatePublPath(pathToMemex, citationKey)
    pdfFile  = os.path.join(publPath, citationKey + ".pdf")
    jsonFile = os.path.join(publPath, citationKey + ".json")
    saveToPath = os.path.join(publPath, "pages")

    pdfFileTemp = functions.removeCommentsFromPDF(pdfFile) # Creates temporary file of a clean PDF 
                    # (in case the PDF is annotated) so that the annotations aren't deleted

    if not os.path.isfile(jsonFile):
        if not os.path.exists(saveToPath):
            os.makedirs(saveToPath)
        
        print("\t>>> OCR-ing: %s" % citationKey)

        textResults = {} # Creates a dictionary of the extracted text
        images = pdf2image.convert_from_path(pdfFileTemp)
        pageTotal = len(images) # Gets the total number of pages in PDF file
        pageCount = 1
        for image in images:
            image = image.convert('1')
            finalPath = os.path.join(saveToPath, "%04d.png" % pageCount) # Opens file and saves it to .png
            image.save(finalPath, optimize=True, quality=10)

            custom_config = r'-l fra+eng+nld+deu --psm 6' # psm 6: Page segmentation mode defines how 
                                                          # tesseract splits image into lines of text
                                                          # Mode 6 assumes a single uniform block of text.
                                                          # l is language
            text = pytesseract.image_to_string(image, config = custom_config) # Refers back to specified languages.
            textResults["%04d" % pageCount] = text

            print("\t\t%04d/%04d pages" % (pageCount, pageTotal))
            pageCount += 1

        with open(jsonFile, 'w', encoding='utf8') as f9: # Saves OCR results into a JSON file.
            json.dump(textResults, f9, sort_keys=True, indent=4, ensure_ascii=False)
    
    else:
        print("\t>>> %s has already been OCR-ed..." % citationKey)

    os.remove(pdfFileTemp) # Deletes the temporary clean version of the PDF

### Process all PDFs ###
def processAllPDFs():
    for subdir, dirs, files in os.walk(r'./_data'):
        for filename in files:
            filepath = subdir + os.sep + filename

            if filepath.endswith(".pdf"):
                print (filepath)

    


image_pdf = Image(filename="./_data")
