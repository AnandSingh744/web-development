# a. Count characters, words, and lines
def count_file_contents():
    filename = 'assignment.txt'
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        total_characters = sum(len(line) for line in lines)
        total_words = sum(len(line.split()) for line in lines)
        total_lines = len(lines)

        print("Total Characters:", total_characters)
        print("Total Words:", total_words)
        print("Total Lines:", total_lines)

    except FileNotFoundError:
        print("File not found. Please check the filename.")
