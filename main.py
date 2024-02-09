from tkinter import *
import tkinter as tk
import win32gui
from PIL import ImageGrab, Image
import numpy as np
from tensorflow.keras.models import load_model
import threading

# Load the trained model
model = load_model('mnist.h5')

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.x = self.y = 0
        self.bind("<Button-1>", self.on_click)

        # Creating elements
        self.canvas = tk.Canvas(self, width=300, height=300, bg="white", cursor="cross")
        self.label = tk.Label(self, text="Thinking..", font=("Helvetica", 48))
        self.classify_btn = tk.Button(self, text="Recognise", command=self.classify_handwriting)
        self.button_clear = tk.Button(self, text="Clear", command=self.clear_all)

        # Grid structure
        self.canvas.grid(row=0, column=0, pady=2, sticky=W)
        self.label.grid(row=0, column=1, pady=2, padx=2)
        self.classify_btn.grid(row=1, column=1, pady=2, padx=2)
        self.button_clear.grid(row=1, column=0, pady=2)

    def on_click(self, event):
        if event.widget == self.classify_btn:
            self.canvas.unbind("<B1-Motion>")
            threading.Thread(target=self.classify_handwriting).start()
            self.canvas.bind("<B1-Motion>", self.draw_lines)

    def clear_all(self):
        self.canvas.delete("all")
        self.label.configure(text="Thinking..")

    def classify_handwriting(self):
        x, y, width, height = self.canvas.winfo_rootx(), self.canvas.winfo_rooty(), self.canvas.winfo_width(), self.canvas.winfo_height()
        rect = (x, y, x + width, y + height)
        im = ImageGrab.grab(rect)
        im = im.resize((28, 28)).convert('L')
        im = np.array(im)
        im = im.reshape(1, 28, 28, 1) / 255.0
        res = model.predict(im)[0]
        digit = np.argmax(res)
        self.label.configure(text=str(digit))

    def draw_lines(self, event):
        self.x = event.x
        self.y = event.y
        r = 8
        self.canvas.create_oval(self.x - r, self.y - r, self.x + r, self.y + r, fill='black')

if __name__ == "__main__":
    app = App()
    app.mainloop()