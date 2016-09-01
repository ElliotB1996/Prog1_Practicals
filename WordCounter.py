word_counter_dict = {}

text = input("Enter your String")
text = text.split(" ")

longest_word_length = 0

for word in text:
    if word in word_counter_dict:
        word_counter_dict[word] +=1
    else:
        word_counter_dict[word] = 1

for word in word_counter_dict:
    current_longest = len(word)
    while current_longest > longest_word_length:
        longest_word_length = current_longest


for word in sorted(word_counter_dict):
    print("{:{}} : {}".format(word, longest_word_length, word_counter_dict[word]))