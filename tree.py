class TreeNode:
    def __init__(self, value):
        self.value = value 
        self.children = []
    
    def add_child(self, word, prev_node=None):
        letters_of_word = word

        if len(word) == 0:
            return
    
        while letters_of_word:
            current_letter = letters_of_word[:1]
            child_node = TreeNode(current_letter)
            parent_childs = self.child_compressor(self.children)
            if len(self.children) == 0:
                self.children.append(child_node)
                updated_word = word[1:]
                prev_node = child_node
                return child_node.add_child(updated_word, prev_node)
            
            elif child_node.value in parent_childs:
                for letter in self.children:
                    if prev_node == None:
                        prev_node = child_node
                    if prev_node.value == letter.value:
                        updated_word = word[1:]
                        prev_node = letter
                        return self.add_child(updated_word, prev_node)
            else:
                self.children.append(child_node)
                updated_word = word[1:]
                prev_node = child_node
                return self.add_child(updated_word, prev_node)
    

            
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

test = TreeNode(None)

test.add_child("west")
test.add_child("cap")
test.add_child("dap")
print(test.traverse())


# d p a c t s e w