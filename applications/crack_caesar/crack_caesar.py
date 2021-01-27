# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

most_frequent = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

with open('ciphertext.txt', 'r') as fileoutput:                 # open and read file
    data = fileoutput.read()                                    # store output string into data variable
    letters = [letter for letter in data]

    cache = {}

    for letter in letters:

        if letter not in most_frequent:
            continue
        
        if letter not in cache:
            cache[letter] = 0
        cache[letter] += 1

    ordered_freq = [letter for letter in cache]

    def sorter(letter):
        return cache[letter]
        
    ordered_freq.sort(key = sorter, reverse = True)             # reverse = True --> greatest to least

    story = ''

    for letter in letters:

        if letter not in ordered_freq:
            story += letter
            continue
        
        index = ordered_freq.index(letter)                      # find index of letter

        new_letter = most_frequent[index]

        story += new_letter

    print(story)
