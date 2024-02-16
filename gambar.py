import tkinter as tk
from tkinter import colorchooser

class PixelArtCreator:
    def __init__(self, master, width=10, height=10, pixel_size=30):
        self.master = master
        self.width = width
        self.height = height
        self.pixel_size = pixel_size
        self.colors = []
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=self.width*self.pixel_size, height=self.height*self.pixel_size, bg="white")
        self.canvas.pack()

        self.color_button = tk.Button(self.master, text="Pilih Warna", command=self.choose_color)
        self.color_button.pack()

        self.clear_button = tk.Button(self.master, text="Hapus Semua", command=self.clear_canvas)
        self.clear_button.pack()

        self.canvas.bind("<B1-Motion>", self.paint)

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        self.colors.append(color)

    def paint(self, event):
        x = event.x // self.pixel_size
        y = event.y // self.pixel_size
        if x < self.width and y < self.height:
            color = self.colors[-1] if self.colors else "black"
            self.canvas.create_rectangle(x*self.pixel_size, y*self.pixel_size, (x+1)*self.pixel_size, (y+1)*self.pixel_size, fill=color, outline="")

    def clear_canvas(self):
        self.canvas.delete("all")

def main():
    root = tk.Tk()
    root.title("Pixel Art Creator")
    app = PixelArtCreator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
