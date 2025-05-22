from tkinter import *

def loadImage(fname):
    global inImage, XSIZE, YSIZE
    fp = open(fname, 'rb')
    
    for i in range(0, XSIZE):
        tmpList = []
        for k in range(0, YSIZE):
            data = int(ord(fp.read(1))) 
            tmpList.append(data)
        inImage.append(tmpList)
        
    fp.close()
    
def displayImage(image):
    global XSIZE, YSIZE
    rgbString=""
    for i in range(0, XSIZE):
        tmpString = ""
        for k in range(0, YSIZE):
            data = image[i][k]
            tmpString += "#%02x%02x%02x " % (data, data, data)
        rgbString += "{" + tmpString + "}"
    paper.put(rgbString) 
    
#전역변수선언파트

window = None
Canvas = None 
XSIZE, YSIZE = 256, 256 
inImage = []

#메인코드파트 

window = Tk()
window.title("흑백사진")
canvas = Canvas(window, height = XSIZE, width = YSIZE) 
paper = PhotoImage(width=XSIZE, height=YSIZE)
canvas.create_image((XSIZE / 2, YSIZE / 2), image = paper, state = "normal")

filename = 'RAW/tree.raw'
loadImage(filename)

displayImage(inImage)

canvas.pick()
window.mainloop()
    