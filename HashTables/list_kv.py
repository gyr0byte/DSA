def get_index(data_list, a_string):
    result = 0
    for a_character in a_string:
        a_number = ord(a_character)
        result += a_number

    list_index = result % len(data_list)
    return list_index


data_list = [None] * 4096
key, value = "Gaurav", "9811100022"
idx = get_index(data_list, key)
data_list[idx] = (key, value)

key, value = "Sirjan", "9811122200"
idx = get_index(data_list, key)
data_list[idx] = (key, value)
key, value = data_list[idx]
keys = [key[0] for key in data_list if key is not None]
print(keys)
