import tkinter as tk
from google.cloud import translate_v2 as translate

def detect_language(text):
    client = translate.Client()
    result = client.detect_language(text)
    detected_language = result['language']
    return detected_language

def translate_text():
    source_text = source_entry.get()
    target_language = target_language_entry.get()

    # Automatically detect the source language
    detected_language = detect_language(source_text)

    # Translate the text
    result = client.translate(source_text, source_language=detected_language, target_language=target_language)
    translated_text = result['input']

    # Update the GUI with the translated text
    translated_text_var.set(translated_text)
    detected_language_var.set(detected_language)

# Set up the GUI
root = tk.Tk()
root.title("Text Translator")

# Create GUI components
source_label = tk.Label(root, text="Source Text:")
source_entry = tk.Entry(root, width=40)
target_language_label = tk.Label(root, text="Target Language:")
target_language_entry = tk.Entry(root, width=10)
translate_button = tk.Button(root, text="Translate", command=translate_text)
translated_text_label = tk.Label(root, text="Translated Text:")
translated_text_var = tk.StringVar()
translated_text_display = tk.Label(root, textvariable=translated_text_var)
detected_language_var = tk.StringVar()
detected_language_display = tk.Label(root, textvariable=detected_language_var)

# Grid layout
source_label.grid(row=0, column=0, sticky="e")
source_entry.grid(row=0, column=1, columnspan=2)
target_language_label.grid(row=1, column=0, sticky="e")
target_language_entry.grid(row=1, column=1)
translate_button.grid(row=1, column=2)
translated_text_label.grid(row=2, column=0, sticky="e")
translated_text_display.grid(row=2, column=1, columnspan=2)
detected_language_display.grid(row=3, column=1)

# Run the GUI
root.mainloop()