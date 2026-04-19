class Solution:
    def func(self, digits, itr, mp, s):
        
        if itr == len(digits):
            self.answer.append(s)
            return

        lis = mp[digits[itr]]
        
        for i in range(len(lis)):
            # s += lis[i]
            self.func(digits, itr+1, mp, s + lis[i])

    def letterCombinations(self, digits: str) -> List[str]:
        mp = {'2': ['a', 'b', 'c'], 
        '3': ['d', 'e', 'f'], 
        '4': ['g', 'h', 'i'], 
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']}
        if len(digits) == 0:
            return []
        self.answer = []
        self.func(digits, 0, mp, '')
        return self.answer