# -*- coding: utf-8 -*-
"""
Created on ：2018/04/03
@author: Freeman
"""
from tkinter import *
import tkinter.filedialog
from PdfMake import PDFMake


def getPdfFileName():
    filename = tkinter.filedialog.askopenfilename()
    pdfFileName.set(filename)
    if filename != '':
        lb1.config(text="拆分文件：" + filename)
    else:
        lb1.config(text="您没有选择任何文件")

def getPdfFileNames():
    filenames = tkinter.filedialog.askopenfilenames()
    if len(filenames) != 0:
        string_filename = ""
        for i in range(0, len(filenames)):
            string_filename += str(filenames[i]) + "\n"
        pdfFileNames.set(string_filename)
        llb1.config(text="合并文件：\n" + string_filename)
    else:
        pdfFileNames.set('')
        llb1.config(text="您没有选择任何文件")


def selectPath():
    path = tkinter.filedialog.askdirectory()
    outputdirectory.set(path)
    if path != '':
        lb2.config(text="输出路径：" + path)
    else:
        lb2.config(text="您没有选择任何路径")


def selectPaths():
    path = tkinter.filedialog.askdirectory()
    outputdirectory.set(path)
    if path != '':
        llb2.config(text="输出路径：" + path)
    else:
        llb2.config(text="您没有选择任何路径")


def splitPdf():
    if outputdirectory.get() != '' and pdfFileName.get() != '':
        master = PDFMake(outputdirectory=outputdirectory.get())
        if pageList.get() == '':
            master.spilt_pdf(pdfFileName.get())
            lb3.config(text="拆分成功！")
        else:
            try:
                master.spilt_pdf(pdfFileName.get(), pageList.get())
                lb3.config(text="拆分成功！")
            except ValueError:
                lb3.config(text="拆分失败:ValueError！")
    else:
        lb3.config(text="拆分失败:选择文件或者目录有误！")


def mergePdf():
    if outputdirectory.get() != '' and pdfFileNames.get() != '':
        master = PDFMake(outputdirectory=outputdirectory.get())
        master.merge_pdf(pdfFileNames.get().split('\n')[:-1])
        llb3.config(text="合并成功！")
    else:
        llb3.config(text="合并失败:选择文件或者目录有误！")


if __name__ == '__main__':

    root = tkinter.Tk()
    root.geometry('700x550+300+50')

    outputdirectory = StringVar()
    pdfFileName = StringVar()
    pdfFileNames = StringVar()
    pageList = StringVar()

    root.title('PDF Master           Copyright © 2018 by Freeman')
    root['bg'] = '#a9ed96'
    root.attributes("-alpha",0.97)

    lb0 = Label(root, text='拆分PDF模块', width=20, font = 'Helvetica -20 bold',bg='#a9ed96')
    lb0.grid(row=0, columnspan=2,stick=W,pady=10,)

    btn1 = Button(root, text="选择需要拆分的PDF", width=20, command=getPdfFileName)
    btn1.grid(row=1, column=0, stick=W, pady=10, padx=50)

    lb1 = Label(root, text='', width=50)
    lb1.grid(row=1, column=1)

    btn2 = Button(root, text="选择拆分后的存储路径", width=20, command=selectPath)
    btn2.grid(row=2, column=0, stick=W, pady=10,padx=50)

    lb2 = Label(root, text='', width=50)
    lb2.grid(row=2, column=1)

    lbe = Label(root, text='请输入要拆分出来的页码', width=20)
    lbe.grid(row=3, column=0, stick=W,pady=10,padx=50)

    en1 = Entry(root, textvariable=pageList, width=50,)
    pageList.set('例如:1-2,7-10表示将1-2和7-10拆出来并合并，不填则单页拆分')
    en1.grid(row=3, column=1, pady=10, padx=40)

    btn3 = Button(root, text="拆 分 ", width=20,  bg='SkyBlue',command=splitPdf)
    btn3.grid(row=4, column=0, stick=W,  pady=10, padx=50)

    lb3 = Label(root, text='', width=50)
    lb3.grid(row=4, column=1)

    w = Canvas(
        root,
        width=700,
        height=8,
            background="SlateGray"
    ).grid(row=5, pady=10, columnspan=2)

    llb0 = Label(root, text='合并PDF模块', width=20, font = 'Helvetica -20 bold',bg='#a9ed96')
    llb0.grid(row=6, columnspan=2,stick=W,pady=10,)

    bbtn1 = Button(root, text="选择需要合并的PDF", width=20, command=getPdfFileNames)
    bbtn1.grid(row=7, column=0, stick=W, pady=10, padx=50)

    llb1 = Label(root, text='', width=50, height=5)
    llb1.grid(row=7, column=1)

    bbtn2 = Button(root, text="选择合并后的存储路径", width=20, command=selectPaths)
    bbtn2.grid(row=8, column=0, stick=W, pady=10,padx=50)

    llb2 = Label(root, text='', width=50)
    llb2.grid(row=8, column=1)

    bbtn3 = Button(root, text="合 并", width=20, bg='SkyBlue',command=mergePdf)
    bbtn3.grid(row=9, column=0, stick=W,  pady=10, padx=50)

    llb3 = Label(root, text='', width=50)
    llb3.grid(row=9, column=1)


    root.mainloop()
