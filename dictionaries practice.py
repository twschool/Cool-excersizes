dictionary = {
    10169420: True,
    2169420: True,
    5636123: True
}
dictionary_input = int(input("Card number: "))
try:
    print(f"{(dictionary[dictionary_input])}")
except KeyError:
    print("Not a valid card number")
