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

class WordWithCount:
  def __init__(self,word,count):
    self.word = word
    self.count = count
  def printthis(self):
    print(self.word + " " + str(self.count))
def sortByCount(item):
  return item.count
def fileHandling(file:str) :
   split:list = file.split(" ")
   newlist:list = []
   ignoredWords:list = ["the","and","or","is","at","which","so","but","an","has","as","in","on","it","of","its","to","was"]
   for word in split :
    newword:str = "".join(char for char in word if char.isalpha()).casefold()
    if newword not in ignoredWords and len(newword) > 1:
      newlist.append(newword)
   split = newlist

   uniqueWords:list = list(set(split))
   AllWords:list = []
   for word in uniqueWords :
    AllWords.append(WordWithCount(word,split.count(word)))
    # for item in split : #replace with split.count(word)
    #     if(item == word) :
    #      counter += 1
   AllWords.sort(key=sortByCount)
   for index in range(1,10):
    AllWords[len(AllWords) - index].printthis()



fileHandling(text)