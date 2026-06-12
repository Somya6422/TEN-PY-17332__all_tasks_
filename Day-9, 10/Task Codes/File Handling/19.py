# 19. Count Frequency of a Given Word
search_word = input("Enter word: ").lower()
f = open("student.txt", "r")
words = f.read().lower().split()
count = words.count(search_word)
print("Frequency:", count)
f.close()\n