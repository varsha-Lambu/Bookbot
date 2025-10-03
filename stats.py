def  get_count(lines):
    text = lines.split()
    return len(text)




def count_alphabets(lines):
    text={}
    for char in lines:
        char=char.lower()
        if char.isalpha():
            if char not in text:
                text[char]=0
            text[char]+=1
    return text

def get_num(item):
    return item["num"]

# New function: convert dictionary to sorted list of dicts
def char_count_report(count_dict):
    report_list = []

    for char, count in count_dict.items():
        if char.isalpha():  # skip non-alphabet characters
            report_list.append({"char": char, "num": count})
    
    # Sort the list from greatest to least using the helper
    report_list.sort(key=get_num, reverse=True)
    return report_list