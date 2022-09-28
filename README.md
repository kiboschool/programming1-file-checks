## File Checks

In this exercise, you'll practice working with files and directories. 
You'll write a program to test whether or not some files exist.

Write a program in `check-files.py` that

* takes a filename as input
* reads that file
* assuming each line is a filename, print out whether or not the corresponding file exists

## Steps

Implement a function called `check_files` that performs the following actions:
- Asks the user to provide the path to a file
- Reads that file
- For each line of the file, prints either: 
    - File [name of file] exists! 
    - File [name of file] does not exist! 

When the program is run as the main module, call your function.

## Input Validation

Your program should not crash if the user enters a file that doesn't exist, 
or an empty value. Instead, it should print a message describing how to use the
program.

## Expected Results

### Example 1

test_1.txt:
```text
./README.md
images/
```

Output:
```text
Enter a file name: test_1.txt
File ['./README.md'] exists!
File ['images/'] does not exist!
```

### Example 2

test_2.txt:
```text
README.md
/
wrong_file.txt
```

Output:
```text
Enter a file name: test_2.txt
File ['./README.md'] exists!
File ['/'] exists!
File ['images/'] does not exist!
```

### Example 3

With a file that doesn't exist.

Output:
```text
Enter a file name: wrong_file.txt
Usage: File 'wrong_file.txt' does not exist
```

## Testing

There are no unit tests for this exercise. Run your program with sample
inputs and check that the output matches the expected output.
