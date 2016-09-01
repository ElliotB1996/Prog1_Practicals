word_counter_dict = {}

text = input("Enter your String")
text = text.split(" ")

for word in text:
    if word in word_counter_dict:
        word_counter_dict[word] +=1
    else:
        word_counter_dict[word] = 1

for word in sorted(word_counter_dict):
    print("{:<15} : {}".format(word, word_counter_dict[word]))