import os

def main():   
    print(os.getcwd())
    print(os.listdir('../'))
    
    for folder, sub_folder, files in os.walk('../'):
        print("Folder: {}, SubFolders: {}, Files: {}".format(folder, sub_folder, files))

# end def

if __name__ == "__main__":
    main()
    