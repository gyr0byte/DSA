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

    def