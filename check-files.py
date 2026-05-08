import os

def check_files():
    filename = input("Enter a file name: ")

    # Check if input file exists
    if not os.path.exists(filename):
        print(f"Usage: File '{filename}' does not exist")
        return

    # Read file
    with open(filename, "r") as f:
        lines = f.readlines()

    # Check each line
    for line in lines:
        file_to_check = line.strip()

        if os.path.exists(file_to_check):
            print(f"File '{file_to_check}' exists!")
        else:
            print(f"File '{file_to_check}' does not exist!")

if __name__ == "__main__":
    check_files()