## File Checks

In this exercise, you'll practice working with files and directories. You'll write a program to test whether or not some files exist.

Write a program in `check-files.py` that
* takes a filename as input
* reads that file
* assuming each line is a filename, print out whether or not the corresponding file exists

## Flow & Task 
Implement a function called `check_files` that performs the following actions:
- Asks the user to provide a file that has a list of files
- Check each file of these, and show a statement if it exists or not

## Input Validation
Your program should not crash if the user enters a wron file name or an empty value - A usage statement should be shown accordingly.

## Starter Code
Check the file called `check_files.py`.

## Examples
Here are some example runs:

### Example 1
Input:
```text
./README.md
images/
```

Output:
```text
Enter a file name: assets/testing_files/test_1.txt
File ['./README.md'] exists!
File ['images/'] does not exist!
```

### Example 2
Input:
```text
README.md
/
wrong_file.txt
```

Output:
```text
Enter a file name: assets/testing_files/test_1.txt
File ['./README.md'] exists!
File ['images/'] does not exist!
```

### Example 3
Input:
```text
wrong_file.txt
```

Output:
```text
Enter a file name: wrong_file.txt
Usage: Filename [wrong_file.txt] does not exist
```