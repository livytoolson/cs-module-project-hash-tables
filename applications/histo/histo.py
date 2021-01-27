def histo(textfile):
    with open(textfile, 'r') as fileoutput:             # open file, make it readable, store it as fileoutput variable
        data = fileoutput.read()
    
    words = data.split()                                # split data file into an array
    cache = {}                                          # counter

    for word in words:
        word = word.lower().strip('":;,.-+=/\\|[]}{()*^&')      # lowercase all words and strip punctuation

        if word not in cache:                                   # if word is not in cache, add it, and append # for each word
            cache[word] = []
        cache[word].append('#')                                 # '#' is acting like word counter
    
    ordered_cache = [word for word in cache]

    def sorter(word):
        return cache[word]

    ordered_cache.sort(key = sorter, reverse = True)

    for word in ordered_cache:
        print(f"{word:20} {''.join(cache[word])}")

    # for word in ordered_cache:                                        # access key and value in cache
    #     count_str = ''

    #     for symbol in cache[word]:                                    # removes brackets from output
    #         count_str += '#'

        # print(f'{word:20}    {count_str}')
    #   print("{:>20}{:>100}".format(word, count))
    #   print(f"{i:3} {fib(i)}")

histo('robin.txt')
