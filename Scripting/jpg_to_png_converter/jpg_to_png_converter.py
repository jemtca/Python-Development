import sys, os
from PIL import Image

input = sys.argv[1:3] # getting only two arguments

def jpg_to_png(folders):
    if len(folders) == 0 or len(folders) == 1:
        print('Missing argument...\nType something like: python3 JPGtoPNGconverter.py input_folder/ output_folder/')
    else:
        input_folder = folders[0]
        output_folder = folders[1]

        if folders[0][-1] == '/' and folders[1][-1] == '/': # it checks argvs end with /
            if os.path.exists(input_folder):
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)

                for filename in os.listdir(input_folder):
                    img = Image.open(f'{input_folder}{filename}')
                    clean_name = os.path.splitext(filename) # tuple with two elements: name and extension
                    img.save(f'{output_folder}{clean_name[0]}.png', 'png')
                    
                print('All done!')
            else:
                print(f'Input folder \'{input_folder}\' doesn\'t exist.')
        else:
            print(f'Missing \'/\' after a path argument\nInput folder: {input_folder}\nOutput folder: {output_folder}')

jpg_to_png(input)
