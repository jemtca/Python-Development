import sys
import PyPDF2

input = sys.argv[1:]

def pdf_combiner(pdf_list):
    if len(pdf_list) == 0:
        print('Missing arguments...')
    elif len(pdf_list) == 1:
        print('Only one PDF received...')
    else:
        extension_ok = True

        for pdf in pdf_list:
            if pdf[-4:].lower() != '.pdf':
                extension_ok = False
                break
        
        if extension_ok:
            merger = PyPDF2.PdfFileMerger()

            try:
                for pdf in pdf_list:
                    merger.append(pdf)

                merger.write('merged_pdf.pdf')
                
                print('All done!')
            except FileNotFoundError:
                print('PDF not found...')
        else:
            print('Invalid extension...')

pdf_combiner(input)
