def is_vowel(letter):
    letter_set = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    if letter in letter_set:
        print(letter, "is a Vowel")
    else:
        print(letter, "is a Consonant")


if __name__ == '__main__':
    value = input("Enter a letter of the alphabet: ")
    is_vowel(value)
