class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.node = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.node
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end = True
        return

    def search(self, word: str) -> bool:
        n = len(word)
        curr = self.node
        itr = 0
        # print(curr, word)
        def func(curr, itr):
            while itr<n:
                if word[itr] == '.':
                    if not curr.children:
                        return False
                    for node in curr.children:
                        if func(curr.children[node], itr+1):
                            return True
                    return False
                else:
                    if word[itr] not in curr.children:
                        return False
                    curr = curr.children[word[itr]]
                itr += 1 
            return curr.end if itr == len(word) else False
        return func(curr, 0)
