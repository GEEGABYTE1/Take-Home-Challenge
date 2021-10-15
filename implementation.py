from tree import TreeNode
import time
from dfs import dfs

# Test inputs
lst = []


class Trie:

    #def running(self):
        #self.add_keyword()
        

    def implementation(self, lst):
        self.tree = TreeNode(len(lst))
        head_node = self.tree
        letters_in_tree = []

        for word in lst:
            word = word.lower()
            self.tree = head_node
            counter = 0
            for letter in word:
                if len(letters_in_tree) == 0:
                    self.tree.add_child(TreeNode(letter))
                    letters_in_tree.append(letter)
                
                elif word[0] == head_node.children[0].value and len(letters_in_tree) != 0 and counter == 0:
                    counter += 1
                    self.tree = self.tree.children[0]
                    letters_in_tree.append(word[0])
                    continue

                elif letter == letters_in_tree[-1]:
                    self.tree.add_child(TreeNode(letter))
                    letters_in_tree.append(letter)
                    self.tree = self.tree.children[0]
                    counter += 1
                    continue
                   
                else:
                    possible_letter = TreeNode(letter)
                    current_tree_lists = [i.value for i in self.tree.children]
                    if not letter in current_tree_lists:              
                        self.tree.add_child(possible_letter)
                        letters_in_tree.append(letter)
                
                if len(self.tree.children) == 2:
                    left_side = self.tree.children[0]
                    right_side = self.tree.children[-1]
                    if left_side.value == letter:
                        self.tree = left_side 
                        continue 
                    elif right_side.value == letter:
                        self.tree = right_side 
                        continue 
                else:
                    self.tree = self.tree.children[0]
                
                counter += 1
        
        self.tree = head_node


    def traverse(self):
        user_prompt = input("Please enter a word you are trying to find in a trie: ")
        tree = self.tree

        user_prompt = user_prompt.lower()
        user_letters = [i for i in user_prompt]

        returned_path = []

        nodes = [self.tree]
        while len(nodes) > 0 and len(user_letters) > 0:
            current_node = nodes.pop()
            if current_node.value == user_letters[0]:
                returned_path.append(current_node)
                user_letters.pop(0)
            nodes += current_node.children
        

        returned_path = [i.value for i in returned_path]
        user_letters  = [i for i in user_prompt]
        if returned_path == user_letters:
            return True 
        else:
            return False

    def add_keyword(self):
        user_word = str(input("Please enter a word to add to the trie: "))
        lst.append(user_word)
        self.implementation(lst)

    def delete(self):
        user_prompt = str(input("Please enter a word that you are trying to find in a trie: "))
        try:
            tree = self.tree  
            user_prompt = user_prompt.lower()
            user_letters = [i for i in user_prompt]

            nodes = [self.tree]
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

class Prompt:
    trie = Trie()
    def __init__(self):
        print("Welcome to the trie! ")
        time.sleep(0.2)
        print("Here are the commands: \n")
        time.sleep(0.3)
        print(":/add_keyword - to add a keyword \n")
        time.sleep(0.3)
        print(":/search_keyword - to search for keyword \n")
        time.sleep(0.3)
        print(":/delete_keyword - to delete a keyword from the trie \n")
        time.sleep(0.3)
        print(":/search_bar_sim - Experience the search algoritm on networks \n")
        time.sleep(0.3) 
        self.prompt()

    def prompt(self):
        while True:
            print("\n")
            user_prompt = str(input(':'))
            
            if user_prompt == '/add_keyword':
                self.trie.add_keyword()

            elif user_prompt == '/search_keyword':
                result = self.trie.traverse()
                print(result)

            elif user_prompt == '/delete_keyword':
                deletion = self.trie.delete()
                time.sleep(0.2)
                if deletion == True:
                     print("Keyword deleted succesfully! ")
                else:
                    print("Keyword was not found in the trie ")
            
            elif user_prompt == '/search_bar_sim':
                user_letter_prompt = str(input('Search Prompt :/ '))
                user_letter_prompt = user_letter_prompt.lower()
                results = self.trie.tree.traversing_tree(user_letter_prompt)

                
                for tree_object in results:
                    for object in tree_object:
                        print(object)
                                


            elif user_prompt == '/quit':
                break
            else:
                print("That command does not seem to be valid")


        
        
            



#test.implementation(lst)
test = Prompt()
print(test.prompt())



