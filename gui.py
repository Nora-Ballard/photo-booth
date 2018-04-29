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
            "photo_path" : "/home/pi/Desktop/PhotoBooth/image.jpeg",
        }

    def create_widgets(self):
        self.shutterBtn = tk.Button(self)
        self.shutterBtn["text"] = "Take Picture"
        self.shutterBtn["command"] = self.shutter_press(5)
        self.shutterBtn.pack(side="top")

    def shutter_press(countdown=0):
        try:
            self.camera = PiCamera()
            self.camera.start_preview()
            if countdown > 0:
                start_countdown(countdown)

            self.camera.capture(self.config["photo_path"], format="jpeg")
            self.camera.stop_preview()
            pass
        finally:
            self.camera.close()
            pass

    def start_countdown(seconds):
        overlay_text = tk.Text()
        countdown_overlay = self.camera.add_overlay(overlay_text)
        countdown_overlay.layer = 1
        
        for s in reversed(range(1,seconds)):
            overlay_text.delete(1.0, END)
            overlay_text.insert(str(s)
            time.sleep(1 - time.time() % 1) # sleep until a whole second boundary



if __name__ == "__main__":
    root = tk.Tk()
    root.wm_title("Photo Booth")
    root.attributes("-fullscreen", True)
    root.configure(
        bg=ApplicationTheme["background"],
    )
    
    app = Application(master=root)
    root.mainloop()
