class PrefixTree:

    def __init__(self):
        self.sh = []

    def insert(self, word: str) -> None:
        self.sh.append(word)

    def search(self, word: str) -> bool:
        if word in self.sh:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for word in self.sh:
            i = 0
            while i < min(len(prefix),len(word)) and word[i] == prefix[i]:
                i += 1
            if i == len(prefix):
                return True
        return False
        