import tkinter as tk
from picamera import PiCamera
import time 

ApplicationTheme =  {
    "background":"#B8A3CD",
    "foreground":"#F8F8F2",
}
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.config = {
            "photo_path" : "/home/pi/Desktop/PhotoBooth/image.jpg",
        }

    def create_widgets(self):
        self.shutterBtn = tk.Button(self)
        self.shutterBtn["test"] = "Take Picture"
        self.shutterBtn["command"] = self.shutter_press
        self.shutterBtn.pack(side="top")

    def shutter_press(self):
        camera = PiCamera()

        camera.start_preview()
        time.sleep(5)

        camera.capture(self.config["photo_path"], format="jpg")
        camera.stop_preview()


if __name__ == "__main__":
    root = tk.Tk()
    root.wm_title("Photo Booth")
    root.configure(
        bg=ApplicationTheme["background"],
    )
    
    app = Application(master=root)
    root.mainloop()
