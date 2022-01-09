from PIL import Image
from tkinter import *


class App:
    
    def __init__(self,root):
        self.root = root
        self.frame = Frame(root,bg="#C8001F")
        self.frame.pack(anchor = CENTER)
        self.frame_encode = Frame(root,bg="#C8001F")
        self.frame_encode.pack(anchor = CENTER)
        self.ask_encode_or_decode(self.frame_encode)
        
    def ask_encode_or_decode(self,root):
        self.header = Label(root,text="CRYPTECH",font="comicsansms 25 bold",bg="#C8001F",fg="white")
        self.header.grid(row=0,column=0)
        self.v = StringVar(root,"1")
        self.values = {"Encode":"1","Decode":"2"}
        i = 1
        for (text, value) in self.values.items(): 
            Radiobutton(root, text = text, variable = self.v,value = self.values).grid(row=i,column=0)
            i+=1
        self.button = Button(root,text="Submit",fg="grey",bg="white",command= lambda: self.perform(self.v))

    def perform(self,v):
        if v == "1":
            self.create_GUI_encoder()
        elif v == "2":
            self.decode()

    def create_GUI_encoder(self):
        self.top = Toplevel()
        self.top.title("Encode")
        self.top.configure(bg="#C8001F")
        self.header = Label(top,text="CRYPTECH",font="comicsansms 25 bold",bg="#C8001F",fg="white")
        self.header.gird(row=0,column=0,columnspan=2)
        self.btn_browse_label = Label(top,text="Choose the File",bg="#C8001F",fg="white")
        self.btn_browse_label.grid(row=1,column=0)
        self.btn_browse = Button(top,text="Browse : ",bg="white",fg="grey",command=self.browse_file)
        self.btn_browse.grid(row=1,column=1)
        self.path_label = Label(top,text="Path of File",bg="#C8001F",fg="white")
        self.path_label.grid(row=2,column=0,columnspan=2)
        self.message = Label(top,text="Message : ",bg="#C8001F",fg="white")
        self.message.grid(row=3,column=0)
        self.text_area = Text(top,bg="white",fg="blue",font="comicsansms 12")
        self.text_area.grid(row=3,column=1)
        self.submit_btn = Button(top,text="Submit",bg="white",fg="grey",font ="helvetica 15 bold",command=self.submit)
if __name__ == '__main__' :
    root = Tk()
    root.title("Cryptech Steganography")
    # root.geometry("600x700")
    App(root)
    root.mainloop()
    
    # def genBin(data):

    #         # list of binary digit of the secret message
    #         newd = []

    #         for i in data:
    #             newd.append(format(ord(i), '08b'))
    #         return newd

    # def modPix(pix, data):

    #     datalist = genBin(data)
    #     lendata = len(datalist)
    #     imdata = iter(pix)

    #     for i in range(lendata):

    #         # Extracting 3 pixels at a time
    #         pix = [value for value in imdata.__next__()[:3] +
    #                                 imdata.__next__()[:3] +
    #                                 imdata.__next__()[:3]]

    #         # Pixel value should be made odd for 1 and even for 0
    #         for j in range(0, 8):
    #             if (datalist[i][j] == '0' and pix[j]% 2 != 0):
    #                 pix[j] -= 1

    #             elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
    #                 if(pix[j] != 0):
    #                     pix[j] -= 1
    #                 else:
    #                     pix[j] += 1
                    

    #         # Eighth pixel of every set tells
    #         # whether to stop ot read further.
    #         # 0 means keep reading; 1 means thec
    #         # message is over.
    #         if (i == lendata - 1):
    #             if (pix[-1] % 2 == 0):
    #                 if(pix[-1] != 0):
    #                     pix[-1] -= 1
    #                 else:
    #                     pix[-1] += 1

    #         else:
    #             if (pix[-1] % 2 != 0):
    #                 pix[-1] -= 1

    #         pix = tuple(pix)
    #         yield pix[0:3]
    #         yield pix[3:6]
    #         yield pix[6:9]

    # def encode_new(newimg, data):
    #     w = newimg.size[0]
    #     (x, y) = (0, 0)

    #     for pixel in modPix(newimg.getdata(), data):

    #         # processed pixels in the new image
    #         newimg.putpixel((x, y), pixel)
    #         if (x == w - 1):
    #             x = 0
    #             y += 1
    #         else:
    #             x += 1

    # # Encode data into image
    # def encode():
    #     img = input("Enter image name(with extension) : ")
    #     image = Image.open(img, 'r')

    #     data = input("Enter data to be encoded : ")
    #     if (len(data) == 0):
    #         raise ValueError('Data is empty')

    #     newimg = image.copy()
    #     encode_new(newimg, data)

    #     new_img_name = input("Enter the name of new image(with extension) : ")
    #     newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))

    # # Decode the data in the image
    # def decode():
    #     img = input("Enter image name(with extension) : ")
    #     image = Image.open(img, 'r')

    #     data = ''
    #     imgdata = iter(image.getdata())

    #     while (True):
    #         pixels = [value for value in imgdata.__next__()[:3] +
    #                                 imgdata.__next__()[:3] +
    #                                 imgdata.__next__()[:3]]

    #         # string of binary data
    #         binstr = ''

    #         for i in pixels[:8]:
    #             if (i % 2 == 0):
    #                 binstr += '0'
    #             else:
    #                 binstr += '1'

    #         data += chr(int(binstr, 2))
    #         if (pixels[-1] % 2 != 0):
    #             return data
    # def main():
    #     a = int(input("Welcome to Cryptech ::\n"
    #                         "1. Encode\n2. Decode\n"))
    #     if (a == 1):
    #         self.encode()

    #     elif (a == 2):
    #         print("Decoded Word :  " + self.decode())
    #     else:
    #         raise Exception("Enter correct input")


