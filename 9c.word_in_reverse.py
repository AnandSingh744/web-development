def reverse_words_in_file():
    filename = 'assignment.txt'
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        print("Words in reverse order:")
        for line in lines:
            words = line.split()
            print(" ".join(reversed(words)))

    except FileNotFoundError:
        print("File not found. Please check the filename.")