#!/usr/bin/env python
# coding: utf-8

import PyPDF2, os

def main():
    while True:
        print('# Combine or Split [c/s]: ', end='')
        cmd = input().lower()
        if cmd == 'c' or cmd == 's':
            break
        else:
            print('Error: No such command. Input again.')

    '''PDFファイルの結合'''
    if cmd == 'c':
        pdf_files = []
        
        while True:
            try:
                print('# How many pdfs?: ', end='')
                num = int(input())
            except ValueError as err:
                print('Error: invalid literal for int(). Input again.')
            else:
                break
        
        print('### Input filename. ###')
        for i in range(num):
            while True:
                print('# pdf[{}]: '.format(i+1), end='')
                filename = input()
                # 拡張子の追加
                if filename.endswith('.pdf'):
                    pass
                else:
                    filename += '.pdf'
                # 存在の確認
                if os.path.exists(filename):
                    break
                else:
                    print('Error: No such file. Input again.')

            pdf_files.append(filename)
        
        # ファイルの書き込み
        pdf_writer = PyPDF2.PdfFileWriter()
        # 全てのpdfファイルをループする
        for filename in pdf_files:
            pdf_file_obj = open(filename, 'rb')
            pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
            # 全てのページをループする
            for page_num in range(pdf_reader.numPages):
                page_obj = pdf_reader.getPage(page_num)
                pdf_writer.addPage(page_obj)
        
        # 作成するpdfの名前
        print('# created_filename: ', end='')
        created_filename = input()
        # 拡張子の確認
        if created_filename.endswith('.pdf'):
            pass
        else:
            created_filename += '.pdf'

        # 結合したPDFをファイルに保存する．
        pdf_output_file = open(created_filename, 'wb')
        pdf_writer.write(pdf_output_file)
        pdf_output_file.close()

        print('### Completed! ###')
    
    '''PDFファイルの分割'''
    if cmd == 's':
        # 元ファイル名の入力
        while True:
            print('# Input filename: ', end='')
            filename = input()
            # 拡張子の追加
            if filename.endswith('.pdf'):
                pass
            else:
                filename += '.pdf'
            # 存在の確認
            if os.path.exists(filename):
                break
            else:
                print('Error: No such file. Input again.')
        
        pdf_file_obj = open(filename, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
        
        # 最初のページ数と最後のページ数
        print('### Input first and last page number to be splited. ###')
        while True:
            try:
                print('# first number: ', end='')
                first_num = int(input()) - 1
                print('# last number: ', end='')
                last_num = int(input()) - 1
            except ValueError as err:
                print('Error: invalid literal for int(). Input again.')
            else:
                if first_num > pdf_reader.numPages - 1 or last_num > pdf_reader.numPages - 1 or first_num > last_num:
                    print('Error: Incorrect number! Input again.')
                else:
                    break
        
         # ファイルの書き込み
        pdf_writer = PyPDF2.PdfFileWriter()
        # 全てのpdfファイルをループする
        pdf_file_obj = open(filename, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
        # first_numからlast_numのページをループする
        for page_num in range(first_num, last_num + 1):
            page_obj = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page_obj)
        
        # 作成するpdfの名前
        print('# created_filename: ', end='')
        created_filename = input()
        # 拡張子の確認
        if created_filename.endswith('.pdf'):
            pass
        else:
            created_filename += '.pdf'

        # 結合したPDFをファイルに保存する．
        pdf_output_file = open(created_filename, 'wb')
        pdf_writer.write(pdf_output_file)
        pdf_output_file.close()

        print('### Completed! ###')

if __name__ == "__main__":
    main()
