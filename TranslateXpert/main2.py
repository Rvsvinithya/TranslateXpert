import tkinter as tk
from googletrans import Translator

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Translator")

        # Source Language
        self.source_lang_label = tk.Label(root, text="Source Language:")
        self.source_lang_entry = tk.Entry(root)

        # Destination Language
        self.dest_lang_label = tk.Label(root, text="Destination Language:")
        self.dest_lang_entry = tk.Entry(root)

        # Source Text
        self.source_text_label = tk.Label(root, text="Enter Text:")
        self.source_text_widget = tk.Text(root, width=40, height=5)

        # Translated Text
        self.output_text_label = tk.Label(root, text="Translated Text:")
        self.output_text_widget = tk.Text(root, state=tk.DISABLED, width=40, height=5)

        # Translate Button
        self.translate_button = tk.Button(root, text="Translate", command=self.translate_text)

        # Layout
        self.source_lang_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.source_lang_entry.grid(row=1, column=0, padx=5, pady=5)

        self.dest_lang_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.dest_lang_entry.grid(row=3, column=0, padx=5, pady=5)

        self.source_text_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.source_text_widget.grid(row=5, column=0, padx=5, pady=5)

        self.output_text_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.output_text_widget.grid(row=7, column=0, padx=5, pady=5)

        self.translate_button.grid(row=8, column=0, pady=10)

    def translate_text(self):
        src_lang = self.source_lang_entry.get()
        dest_lang = self.dest_lang_entry.get()
        text = self.source_text_widget.get("1.0", tk.END).strip()

        translator = Translator()

        try:
            translation = translator.translate(text, src=src_lang, dest=dest_lang)
            self.output_text_widget.config(state=tk.NORMAL)
            self.output_text_widget.delete("1.0", tk.END)
            self.output_text_widget.insert(tk.END, f"Translation from {src_lang} to {dest_lang}:\n")
            self.output_text_widget.insert(tk.END, translation.text)
        except Exception as e:
            self.output_text_widget.config(state=tk.NORMAL)
            self.output_text_widget.delete("1.0", tk.END)
            self.output_text_widget.insert(tk.END, f"Translation Error: {str(e)}")
        finally:
            self.output_text_widget.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()