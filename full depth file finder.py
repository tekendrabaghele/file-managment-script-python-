import os
import shutil
dict_extensions = {
    'audio_extensions' : ('.mp3', '.m4a', '.wav', '.flac'),
    'video_extensions' : ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg'),
    'document_extensions' : ('.doc', '.pdf', '.txt'),
    'image_extension' : ('.jpg','.jpeg','.png','.bmp')
}
while True:
    folderpath = input('enter folder path : ')
    if not list(os.walk(folderpath)):
        print('invalid path...\n')
    else:
        break

def Defth_find(folder_paths,extensions_list):
    data = []
    for file in os.listdir(folder_paths):
        for extension in extensions_list:
            if file.endswith(extension):
                data.append(file)
    return data

for extension_type,extension_tuple in dict_extensions.items():
    folder_name = extension_type.split('_')[0] + 'Files'
    folder_path = os.path.join(folderpath,folder_name)
    for current_path,folders,files in os.walk(folderpath):
        for item in Defth_find(current_path,extension_tuple):
            item_path = os.path.join(current_path, item)
            item_new_path = os.path.join(folder_path, item)
            if os.path.exists(folder_path):
                shutil.move(item_path, item_new_path)
            else:
                os.mkdir(folder_path)
                shutil.move(item_path, item_new_path)
print(f'Script Complete........\n I Hope Your Files Managed (please check your files in path: {folderpath}) \n\t\tThank you ')

# Tekendra Baghele