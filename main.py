# Programmers: Andrew Leimbach
# Course:  CS151, Zelalem Yalew
# Due Date: 11/21/24
# Lab Assignment: PA 04
# Problem Statement: program to analyze headlines from the Australian Broadcasting Company (ABC)
# Data In: Users choice, then proceeding user input to that step
# Data Out:  Solution to whatever step user chooses
# Credit: Class Assignment
# Input Files: 2014.txt, 2015.txt, 2016.txt, 2017.txt, 2018.txt, 2019.txt

#Purpose: Load headlines from a file into a list
#Parameters: file_name
#Return: A list of strings, or None if not successful
def load_headlines(file_name):
    try:
        with open(file_name, 'r') as file:
            headlines = []
            for line in file:
                headlines.append(line.strip())
            return headlines
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None

#Purpose: Count the number of headlines that contain a specific word
#Parameters: headlines, words
#Return: An integer count
def count_headlines_with_word(headlines, word):
    count = 0
    for headline in headlines:
        if word.lower() in headline.lower():
            count += 1
    return count

#Purpose: Write headlines containing a specific word to a new file
#Parameters: headlines, words, output_file
#Return: None
def write_headlines_with_word(headlines, word, output_file):
    with open(output_file, 'w') as file:
        for headline in headlines:
            if word.lower() in headline.lower():
                file.write(headline + '\n')

#Purpose: Calculate the average number of characters per headline
#Parameters: headlines
#Return: A float representing average, or 0 if headlines is empty
def average_headline_length(headlines):
    total_characters = 0
    for headline in headlines:
        total_characters += len(headline)
    if len(headlines) > 0:
        return total_characters / len(headlines)
    return 0

#Purpose: Find the longest and shortest headlines based on character count
#Parameters: headlines
#Return: A tuple containing the longest and shortest headlines(both strings)
def find_extreme_headlines(headlines):
    if len(headlines) == 0:
        return ("", "")
    longest = headlines[0]
    shortest = headlines[0]
    for headline in headlines:
        if len(headline) > len(longest):
            longest = headline
        if len(headline) < len(shortest):
            shortest = headline
    return longest, shortest

#Purpose: Manage program flow and handle user interaction
#Parameters: None
#Return: None
def main():
    headlines = None
    choice = 0  # Initialize menu choice to enter the loop

    while choice != 6:
        print("\nMenu:")
        print("1. Load a headline file")
        print("2. Count headlines containing a word")
        print("3. Write headlines containing a word to a new file")
        print("4. Calculate average headline length")
        print("5. Find the longest and shortest headlines")
        print("6. Quit")

        try:
            choice = int(input("Choose an option: ").strip())
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            file_name = input("Enter the file name to load: ").strip()
            loaded_headlines = load_headlines(file_name)
            if loaded_headlines is not None and len(loaded_headlines) > 0:
                headlines = loaded_headlines
                print(f"Loaded {len(headlines)} headlines.")
            else:
                print("Failed to load headlines. Check the file and try again.")

        elif choice == 2:
            if headlines is not None and len(headlines) > 0:
                word = input("Enter the word to search for: ").strip()
                count = count_headlines_with_word(headlines, word)
                print(f"{count} headlines contain the word '{word}'.")
            else:
                print("No data loaded. Please load a file first.")

        elif choice == 3:
            if headlines is not None and len(headlines) > 0:
                word = input("Enter the word to search for: ").strip()
                output_file = input("Enter the name of the output file: ").strip()
                write_headlines_with_word(headlines, word, output_file)
                print(f"Headlines containing '{word}' have been written to '{output_file}'.")
            else:
                print("No data loaded. Please load a file first.")

        elif choice == 4:
            if headlines is not None and len(headlines) > 0:
                avg_length = average_headline_length(headlines)
                print(f"The average headline length is {avg_length:.2f} characters.")
            else:
                print("No data loaded. Please load a file first.")

        elif choice == 5:
            if headlines is not None and len(headlines) > 0:
                longest, shortest = find_extreme_headlines(headlines)
                print(f"Longest headline: {longest}")
                print(f"Shortest headline: {shortest}")
            else:
                print("No data loaded. Please load a file first.")

        elif choice == 6:
            print("Goodbye!")

        else:
            print("Invalid option. Please enter a number between 1 and 6.")
main()
