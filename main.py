import os.path

# The root folder
folder = '/Users/calinvladth/Desktop/Testing'


def search_in_folder(rootdir):
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.startswith('.'):
                # print('FILE: ', file)
                print('TO DELETE FILE: ', os.path.join(subdir, file))
                # This removes the specified files
                # os.remove(os.path.join(subdir, file))


def main():
    search_in_folder(folder)


if __name__ == '__main__':
    main()
