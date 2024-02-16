import tkinter as tk
from tkinter import colorchooser, messagebox, simpledialog

class PixelArtCreator:
    def __init__(self, master):
        self.master = master
        self.pixel_size = 10
        self.colors = []
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        self.pixel_size_label = tk.Label(self.master, text="Ukuran Pixel:")
        self.pixel_size_label.grid(row=0, column=0, padx=5, pady=5)

        self.pixel_size_entry = tk.Entry(self.master)
        self.pixel_size_entry.insert(tk.END, str(self.pixel_size))
        self.pixel_size_entry.grid(row=0, column=1, padx=5, pady=5)

        self.pixel_size_button = tk.Button(self.master, text="Terapkan", command=self.apply_pixel_size)
        self.pixel_size_button.grid(row=0, column=2, padx=5, pady=5)

        self.color_button = tk.Button(self.master, text="Pilih Warna", command=self.choose_color)
        self.color_button.grid(row=2, column=0, padx=5, pady=5)

        self.clear_button = tk.Button(self.master, text="Hapus Semua", command=self.clear_canvas)
        self.clear_button.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

        self.canvas.bind("<B1-Motion>", self.paint)

        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)
        
        canvas_menu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Ukuran Kanvas", menu=canvas_menu)
        canvas_menu.add_command(label="300x300", command=lambda: self.set_canvas_size(300, 300))
        canvas_menu.add_command(label="400x400", command=lambda: self.set_canvas_size(400, 400))
        canvas_menu.add_command(label="500x500", command=lambda: self.set_canvas_size(500, 500))
        canvas_menu.add_command(label="Custom", command=self.custom_canvas_size)

    def set_canvas_size(self, width, height):
        self.canvas.config(width=width, height=height)
        self.master.geometry('')  # Reset window size after changing canvas size

    def custom_canvas_size(self):
        custom_width = simpledialog.askinteger("Custom Width", "Masukkan lebar kanvas:")
        custom_height = simpledialog.askinteger("Custom Height", "Masukkan tinggi kanvas:")
        if custom_width and custom_height:
            self.set_canvas_size(custom_width, custom_height)

    def apply_pixel_size(self):
        try:
            new_pixel_size = int(self.pixel_size_entry.get())
            if new_pixel_size <= 0:
                raise ValueError
            self.pixel_size = new_pixel_size
        except ValueError:
            messagebox.showerror("Error", "Ukuran pixel harus berupa bilangan bulat positif.")
        else:
            self.clear_canvas()

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        self.colors.append(color)

    def paint(self, event):
        x = event.x // self.pixel_size
        y = event.y // self.pixel_size
        if x * self.pixel_size < self.canvas.winfo_width() and y * self.pixel_size < self.canvas.winfo_height():
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
