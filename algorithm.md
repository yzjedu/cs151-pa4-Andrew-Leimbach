# Tasks:
Load headlines

Count headlines containing word

Write headlines with words

Average the headline length

Find shortest and longest headline

Call functions

# Algorithm for load_headlines
**Purpose:** Load headlines from a file into a list


**Parameters:** file_name

**Return:** A list of strings, or None if not successful

**Algorithm:**
1. Attempt to open file in read mode
2. If successful:
   1. Intialize an empty list headlines
   4. For each line in the file:
      1. Strip whitespace and add the line to headlines
   3. Return headlines
3. If file is not found:
   1. Print error message 
   2. Return None
 # Algorithm for count_headlines_with_words
**Purpose:** Count the number of headlines that contain a specific word


**Parameters:** headlines, words

**Return:** An integer count

**Algorithm:**
1. Initialize a variable count to 0 
2. For each headline in headlines:
   1. If word is found in headline count by 1
3. Return count

# Algorithm for write_headlines_with_word
**Purpose:** Write headlines containing a specific word to a new file


**Parameters:** headlines, words, output_file

**Return:** None

**Algorithm:**
1. Open the file output_file in write mode
2. For each headline in headlines:
   1. If word is found in headline, write the headline to file
3. CLose the file
# Algorithm for average_headline_length
**Purpose:** Calculate the average number of characters per headline


**Parameters:** headlines

**Return:** A float representing average, or 0 if headlines is empty

**Algorithm:**
1. Initialize a variable total_characters to 0
2. For each headline in headlines:
   1. Add the length of headline to total_characters
3. If the length of headlines is greater than 0:
   1. Return total_characters divided by the number of headlines
4. Otherwise return 0
# Algorithm for find_extreme_headlines
**Purpose:** Find the longest and shortest headlines based on character count


**Parameters:** headlines

**Return:** A tuple containing the longest and shortest headlines(both strings)

**Algorithm:**
1. If headlines is empty
   1. Return an empty tuple(("",""))
2. Initialize longest and shortest to the first headline in headlines
3. For each headline in headlines:
   1. If the length of headline is greater than longest, update longest to headline
   2. If the length of headline is less than shortest, update shortest to headline
4. Return the tuple (longest, shortest)
# Algorithm for main
**Purpose:** Manage program flow and handle user interaction


**Parameters:** None

**Return:** None

**Algorithm:**
1. Initialize headlines to None.
2. Initialize choice to 0.
3. While choice does not equal 6
   1. Go through each option calling function and if not successful output error message
4. End Program
   