def word_count(s):
    counters = {}
    word_list = s.lower().split()

    for word in word_list:
        word.strip('":;,.-+=/\\|[]}{()*^&')
        if word not in counters:
            counters[word] = 0              # key is what is passed into the brackets, value is what we reassign it to
        counters[word] += 1
    print(f"\nkeys: {counters.keys()}")
    print(f"values: {counters.values()}")
    return counters                         # to return just keys there is a .keys() method, to return just values there is a .values() method


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))