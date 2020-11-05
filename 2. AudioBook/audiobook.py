import pyttsx3
import PyPDF2
import time

book_path = "Book.pdf"
gender = 1
words_per_minute = 150
first_page = 14

def read_book(book_path, gender, words_per_minute, first_page):

    # Opens the book to be read
    book=open(book_path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)

    # Initializes the narrator
    narrator = pyttsx3.init()

    # Sets the voice of the narrator 
    narrator.setProperty('voice',narrator.getProperty('voices')[gender].id)

    # Sets the narration speed
    narrator.setProperty('rate', words_per_minute) 

    # Count and print total number of pages in the book
    total_pages = pdfReader.numPages
    print(total_pages) 
    
    # User input to continue reading or not
    continue_reading = "y"
    
    for num in range(first_page, total_pages):
        while continue_reading in ["y","Y"]:
            print("Reading Page Number : " + str(num))
            # Fetches text from the current page
            page = pdfReader.getPage(num)
            text = page.extractText()

            # Narrates the text
            narrator.say("Reading Page Number "+ str(num))
            time.sleep(2)
            narrator.say(text)
            narrator.runAndWait()

            continue_reading = input("Do you want to continue reading (y/n) ? ")

    book.close()

read_book(book_path, gender, words_per_minute, first_page)