def check_length(word_list):
    longest = ""
    double_words = []
    for word in word_list:
        if len(word) > len(longest):
            longest = word
    #if  = len(longest):
    return longest

words = []
word_ = ""
while word_ != "1":
    word_ = input("Add word to list (or 1 to end): ")
    words.append(word_)
print(f"The longest word in the list {words} is {check_length(words)}")
