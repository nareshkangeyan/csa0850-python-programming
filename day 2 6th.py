class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        res = []
        self.backtrack("", digits, res, phone)
        return res
    
    def backtrack(self, combination: str, next_digits: str, res: List[str], phone: Dict[str, List[str]]):
        if not next_digits:
            res.append(combination)
            return
        for letter in phone[next_digits[0]]:
            self.backtrack(combination + letter, next_digits[1:], res, phone)
