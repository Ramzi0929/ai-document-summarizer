import tkinter as tk
from tkinter import filedialog, messagebox
from summarizer_main import summarize_and_export, get_latest_summary_text
import os 
import pyttsx3

class SummarizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Document Summarizer")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.selected_file = None

        # === Upload Section ===
        tk.Label(root, text="Upload a document", font=("Arial", 12, "bold")).pack(pady=(20, 5))
        tk.Button(root, text="Text / PDF / DOCX", command=self.browse_file, width=30).pack()
        self.file_label = tk.Label(root, text="No file selected", fg="gray")
        self.file_label.pack(pady=5)

        # === Export Section ===
        tk.Label(root, text="Save Summary", font=("Arial", 12, "bold")).pack(pady=(20, 5))
        tk.Button(root, text="Save as DOCX", command=lambda: self.export_summary("docx"), width=25).pack(pady=2)
        tk.Button(root, text="Save as PDF", command=lambda: self.export_summary("pdf"), width=25).pack(pady=2)

        # === Voice Button ===
        tk.Button(root, text="🔊 Read Summary", command=self.read_summary_aloud, width=25).pack(pady=(10, 5))

        # === Exit Button ===
        tk.Button(root, text="Exit", command=root.quit, fg="white", bg="red", width=10).pack(pady=(20, 0))

    def browse_file(self):
        filetypes = [("Text files", "*.txt"), ("PDF files", "*.pdf"), ("Word files", "*.docx")]
        path = filedialog.askopenfilename(title="Choose a file", filetypes=filetypes)
        if path:
            self.selected_file = path
            self.file_label.config(text=f"Selected: {os.path.basename(path)}", fg="black")

    def export_summary(self, format):
        if not self.selected_file:
            messagebox.showwarning("No File", "Please upload a document first.")
            return

        save_path = filedialog.asksaveasfilename(
            defaultextension=f".{format}",
            filetypes=[(f"{format.upper()} files", f"*.{format}")],
            title=f"Save summary as {format.upper()}"
        )

        if save_path:
            try:
                summarize_and_export(input_path=self.selected_file, export_format=format, export_path=save_path)
                messagebox.showinfo("Success", f"Summary saved as {format.upper()}!")
            except UnicodeDecodeError:
                messagebox.showerror("Encoding Error", "The file has unsupported encoding. Please use UTF-8.")
            except Exception as e:
                messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")

    def read_summary_aloud(self):
        try:
            summary_text = get_latest_summary_text()
            if not summary_text.strip():
                messagebox.showwarning("Empty Summary", "No summary to read.")
                return
            engine = pyttsx3.init()
            engine.say(summary_text)
            engine.runAndWait()
        except Exception as e:
            messagebox.showerror("Voice Error", f"Couldn't read the summary:\n{str(e)}")

# === Run GUI ===
if __name__ == "__main__":
    root = tk.Tk()
    app = SummarizerGUI(root)
    root.mainloop()
