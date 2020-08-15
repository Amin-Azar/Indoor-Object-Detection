import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time

class App:
    def __init__(self, window, window_title, image_path="background.jpg"):
        self.window = window
        self.window.title(window_title)

        # Load an image using OpenCV
        self.cv_img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)

        # Get the image dimensions (OpenCV stores image data as NumPy ndarray)
        self.height, self.width, no_channels = self.cv_img.shape

        # Create a canvas that can fit the above image
        self.canvas = tkinter.Canvas(window, width = self.width, height = self.height)
        self.canvas.pack()

        # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))

        # Add a PhotoImage to the Canvas
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

        # Button that lets the user blur the image
        self.btn_blur=tkinter.Button(window, text="Blur", width=50, command=self.blur_image)
        self.btn_blur.pack(anchor=tkinter.CENTER, expand=True)

        self.window.mainloop()

    # Callback for the "Blur" button
    def blur_image(self):
        self.cv_img = cv2.blur(self.cv_img, (3, 3))
        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

    def close(self):
        self.window.destroy()

# Create a window and pass it to the Application object
A=App(tkinter.Tk(), "Tkinter and OpenCV", "images/B00000000.jpg")

time.sleep(5)

APP.close()


