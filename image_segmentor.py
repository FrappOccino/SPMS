import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageTk
import customtkinter as ctk


class ImagePointDrawer:
    def __init__(self, root):
        self.root = root
        self.canvas = ctk.CTkCanvas(root)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.root.columnconfigure(0, weight=1)  # Set weight of column 0 to 1
        self.root.rowconfigure(0, weight=3)     # Set weight of row 0 to 3

        self.shapes = []
        self.current_shape = []
        self.is_drawing = False
        self.image = None

        self.create_menu()

        self.draw_button = ctk.CTkButton(root, text="Draw Points", command=self.toggle_drawing)
        self.draw_button.grid(row=1, column=0, pady=10)  # Button in row 1, column 0, sticky to all sides

        self.save_button = ctk.CTkButton(root, text="Save", command=self.save_images)
        self.save_button.grid(row=2, column=0, pady=10)  # Button in row 2, column 0, sticky to all sides

        self.canvas.bind("<Button-1>", self.on_canvas_click)

    def create_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open Image", command=self.open_image)
        menubar.add_cascade(label="File", menu=file_menu)
        self.root.configure(menu=menubar)

    def open_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ppm *.pgm *.pbm *.xbm")])
        if file_path:
            self.load_image(file_path)


    def load_image(self, image_path):
        self.image = Image.open(image_path)
        self.ctk_image = ImageTk.PhotoImage(self.image)
        self.canvas.configure(width=self.image.width, height=self.image.height)
        self.canvas.create_image(0, 0, image=self.ctk_image, anchor=tk.NW)

    def toggle_drawing(self):
        if self.is_drawing:
            if self.current_shape:
                self.close_current_shape()
        else:
            self.start_new_shape()

    def start_new_shape(self):
        self.current_shape = []
        self.is_drawing = True
        self.draw_button.configure(text="Stop Drawing")
        self.canvas.configure(cursor="plus")

    def on_canvas_click(self, event):
        if not self.is_drawing:
            return

        x, y = event.x, event.y
        self.current_shape.append((x, y))
        self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="red")

        if len(self.current_shape) > 1:
            self.canvas.create_line(self.current_shape[-2], self.current_shape[-1], fill="blue")

        if len(self.current_shape) > 2:
            if self.is_close_to_start(x, y):
                self.prompt_save_shape()

    def is_close_to_start(self, x, y):
        if self.current_shape:
            start_x, start_y = self.current_shape[0]
            return abs(x - start_x) < 5 and abs(y - start_y) < 5
        return False

    def close_current_shape(self):
        if self.current_shape:
            self.shapes.append(self.current_shape)
            self.current_shape = []
            self.is_drawing = True
            self.draw_button.configure(text="Stop Drawing")
            self.canvas.configure(cursor="plus")

    def prompt_save_shape(self):
        result = messagebox.askyesno("Save Shape?", "Do you want to save and close the shape?")
        if result:
            self.close_current_shape()

    def clear_canvas(self):
        self.canvas.delete("all")
        self.shapes = []
        self.current_shape = []
        self.is_drawing = False
        self.draw_button.configure(text="Draw Points")
        self.canvas.configure(cursor="arrow")

    def save_images(self):
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if not save_path:
            return  # User canceled the file dialog

        self.save_canvas_image(save_path)
        self.save_filled_shape_image(save_path)

    def save_canvas_image(self, save_path):
        if self.image:
            image = self.image.copy()
            draw = ImageDraw.Draw(image)

            for shape in self.shapes:
                draw.polygon(shape, outline="black", fill="white")

            image.save(save_path)

    def save_filled_shape_image(self, save_path):
        if self.image:
            image = Image.new("L", (self.image.width, self.image.height), 0)  # Black background
            draw = ImageDraw.Draw(image)

            for shape in self.shapes:
                draw.polygon(shape, outline="white", fill="white")

            image.save(save_path)



root = ctk.CTk()
root.title('')
app = ImagePointDrawer(root)
root.mainloop()
