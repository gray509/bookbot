def count_words(s):
    words = s.split()
    return len(words)

def count_instance_char(s):
    c = {}
    for char in s.lower():
        if char in c:
            c[char] += 1
        else:
            c[char] = 1            
    return c

def sort_dict(char_count):
    arr = []
    for char in char_count:
        dic = {"char": char, "num": char_count[char]}
        arr.append(dic)
    def get_count(item):
        return item["num"]

    arr.sort(key=get_count, reverse=True)
    return arr

