# Triegig ๐ด

Interact with the global trie right from your localhost with the simplest commands. Forget trying to implement the data structure all by yourself when you can implement the data structure by just importing the library.

Users have the option to add, remove, search, and even emulate a search prefix predictor with this trie library.


# Importing ๐งช

The library can be downloaded by typing the command in the terminal: `pip install triegig`.

## Implementation ๐ 

Users can then import the trie to their workspace using: the command `from tree import initializer()`.

This will import the Global Trie to your workspace.

# Adding a word to the trie ๐

Users can add words to the trie using the command:

Syntax: `initializer().add_child(word)`. 

*Note*: The `initializer()` can be set to a variable name when importing to make code much cleaner.


# Removing a keyword ๐ง

Users can also remove words from the trie using the command:

Syntax: `initializer().delete()`

The user will then be asked to type in a word, which the program will delete letter by letter from the trie.


# Searching for a Word in the Trie ๐ฎ

Users can search for words in the trie.

Syntax: `initializer().search_keyword()`

The user will be prompted to search for a word, and the program will return either `True` or `False` if the word is in the Trie.

# Auto-Complete Simulator โ๐ป

Users can type a prefix and the program will return all the words in the trie that start with that very prefix.

Syntax: `initializer().input_prefix()` 

The command will return a list of all the words in the trie that match the prefix inputted with the help of the DFS algorithm.

# Extra Information ๐

*Note*: Library works for all Python versions above 3.0
Library Link: https://pypi.org/project/triegig/

