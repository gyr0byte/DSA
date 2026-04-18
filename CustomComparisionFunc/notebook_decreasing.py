class Notebook:
    def __init__(self, title, username, likes):
        self.title = title
        self.username = username
        self.likes = likes
        
    def __repr__(self):
        return f"Notebook(title='{self.title}', username='{self.username}', likes={self.likes})"
    
def compare_likes(nb1, nb2):
        if nb1.likes > nb2.likes:
            return 'lesser'
        elif nb1.likes == nb2.likes:
            return 'equal'
        elif nb1.likes < nb2.likes:
            return 'greater'
        
def default_compare(x, y):
        if x < y:
            return 'lesser'
        elif x == y:
            return 'equal'
        elif x > y:
            return 'greater'
        
def merge_sort(objs, compare = default_compare):
        if len(objs) < 2:
            return objs
        mid = len(objs) // 2
        return merge(merge_sort(objs[:mid], compare), merge_sort(objs[mid:], compare), compare)

def merge(left, right, compare):
        i, j, merged = 0, 0, []
        while i < len(left) and j < len(right):
            result = compare(left[i], right[j])
            if result == 'lesser' or result == 'equal':
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                
        return merged + left[i:] + right[j:]
    
notebooks = [
    Notebook("Python Basics", "alice", 150),
    Notebook("Data Structures", "bob", 200),
    Notebook("Machine Learning", "charlie", 180),
    Notebook("Deep Learning", "dave", 220)
]
sorted_notebooks = Notebook.merge_sort(notebooks, compare_likes)
