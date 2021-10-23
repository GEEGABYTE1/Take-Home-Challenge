# Triegig 🌴

Triegig is a light and fast trie library that allows users to implement and interact with the trie data structure. Instead of implementing their custom data structure, why not use a global trie that is live and used by many users. 

Triegig is great for fetching data for NLP projects, and for literature research for the most used words. 

Users can add, delete, search, and even emulate the auto-complete feature that most search engines have making their research and searching more efficient.

# Technical Information ⚙️

The Trie was made mostly based of the typical tree data structure.

### Time Complexity 🕰
*Note*: All processes are relative to the user-inputted words
 - Adding a keyword: `O(n)` 
 - Subtracing a keyword: `O(n)`
 - Searching a keyword: `O(n)`
 - Input Prefix: `O(n) + O(n')` where `n'` represents the array with filtered words equivalent to the length of the prefix.

## Adding a keyword 💡

To add a keyword to the trie, the word will be split up into letters and will be filtered into lowercase to be consistent with the inputs. The program will add each letter as a node. However, strings with digits or symbols will remain the same.

If a letter has already been added, insted of the root node being the very top node, the node with the same letter as our "new letter" will be the new root node, and the process of adding a letter to a new root letter will continue iteratively.

## Deleting a keyword 🪓

Similar to adding a keyword, the delete function will split the word into letters and will traverse the tree letter by letter. 

If the node it is currently on has the same value as the desired letter it is on, the node value will be replaced with `None` (indicating that it has been deleted) and will pop the letter from the word to receieve a new letter to search for. Do note that when the program receieves a new letter to search for, the root node remains the same as the node it been replaced since according to a trie, the letters added are in-terms of depth and not width. 

## Searching for a keyword 🔎

Similar to the delete function, the program will prompt the user to search a word in the trie. It will then filter the word into lowercase since all letters had been added in their lowercase forms.

As the program traverses the trie, if a node has the same letter it is currently searching for, the traversal will continue but the letter from the word will be popped. This process will keep repeating itself until either all the letters are searched for, or the program has reached the bottom of the data structure.

If all the letters have been searched, the program will return `True`, else `False`.

## AutoComplete Emulation 🔮

With the help of the DFS algorithm (view depth.py for the algorithm implementation), the user will type in a prefix and the program will filter all the words with that very prefix in `O(n)` time. 

The program will first start off traversing the trie by finding the first letter in the inputted prefix. When that has been done, the dfs algorithm will be ran iteratively relative to the length of the prefix to search for letters that start with the first letter of the prefix. We decided to use the DFS algorithm as the words are implemented by depth. Moreover, to make sure each depth traversal is unique, the node that had just been traversed from the root node gets ignored from the child list temporarily by setting the value as `None`.

After the traversal is complete, all the sample words are then put into an array. With an iterative approach, the program will use the prefix the user has orignially inputted and see if that prefix is present for all the words outputted. Remember, all the words that been returned by our traversal originally were just words with the same first letter as the inputted prefix. 

If the prefix of the word returned matches the inputted prefix, the word will stay in the array, else, the word gets popped.


# CLI 💻

To learn about the controls and how the user can interact with the data structure, visit the "CLI Documentation": https://github.com/GEEGABYTE1/Take-Home-Challenge/blob/master/README.md. 

All the commands and details about inputs and outputs are listed on that documentation.

# Global Server 🎆

The trie is hosted with streamlit and on their cloud. Each user's input is gone through Streamlit's Queue data structure, which will then complete the process in a FIRST-IN-FIRST-OUT order, making it efficient for the users. 

The commands inputted are sent to Streamlit's Stack as a process, and will run in a linearized fashion. No command is prioritized over another, and there is only one terminal entry and exit point for the data. 


# More information 📕

Link to Library: https://pypi.org/project/triegig/

Made in Python 3.9
- `depth.py` = DFS algorithm
- `tree.py` = Trie Data Structure

Methods that have not been talked about are helper methods and do not provide much significance to the overall data structure; rather only the processes.

