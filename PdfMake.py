# -*- coding: utf-8 -*-
"""
Created on ：2018/04/03
@author: Freeman
"""

from PyPDF2 import PdfFileReader, PdfFileWriter

__all__ = ['PDFMake']


class PDFMake(object):
    def __init__(self, outputdirectory=''):
        self.outputdirectory = outputdirectory

    def __check_page_list(self):
        # 检测是否为string类型
        if type(self.listmode) != type('0-6,8-9'):
            return True
        else:
            # 检测是否含有非法字符
            for i in range(1, len(self.listmode) - 1):
                if self.listmode[i] not in \
                        ['-', ',', '\'', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    return True
        return False

    def spilt_pdf(self,  inputfilename=None, listmode=None):
        self.listmode = listmode
        # 读取PDF文件
        pdfFile = PdfFileReader(open(inputfilename, "rb"))
        pageCount = pdfFile.getNumPages()

        if self.listmode == None:
            for i in range(pageCount):
                pdfWriter = PdfFileWriter()
                page = pdfFile.getPage(i)
                pdfWriter.addPage(page)
                pdfWriterNmae = self.outputdirectory +'/page{}'.format(i+1) + '.pdf'
                pdfWriter.write(open(pdfWriterNmae, 'wb'))

        else:
            if self.__check_page_list():
                raise ValueError
            else:
                pdfWriter = PdfFileWriter()
                part = self.listmode.split(',')
                for k in part:
                    start = int(k.split('-')[0])
                    end = int(k.split('-')[1])
                    for m in range(start - 1, end):
                        page = pdfFile.getPage(m)
                        pdfWriter.addPage(page)
                pdfWriterNmae = self.outputdirectory + '/part ' + self.listmode + '.pdf'
                pdfWriter.write(open(pdfWriterNmae, 'wb'))

    def merge_pdf(self, flienamelist=None):
        print(flienamelist)
        pdfWriter = PdfFileWriter()
        for i in flienamelist:
            pdfFile = PdfFileReader(open(i, "rb"))
            pdfWriter.appendPagesFromReader(pdfFile)
        pdfWriterNmae = self.outputdirectory + '/mergeByMaster.pdf'
        pdfWriter.write(open(pdfWriterNmae, 'wb'))