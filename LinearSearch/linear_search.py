def locate_card(card, query):
    for i in range(len(card)):
        if card[i] == query:
            return i
    return -1
card = [11, 13, 9, 7, 4, 2, 3, 1]   
query = 7
result = locate_card(card, query)
print(f"The position of the element is at index {result}")