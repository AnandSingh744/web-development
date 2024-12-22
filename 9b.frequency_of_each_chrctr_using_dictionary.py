def calculate_character_frequency():
    filename = 'assignment.txt'
    try:
        with open(filename, 'r') as file:
            content = file.read()

        char_frequency = {}
        for char in content:
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1

        print("Character Frequencies:")
        for char, freq in char_frequency.items():
            print(f"'{char}': {freq}")

    except FileNotFoundError:
        print("File not found. Please check the filename.")