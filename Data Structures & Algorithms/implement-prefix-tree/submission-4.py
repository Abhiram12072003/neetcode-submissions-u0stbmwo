class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:
    def __init__(self):
        self.sh = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.sh
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end = True
            
    def search(self, word: str) -> bool:
        curr = self.sh
        for i in word:
            if not curr or i not in curr.children:
                return False
            curr = curr.children[i]
        
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.sh
        for i in prefix:
            if not curr or i not in curr.children:
                return False
            curr = curr.children[i]
        
        return True
        