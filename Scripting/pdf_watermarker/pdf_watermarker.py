import sys
import PyPDF2

input = sys.argv[1:3] # getting only two arguments

def pdf_watermarker(pdf_list):
    if len(pdf_list) == 0:
        print('Missing arguments...')
    elif len(pdf_list) == 1:
        print('Only one PDF received...')
    else:
        if pdf_list[0][-4:].lower() == '.pdf' and pdf_list[1][-4:].lower() == '.pdf':
            try:
                template = PyPDF2.PdfFileReader(open(f'{pdf_list[0]}', 'rb'))
                watermark = PyPDF2.PdfFileReader(open(f'{pdf_list[1]}', 'rb'))
                output = PyPDF2.PdfFileWriter()

                for x in range(template.getNumPages()):
                    page = template.getPage(x)
                    page.mergePage(watermark.getPage(0))
                    output.addPage(page)
                
                with open('watermarked_pdf.pdf', 'wb') as my_file:
                    output.write(my_file)
                
                print('All done!')
            except FileNotFoundError:
                print('PDF not found...')
        else:
            print('Invalid extension...')

pdf_watermarker(input)
