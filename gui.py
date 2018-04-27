import tkinter as tk
from picamera import PiCamera
import time 

ApplicationTheme =  {
    'background':'#B8A3CD',
    'foreground':'#F8F8F2',
}

class Application(tk.Frame):
    def __init_(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.photo_path = '/home/pi/Desktop/PhotoBooth/image.png'

    def create_widgets(self):
        self.shutter = tk.Button(self)
        self.shutter['test'] = 'Take Picture'
        self.shutter['command'] = self.shutter_press()
        self.shutter.pack(side=top)

    def shutter_press()
        camera = PiCamera()

        camera.start_preview()
        time.sleep(5)

        camera.capture(self.photo_path, format="jpg")
        camera.stop_preview()


if __name__ == '__main__':
    root = tk.Tk()
    root.wm_title('Photo Booth')
    root.configure(
        bg=ApplicationTheme['background'], 
        fg=ApplicationTheme['foreground'],
    )
    
    Window(root)
    root.mainloop()
