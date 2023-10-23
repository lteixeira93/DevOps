import os


def main():
    root_dir = 'rec_dirs/'
    files = get_files(root_dir)

    print("Found these files:")
    for file in files:
        print(file)
    print('Done')


def get_files(root_dir):
    for file in os.listdir(root_dir):

        full_item = os.path.join(root_dir, file)
        print(full_item)
        if os.path.isfile(full_item):
            yield full_item
        elif os.path.isdir(full_item):
            yield from get_files(full_item)


if __name__ == '__main__':
    main()
