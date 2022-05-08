class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashTable = {}
        for char in magazine:
            if char in hashTable:
                hashTable[char] += 1
            else:
                hashTable[char] = 1

        for char in ransomNote:
            if char in hashTable and hashTable[char] >= 1:
                hashTable[char] -= 1
            else:
                return False

        return True