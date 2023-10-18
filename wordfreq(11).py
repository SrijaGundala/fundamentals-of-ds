import string
from collections import Counter

file_path = r"C:\Users\srija\Desktop\sample_text.txt"

with open(file_path, "r") as file:
    text = file.read()
    words = text.split()
    word_freq = Counter(words)  # Correct the capitalization of "Counter"

for word, freq in word_freq.items():  # Correct "counter" to "Counter"
    print(f"{word} : {freq} ")  # Use lowercase "f" in "f-string"
