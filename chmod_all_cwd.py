#!/usr/local/bin/python

# chmod all MP3 files in the current directory to 0644

from os import chmod, getcwd, listdir

def main():
    for file in listdir(getcwd()):
        if '.mp3' in file:
            print("chmod 0644 %s" % file)
            chmod(file, 0644)

if __name__ == '__main__':
    main()