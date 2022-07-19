import os
import shutil

print('WellCome to File Management tool \n ')
dict_extensions = {
    'audio_extensions' : ('.mp3', '.m4a', '.wav', '.flac','mkv','.ogg','.MP3', '.WAV', '.M4A', '.FLAC' , '.AAC'),
    'video_extensions' : ('.mp4', '.mkv', '.MKV', '.flv','.webm','.mpg','.mp2','.mpeg','.mpe','.mpv', '.m4v','.avi','.wmv','.mov','.qt', '.swf','.avchd''.WEBM','.MPG','.MP2','.MPEG','.MPE','.MPV','.M4P', '.M4V','.AVI','.WMV','.MOV','.QT','.FLV', '.SWF'
,'.AVCHD'),
    'document_extensions' : ('.doc', '.pdf', '.txt','.odt','.DOC', '.PDF', '.TXT','.ODT','.pptx','.docx'),
    'image_extension' : ('.jpg','.jpeg','.png','.bmp','.JPG'),
    'compressed_extension' : ('.zip','.rar', '.ZIP','.RAR'),
    'exe_extension' : ('.exe', '.apk')
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
print('Your files moved successfully .....')
User_Want = input(f'\nDo You want to delete all Empty Folders in / {folderpath}  (y/n) ?:  ')
if User_Want == 'y'or User_Want == 'Y':
    path_abs = folderpath
    walk = list(os.walk(path_abs))
    for path, _, _ in walk[::-1]:
        if len(os.listdir(path)) == 0:
            os.rmdir(path)
            print('All process completed ...')
else:
    print('Empty Folders Not Removed')