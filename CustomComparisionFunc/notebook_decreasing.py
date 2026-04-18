class Notebook:
    def __init__(self, title, username, likes):
        self.title = title
        self.username = username
        self.likes = likes
        
    def __repr__(self):
        return f"Notebook(title='{self.title}', username='{self.username}', likes={self.likes})"
    
def compare_likes(nb1, nb2):
    
    