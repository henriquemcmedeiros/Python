# Including library
from cs50 import get_string


def main():
    words, letters, sentence = 0, 0, 0
    text = get_string("Text: ")

    spaces = text.count(" ")
    words = spaces + 1

    for i in range(len(text)):
        if text[i].isalpha():
            letters += 1
    sentence = text.count("." or "?" or "!")

    # Grade the sentence
    l = letters / words * 100
    s = sentence / words * 100
    grade = round(0.0588 * l - 0.296 * s - 15.8)

    if grade < 1:
        print("Before Grade 1")
    elif grade > 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")


main()