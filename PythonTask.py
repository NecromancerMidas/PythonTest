# ChatGPT
# Here's a random Python task for you: Create a Python script to analyze a text file.

# The task involves the following steps:

# Read a Text File: Your script should be able to read a text file (for example, a .txt file).

# Count Word Frequency: Analyze the file to count the frequency of each word.

# Filter Out Common Words: Optionally, you could filter out common English words (like "the", "is", "at", "which", etc.) to focus on more meaningful words.

# Output Results: Finally, display or output the top 10 most frequent words in the file.

# This task involves file handling, string manipulation, and data analysis, offering a well-rounded exercise in Python programming.

text:str = open("sample_text (1).txt").read()
print(text)

def fileHandling(file:str) :
   split:list = file.split(" ")
   newlist:list = []
   
   for word in split :
    newword:str = "".join(char for char in word if char.isalpha() or char.isspace()).casefold()
    newlist.append(newword)
   split = newlist

   uniqueWords:list = list(set(split))
   for word in uniqueWords :
    
    print(word + " " + str(split.count(word)))
    # for item in split : #replace with split.count(word)
    #     if(item == word) :
    #      counter += 1
    



fileHandling(text)