import PyPDF2, os

def main():
    print('Combine or Split [c/s]: ', end='')
    cmd = input().lower()

    '''PDFファイルの結合'''
    if cmd == 'c':
        pdf_files = []
        print('How many pdfs?: ', end='')
        num = int(input())
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
        
        # 作成するpdfの名前
        print('created_filename: ', end='')
        created_filename = input()
        # 拡張子の確認
        if created_filename.endswith('.pdf'):
            pass
        else:
            created_filename += '.pdf'

        pdf_writer = PyPDF2.PdfFileWriter()
        # 全てのpdfファイルをループする
        for filename in pdf_files:
            pdf_file_obj = open(created_filename, 'wb')
            pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
        
        

if __name__ == "__main__":
    main()


