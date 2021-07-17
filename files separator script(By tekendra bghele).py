import os
import shutil
dict_extensions = {
    'Audio_extension': ('.mp3', '.wav', '.m4a', '.flac'),
    'Video_extension': ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg'),
    'Document_extension': ('.doc', '.pdf', '.txt'),
    'Image_extension': ('.jpg', '.jpeg', '.png', '.bmp')
}
while True:
    FolderPath = input('Enter Folder Path :  ')

    def file_finder(folder_path, file_extension):
        files = []
        for file in os.listdir(folder_path):
            for extension in file_extension:
                if file.endswith(extension):
                    files.append(file)
        return files
    try:
        for extension_type, extension_tuple in dict_extensions.items():
            folder_name = extension_type.split('_')[0] + 'Files'

            Folder_path = os.path.join(FolderPath, folder_name)
            for item in (file_finder(FolderPath, extension_tuple)):
                if not item:
                    pass
                else:
                    item_path = os.path.join(FolderPath, item)
                    item_new_path = os.path.join(Folder_path, item)
                    if os.path.exists(Folder_path):
                        shutil.move(item_path, item_new_path)
                    else:
                        os.mkdir(Folder_path)
                        shutil.move(item_path, item_new_path)
        print(f'Script Complete........\n I Hope Your Files Managed (please check your files in path: {FolderPath}) \n\t\tThank you ')
        break
    except FileNotFoundError:
        print('Please Input Valid Path.......\n')

# Tekendra Baghele
