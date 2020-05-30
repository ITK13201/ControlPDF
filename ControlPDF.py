import PyPDF2, os

def main():
    while True:
        print('Combine or Split [c/s]: ', end='')
        cmd = input().lower()
        if cmd == 'c' or cmd == 's':
            break
        else:
            print('No such command. Input again.')
    

    '''PDFファイルの結合'''
    if cmd == 'c':
        pdf_files = []
        
        while True:
            try:
                print('How many pdfs?: ', end='')
                num = int(input())
            except ValueError as err:
                print('invalid literal for int(). Input again.')
            else:
                break
        
        for i in range(num):
            while True:
                print('pdf[{}]: '.format(i+1), end='')
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
                    print('No such file. Input again.')

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
        print('created_filename: ', end='')
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

        print('Completed!')
    
    

if __name__ == "__main__":
    main()


