class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.end = False

class PrefixTree:
    def __init__(self):
        self.sh = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.sh
        for i in word:
            idx = ord(i) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.end = True
            
    def search(self, word: str) -> bool:
        curr = self.sh
        n = len(word)
        i = 0

        while i<n:
            idx = ord(word[i]) - ord('a')

            if not curr or not curr.children[idx]:
                return False
            curr = curr.children[idx]
            i += 1
        
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.sh
        n = len(prefix)
        i = 0

        while i<n:
            idx = ord(prefix[i]) - ord('a')

            if not curr or not curr.children[idx]:
                return False
            curr = curr.children[idx]
            i += 1
        
        return True
        