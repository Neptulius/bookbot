def get_count(text):
    split = text.split()
    count = len(split)
    return count

def char_counts(text):
    counts = {}
    for char in text:
        char = char.lower()
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_on(dict):
    return dict["num"]



def split_dict(dict):
    dict_list = []
    for key, value in dict.items():
        dict_list.append({"char":key, "num":value})
    dict_list.sort(reverse=True, key= sort_on)
    return(dict_list)

def final_output(list):
    for i in list:
        if i["char"].isalpha():
             print(f"{i['char']}: {i['num']}")
    



    
