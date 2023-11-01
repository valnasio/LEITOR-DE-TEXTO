from gtts import gTTS
import PyPDF2
import os

lingua = "pt"
livro = "o_pequeno_principe.pdf"

if not os.path.exists("audios"):
    os.makedirs("audios")

with open(livro, "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()

        text_parts = [text[i : i + 9999] for i in range(0, len(text), 9999)]

        for i, text_part in enumerate(text_parts):
            if text_part.strip():  # Verifica se o texto não está vazio
                tts = gTTS(text_part, lang=lingua)
                audio_filename = f"audios/{os.path.splitext(livro)[0]}_page_{page_num + 1}_part_{i + 1}.mp3"
                tts.save(audio_filename)
