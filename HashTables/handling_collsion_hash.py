def get_index(data_list, a_string):
    result = 0
    for a_character in a_string:
        a_number = ord(a_character)
        result += a_number

    list_index = result % len(data_list)
    return list_index


def get_valid_index(data_list, key):
    idx = get_index(data_list, key)

    while True:
        kv = data_list[idx]

        if kv is None:
            return idx

        k, v = kv
        if k == key:
            return idx

        idx += 1
        if idx == len(data_list):
            idx = 0


data_list = [None] * 4096
key, value = "Gaurav", "9811100022"
idx = get_valid_index(data_list, key)
data_list[idx] = key, value

key, value = "Gaaruv", "9811100000"
idx = get_valid_index(data_list, key)
data_list[idx] = key, value

keys = [key[0] for key in data_list if key is not None]
print(keys)
