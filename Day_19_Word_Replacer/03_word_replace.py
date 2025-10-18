# 03_word_replace.py
# Day 19 Mini Project – Week 3 (File Handling & Functions)
# Goal: Replace one word with another word inside a text file (Final Version)
# Author: Faiz Ur Rehman Ashrafi
# Description:
# This is the final, professional version.
# It reads content from a file, replaces all occurrences of a specific word,
# and displays how many times replacement occurred.


def show_content(filename):
    """Display the current file content."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            print("\n=== Your Content is here ===\n")
            print(content)
    except FileNotFoundError:
        print(f"{filename} FILE NOT FOUND!")


def replace_word_in_file(filename, old_word, new_word):
    """Replace all occurrences of a word inside a text file."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()

        count = content.count(old_word)
        if count == 0:
            print(f"'{old_word}' not found in file.")
            return

        updated_content = content.replace(old_word, new_word)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(updated_content)

        print(f"Successfully replaced '{old_word}' with '{new_word}' ({count} times).")

    except FileNotFoundError:
        print(f"ERROR: The file '{filename}' does not exist.")
    except Exception as e:
        print("An unexpected error occurred:", e)


def main():
    print("-==- Welcome To Word Replacer -==-")

    filename = "content.txt"  # Default file name (you can change it)
    show_content(filename)

    old_word = input("\nEnter the word to replace: ")
    new_word = input("Enter the new word: ")

    replace_word_in_file(filename, old_word, new_word)


if __name__ == "__main__":
    main()
