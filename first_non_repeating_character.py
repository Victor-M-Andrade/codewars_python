def first_non_repeating_letter(string):
    
    list = [i.lower() for i in string]

    for i in range(len(list)):
        if list.count(list[i]) == 1:
            return string[i]
    
    return ""




print(first_non_repeating_letter('aabb'))