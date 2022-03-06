def check_a(letter):
    if letter[0].upper() == "A":
        return True
    else:
        return False


# Main routine
word = input("Enter word: ")
print(f"It is {check_a(word)} that the word {word} has an a in it")
