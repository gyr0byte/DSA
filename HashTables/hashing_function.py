def get_index(list_data, a_string):
    result = 0
    for a_character in a_string:
        a_number = ord(a_character)
        result += a_number
        
    list_index = result % len(list_data)
    return list_index