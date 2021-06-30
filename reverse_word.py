
### String reversing function ###

# Variant 1
def reverse_word(word: str):

    symbols_list = list(word)
    symbols_reversed_list = []

    for i in range(len(symbols_list)):
        if i == 0:
            symbols_reversed_list.append(symbols_list[i])
        else:
            symbols_reversed_list.insert(0, symbols_list[i])
    
    reversed_word = ''.join(symbols_reversed_list)

    return reversed_word

# Variant 2
def reverse_word_fast(word: str):

    return word[::-1]

# Variant 3
def reverse_word_list_comp(word: str):

    return ''.join([symbol for symbol in word[::-1]])

print(reverse_word('Johny Ma'))
print(reverse_word_fast('Johny Ma'))
print(reverse_word_list_comp('Johny Ma'))