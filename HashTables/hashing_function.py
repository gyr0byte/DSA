def get_index(data_list, a_string):
    result = 0
    for a_character in a_string:
        a_number = ord(a_character)
        result += a_number
        
    list_index = result % len(data_list)
    return list_index