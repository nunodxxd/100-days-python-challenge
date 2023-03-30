import tkinter as tk
import time

#  TO DO:
# create random sentence generator

class TypingSpeedTest:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Speed Test")
        self.master.geometry("500x200")
        self.master.resizable(False, False)
        
        self.prompt_label = tk.Label(self.master, text="Type the following sentence:")
        self.prompt_label.pack(pady=10)
        
        self.sentence = "The quick brown fox jumps over the lazy dog"
        self.sentence_words = self.sentence.lower().split()
        self.sentence_label = tk.Label(self.master, text=self.sentence, font=("Helvetica", 16))
        self.sentence_label.pack(pady=10)
        
        self.entry = tk.Entry(self.master, width=50, state="disabled")
        self.entry.pack(pady=10)
        self.entry.focus()
        
        self.start_time = None
        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack(pady=10)
        
        self.button = tk.Button(self.master, text="Start", command=self.start_test)
        self.button.pack()
    
    def start_test(self):
        self.button.config(state="disabled")
        self.entry.config(state="normal") 
        self.entry.delete(0, tk.END)
        self.entry.focus()
        self.start_time = time.time()
        self.master.bind("<Return>", self.end_test)
        self.entry.config(state="normal")
        self.result_label.config(text="")
    
    def end_test(self, event):
        self.master.unbind("<Return>")
        elapsed_time = time.time() - self.start_time
        input_text = self.entry.get()
        input_words = input_text.lower().split()
        uncorrect_words = [w1 for w1, w2 in zip(self.sentence_words, input_words) if w1 != w2]
        gross_wpm = len(input_words) / elapsed_time * 60 
        net_wpm = (len(input_words) - len(uncorrect_words)) / elapsed_time * 60 
        accuracy = (net_wpm / gross_wpm) * 100
        self.result_label.config(text=f"Accuracy: {accuracy:.2f}%, Speed: {gross_wpm:.2f} wpm, Net Speed: {net_wpm:.2f} wpm  ",  state="normal")
        self.button.config(state="normal")
        self.entry.config(state="disabled")

root = tk.Tk()
app = TypingSpeedTest(root)
root.mainloop()
