# 02_word_replace.py
# Day 19 Mini Project – Week 3 (File Handling & Functions)
# Goal: Replace one word with another word (Modular File Version)
# Author: Faiz Ur Rehman Ashrafi
# Description:
# This version uses functions for better structure and reusability.
# It reads content from a file, replaces chosen words, and writes them back.


def index_find(find_word, words):
    """Find index of a word inside a list of words."""
    if find_word in words:
        return words.index(find_word)
    else:
        print(f"'{find_word}' not found!")
        return None


def replace_content(filename, updated_text):
    """Write updated text into the same file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(updated_text)


def replace_word(find_word, index_, words):
    """Replace specific word in the list."""
    replace_word = input("Replace: ")
    words.remove(find_word)
    words.insert(index_, replace_word)
    print(f"'{find_word}' replaced by '{replace_word}'")
    return words


def new_text(words):
    """Convert list of words back into formatted text."""
    return " ".join(words)


def show_text(text):
    """Display formatted content."""
    print("\n-- Your File Content --\n")
    print(text, "\n")


def content(filename):
    """Read file content safely."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"{filename} NOT FOUND!")
        return None


def main():
    print("=== Welcome To Word Replacer ===")

    filename = input("Enter your filename: ")
    text = content(filename)

    if not text:
        return

    show_text(text)
    words = text.strip().split(" ")
    new = text

    while True:
        find_word = input("Enter word to replace (or 'q' to quit): ")
        if find_word.lower() == "q":
            break

        find_index = index_find(find_word, words)
        if find_index is None:
            continue

        words = replace_word(find_word, find_index, words)
        new = new_text(words)
        replace_content(filename, new)

    choice = input("\nDo you want to view updated content? (y/n): ")
    if choice.lower() == "y":
        show_text(new)
    else:
        print("Thank you for using Word Replacer!")


if __name__ == "__main__":
    main()
