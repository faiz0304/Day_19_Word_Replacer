# 01_word_replace.py
# Day 19 Mini Project – Week 3 (File Handling & Functions)
# Goal: Replace one word with another word (Basic Version)
# Author: Faiz Ur Rehman Ashrafi
# Description:
# This script demonstrates a simple in-memory text replacement logic.
# It replaces the first occurrence of a word in a given text.

text = """
My name is Faiz and I am from Karachi.
"""
print("-- Original Text --")
print(text, "\n")

# Split text into words
words = text.strip().split(" ")

# Ask the user for the word to find
find_word = input("Find: ")

if find_word in words:
    # Get index of the word and replace it
    index_ = words.index(find_word)
    replace_word = input("Replace: ")

    # Replace operation
    words.remove(find_word)
    words.insert(index_, replace_word)

    # Join back into a sentence
    new_text = " ".join(words)
    print(f"\n'{find_word}' replaced by '{replace_word}' successfully!")
    print("\n-- Updated Text --")
    print(new_text)
else:
    print(f"'{find_word}' not found!")
