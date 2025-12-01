def get_book_text(book_path):
    with open(book_path) as f:
    # do something with f (the file) here
        file_contents = f.read()
    return file_contents

def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    lower_case = text.lower()
    counts = {}

    for char in lower_case:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def ret_num(item):
    return item["num"]

def sort_character_count(counts):
    dict_list = []
    for key, value in counts.items():
        dict_list.append({"char": key, "num": value})

    dict_list.sort(key=ret_num,  reverse=True)

    return dict_list
    


