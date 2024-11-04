"""
String handling is important.  We can break a string into pieces to help us look at parts one at a time using the string.split function.
Have the user enter a sentence or paragraph and gives a word count.
"""

print("Enter Sample Sentance: ")
x = str(input())
count = x.count(" ")
print(f"there are ", {count+1}, " words in that sentance!")


