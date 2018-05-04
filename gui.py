import tkinter as tk
from PIL import Image,ImageTk
from picamera import PiCamera
import time
import io

ApplicationTheme =  {
    "background":"#B8A3CD",
    "foreground":"#F8F8F2",
}
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill="both")
        self.create_widgets()
        self.config = {
            "photo_path" : "/tmp/image.jpeg",
            "countdown_seconds" : 4,
        }

    def create_widgets(self):
        self.shutter_btn = tk.Button(self)
        self.shutter_btn["text"] = "Start Countdown"
        self.shutter_btn["command"] = lambda: self.shutter_press(self.config["countdown_seconds"])
        self.shutter_btn.pack(side="bottom",anchor="e",padx=10,pady=10)

        self.preview_canvas = tk.Canvas(self, bg=ApplicationTheme["background"])
        self.preview_canvas.width = 480/2
        self.preview_canvas.height = 640/2
        self.preview_canvas.pack(anchor="w",padx=10,pady=10)

    def shutter_press(self,countdown=0):
        with PiCamera() as camera:
            camera.start_preview()
            # if countdown > 0:
            #     self.start_countdown(camera=camera,seconds=countdown)

            self.capture_stream = self.capture_ToStream(camera=camera)
            self.show_preview()

            camera.stop_preview()
            pass

    def capture_ToStream(self,camera):
        stream = io.BytesIO()
        camera.capture(stream, format="jpeg")
        stream.seek(0)

        return stream

    def show_preview(self):
        image = Image.open(self.capture_stream)

        self.preview_photoimage = ImageTk.PhotoImage(image)
        self.preview_canvas.create_image(20,20,image=self.preview_photoimage)

    def start_countdown(self,camera,seconds=0):
        for s in reversed(range(1,seconds)):
            camera.annotate_text_size = 64
            camera.annotate_text = str(s)
            time.sleep(1 - time.time() % 1) # sleep until a whole second boundary
        camera.annotate_text = " "



if __name__ == "__main__":
    root = tk.Tk()
    root.wm_title("Photo Booth")
    # root.attributes("-fullscreen", True)
    root.attributes("-zoomed", True)
    root.configure(
        bg=ApplicationTheme["background"],
    )
    
    app = Application(master=root)
    app.configure(bg=ApplicationTheme["background"])
    root.mainloop()
