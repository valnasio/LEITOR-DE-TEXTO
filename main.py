from gtts import gTTS
import PyPDF2
import os

lingua = "pt"
text = ""

with open("Letra-do-Hino-Nacional-brasileiro.pdf", "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
   
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

tts = gTTS(text, lang=lingua)
tts.save("audio.mp3")

os.system('ffplay -autoexit -nodisp audio.mp3')