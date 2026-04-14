MAX_HASH_TABLE_SIZE = 4096

class BasicHashTabe:
    def __init__(self, max_size = MAX_HASH_TABLE_SIZE):
        self.data_list = [None] * max_size
        
    def insert(self, key, value):
        idx = get_valid_index(self.data_list, key)
        self.data_list[idx] = key, value
        
        
def get_index(data_list, a_string):
    result = 0 
    for a_character in a_string:
        a_number = ord(a_character)
        result += a_number
        
    list_index = result % len(data_list)
    return list_index

def get_valid_index(data_list, key):
    idx =  get_index(data_list, key)

    while True:
        kv = data_list[idx]
        
        