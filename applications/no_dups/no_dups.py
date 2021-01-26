def no_dups(s):
    split_str = s.split()
    res = ""
    count = {}
    # [spam, spam, spam, eggs, spam, sausage, spam, spam, and, spam]

    for word in split_str:
        if word not in count:           # if word is not in count, add it to count dictionary
            count[word] = 0
        count[word] += 1                # increment count by one each time we iterate over word

    for word in count:                  # loop through each key value pair in count,
                                        # if count[word] == 1: this will allow you to return words with count of 1, good to find word that appears the most
        res += word + " "               # add the keys, with the space to res
    return res.strip(" ")               # return res, use .strip(" ") to remove space at the end of the string

    # for word in split_str:
    #     if res.find(word) == -1:        # -1 didn't find word in res
    #         # res = res + word + " "
    #         res += word + " "           # need " " to add space between each word
    # return res.strip(" ")               # .strip() removes trailing white space


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))