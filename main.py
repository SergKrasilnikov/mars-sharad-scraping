import wget, os, shutil

try:
    os.mkdir('results')
except:
    print(f'Folder "results" already exist.')

with open('search_file.txt', 'r') as file:
    rgram = 'https://pds-geosciences.wustl.edu/mro/mro-m-sharad-5-radargram-v1/mrosh_2001/data/rgram/'
    geom =  'https://pds-geosciences.wustl.edu/mro/mro-m-sharad-5-radargram-v1/mrosh_2001/data/geom/'

    for line in file:
        if f'{line}_rgram.img' not in os.listdir('./results'):
            wget.download(f'{rgram}{line[:6]}xx/{line}_rgram.img', f'{line}_rgram.img')
            shutil.move(os.path.abspath(os.path.join('.', f'{line}_rgram.img')),
                        os.path.abspath(os.path.join('./results', f'{line}_rgram.img')))
            wget.download(f'{rgram}{line[:6]}xx/{line}_rgram.lbl', f'{line}_rgram.lbl')
            shutil.move(os.path.abspath(os.path.join('.', f'{line}_rgram.lbl')),
                        os.path.abspath(os.path.join('./results', f'{line}_rgram.lbl')))
            wget.download(f'{geom}{line[:6]}xx/{line}_geom.tab', f'{line}_geom.tab')
            shutil.move(os.path.abspath(os.path.join('.', f'{line}_geom.tab')),
                        os.path.abspath(os.path.join('./results', f'{line}_geom.tab')))
            wget.download(f'{geom}{line[:6]}xx/{line}_geom.lbl', f'{line}_geom.lbl')
            shutil.move(os.path.abspath(os.path.join('.', f'{line}_geom.lbl')),
                        os.path.abspath(os.path.join('./results', f'{line}_geom.lbl')))
        else:
            print(f'File {line[:10]} already downloaded.')

print('All files downloaded.')