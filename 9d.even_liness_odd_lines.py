def split_lines_into_files():
    filename = 'assignment.txt'
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        with open('File1.txt', 'w') as file1, open('File2.txt', 'w') as file2:
            for i, line in enumerate(lines):
                if i % 2 == 0:
                    file2.write(line)
                else:
                    file1.write(line)

        print("Even lines written to 'File1.txt' and odd lines written to 'File2.txt'.")

    except FileNotFoundError:
        print("File not found. Please check the filename.")