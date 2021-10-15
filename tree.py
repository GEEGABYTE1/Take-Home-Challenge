class TreeNode:
    def __init__(self, value):
        self.value = value 
        self.children = []
        counter = 0

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_node):
        self.children = [i for i in self.children if i != child_node]

    def traversing_tree(self, keyword, max_count):
        nodes = [self]
        lst = []
        self.lists = []
        prev_letter = ''
        reference_letters = []
        first_letter = None
        counter = 0
        while len(nodes) > 0:
            current_node = nodes.pop()
            if type(current_node.value) == int:
                pass 
            elif first_letter == None:
                first_letter = current_node.children[-1]
            else:
                first_letter_checker = self.first_letter_checker(current_node.value, keyword)

                if len(nodes) == 0 and current_node.value != prev_letter or first_letter_checker == True:
                    counter += 1
                    self.lists.append(lst)
                    self.lists.append(["Partition"])
                    lst = []
                    
                    if counter >= max_count:
                        break
                    else:
                        nodes.append(first_letter)

                    
                
                
            lst.append(current_node)
            nodes += current_node.children 
            prev_letter = current_node.value
            
            
            
    
        return self.lists

    
    def first_letter_checker(self, keyword, inital_keyword=None):
        first_letter_const = inital_keyword[0]
        first_letter = keyword[0]
        first_letter_checker = None
        if len(self.lists) == 0 and first_letter_const == first_letter:
            first_letter_checker = True
        else:
            first_letter_checker = False

        return first_letter_checker
