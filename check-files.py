import os


def check_files():
    filename = input("Enter a file name: ")
    if os.path.exists(filename):
        with open(filename, 'r') as lines_file:
            lines = lines_file.read().splitlines()
        for line in lines:
            if os.path.exists(line):
                print(f"File {[line]} exists!")
            else:
                print(f"File {[line]} does not exist!")
    else:
        print(f"Usage: Filename [{filename}] does not exist")


if __name__ == "__main__":
    check_files()
