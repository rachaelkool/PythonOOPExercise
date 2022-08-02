"""Word Finder: finds random words from a dictionary."""


from os import pathsep
import random 

class WordFinder:
    '''Can tell you how many words in a file or give you a random word from that file
    
    >>> WordFinder('words.txt').num_words()
    235886 words read
    '''

    
    def __init__(self, path):
        self.path = path
        self.words = []
        handle = self.open()
        self.read(handle)
        
    def open(self): 
        '''Opens file based on path'''
        return open(self.path, "r")

    def read(self, handle):
        '''Loops through each line in file reference aka handle. 
        Appends each line with /n stripped to empty words array.
        '''
        for line in handle: 
            self.words.append(line.strip())

    def num_words(self): 
        '''Prints number of words now in words array'''
        print(f'{len(self.words)} words read')

    def random(self):
        '''Gives you a random word from file'''
        return random.choice(self.words)


class SpecialWordFinder(WordFinder): 
    '''Does same as WordFinder but excludes lines that are blank or start with "#"
    
    >>> SpecialWordFinder("complex.txt").words == ["pear", "carrot", "kale"]
    True
    '''

    def read(self, handle):
        '''Loops through each line in file reference aka handle. 
        Appends each line with /n stripped to empty words array.
        Does not append empty line or line that starts with "#"
        '''
        for line in handle: 
            if line.strip() and not line.startswith("#"):
                self.words.append(line.strip()) 

        

        
