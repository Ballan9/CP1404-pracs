word_count = {}

string = input("Please enter a string: ").split()

for word in string:
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1

length_of_largest_string = max(len(word) for word in word_count)

print(word_count)

for word in sorted(word_count, key=str.upper):
    print("{:{}} : {}".format(word, length_of_largest_string, word_count[word]))