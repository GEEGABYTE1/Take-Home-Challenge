from depth import dfs
from breadth import bfs

class TreeNode:
    def __init__(self, value):
        self.value = value 
        self.children = []
    
    def add_child(self, word, prev_node=None): 
        count = 0
        for letter in word:
            
            if self.letter_checker(letter, self.children) == False:
                tree_object = TreeNode(letter)
                self.add_letter(tree_object)
                self = tree_object
            else:
                for treenode in self.children:
                    if treenode.value == letter:
                        self = treenode
                        
    
    def add_letter(self, child_node):
        self.children.append(child_node)

    def letter_checker(self, letter, list):
        checker = False 
        for obj in list:
            if obj.value == letter:
                checker = True
    
        return checker
                    
        
    def input_prefix(self, word):
        lists = []
        nodes = [self]
        while len(nodes) > 0:
            current_node = nodes.pop()
            if current_node.value == word[0]:
                result = bfs(current_node, None)
        
            nodes += current_node.children
        
        return lists
             
    def child_compressor(self, lst):
        values = []
        for node in lst:
            values.append(node.value)
        return values

    def delete(self):
        user_prompt = str(input("Please type in a word you would like to delete: "))
        try:
            user_prompt = user_prompt.lower()
            user_letters = [i for i in user_prompt]

            nodes = [self]
            while len(nodes) > 0 and len(user_letters) > 0:
                current_node = nodes.pop()
                if current_node.value == user_letters[0]:
                    current_node.value = None 
                    user_letters.pop(0)
                
                nodes += current_node.children
            
            if len(user_letters) == 0:
                return True 
        except:
            return
    
    def search_keyword(self):
        user_prompt = input("Please enter a word you would like to search: ")
        user_prompt = user_prompt.lower()
        user_letters = [i for i in user_prompt]

        returned_path = []

        nodes = [self]
        while len(nodes) > 0 and len(user_letters) > 0:
            current_node = nodes.pop()
            if current_node.value == user_letters[0]:
                returned_path.append(current_node)
                user_letters.pop(0)
            
            nodes += current_node.children 
        
        returned_path = [i.value for i in returned_path]
        user_letters = [i for i in user_prompt]
        if returned_path == user_letters:
            return True 
        else:
            return False

    def remove_child(self, child_node):
        self.children = [i for i in self.children if not i == child_node]

    def traverse(self):
        nodes = [self]
        while len(nodes) > 0:
            current_node = nodes.pop()
            print(current_node.value)
            nodes += current_node.children 

test = TreeNode("")

test.add_child("west")
test.add_child("waka")
test.add_child("weep")
test.add_child("branch")
test.add_child('bam')
test.traverse()






# d p a c t s e w