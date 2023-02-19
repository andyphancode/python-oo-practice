"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Finds random words in dictionary
    
    >>> wf = WordFinder("wordsimple.txt")
    3 words read
    
    >>> type(wf.random()) == str
    True

    >>> wf.random() in ["cat","dog","porcupine"]
    True
    """

    def __init__(self, filepath):
        """Read file and report amount of words read"""

        file = open(filepath)

        self.words = self.parse(file)

        print(f"{len(self.words)} words read")
    
    def parse(self, file):
        """Returns list of words"""

        return [word.strip() for word in file]

    def random(self):
        """Returns random word from list of words"""

        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """
    >>> swf = SpecialWordFinder("wordcomplex.txt")
    4 words read

    >>> type(swf.random()) == str
    True

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True
    """

    def parse(self, file):
        """Returns list of words skipping comments"""
        return [word.strip() for word in file if word.strip() and not word.startswith("#")]
