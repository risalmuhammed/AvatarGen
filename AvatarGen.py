__author__ = 'Rizal'

from PIL import Image as Pil_image
from tkinter import *
import hashlib as hl
import time
import datetime


class Avatar:
    im_digest_sha256 = ''

    def __init__(self, master):

        self.label_name = Label(master, text="Name:")
        self.label_res = Label(master, text="AvatarSize(px):")
        self.entry_name = Entry(master, width=15)
        self.entry_size = Entry(master, width=8)
        self.build_btn = Button(master, text="Avatar !", relief=GROOVE, command=self.build_avatar)

        self.label_name.grid(row=0, sticky=W)
        self.entry_name.grid(row=0, column=1, padx=5, sticky=W)
        self.label_res.grid(row=1, sticky=W)
        self.entry_size.grid(row=1, column=1, padx=5, sticky=W)
        self.build_btn.grid(row=2, column=1, padx=5, sticky=W)

    def build_avatar(self):
        global im_digest_sha256
        txt = self.entry_name.get()
        size = self.entry_size.get()
        if len(txt) != 0 and len(size) != 0:
            im_digest_sha256 = hl.sha256(txt.encode()).hexdigest()
            self.create_new_image(int(size))

    @staticmethod
    def giv_color(val):
        val -= 1
        if im_digest_sha256[val].isalpha():
            return ord(im_digest_sha256[val])
        else:
            return int(im_digest_sha256[val])

    def create_new_image(self, size):
        img = Pil_image.new("RGB", (8, 8), (255, 255, 255))
        for x in range(8):
            for y in range(8):
                u = self.giv_color((x + 1) * (y + 1))
                img.putpixel((x, y), (u, 2 * u, int(u / 2)))

        img = img.resize((size, size))
        img.save("avatar-{0}-{1}px.png".format(self.get_timestamp(), size), "PNG")

    @staticmethod
    def get_timestamp():
        return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%Hh_%Mm_%Ss')

if __name__ == "__main__":
    main_window = Tk()
    my = Avatar(main_window)
    main_window.resizable(width=FALSE, height=FALSE)
    main_window.title("AvatarGen")
    main_window.mainloop()



