def split_on(words, width):
    """
    The method collects a list of words into lines of the desired length.  

    """
    splitted = [[]]
    sumr = 0
    for item in words:
        if sumr + len(item) < width:
            splitted[-1].append(item)
            sumr += len(item) + 1
        else:
            sumr = len(item)
            splitted.append([item])

    return splitted


width = 80
string_words_list = []
string_list = []

# read from file some_txt.txt
with open("some_txt.txt", 'r', encoding='utf-8') as f:
    paragraphs = list(f)

# parsing paragraphs
for paragraph in paragraphs:
    words = paragraph.split()
    string_words_list.append(split_on(words, width))

# collects a list of strings
for i in string_words_list:
    string_list.append([' '.join(k) for k in i])

# edit lines from a list
for string in string_list:
    for i, line in enumerate(string[:-1]):
        words = line.split()
        s = width - sum(map(len, words))
        cs = len(words) - 1
        spw, mod = divmod(s, cs)
        spw = spw if spw > 0 else 1
        ws = [' ' * spw] * (cs - mod) + [' ' * (spw + 1)
                                         for _ in range(mod)] + ['']
        string[i] = ''.join(w+s for w, s in zip(words, ws))

# print text line by line
print('\n\n'.join('\n'.join(string) for string in string_list))
