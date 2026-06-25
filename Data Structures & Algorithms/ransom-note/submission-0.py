class Solution:
    # if magazine string is way larger than ransome note string
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # map chars to their frequency in rasom note
        mapping = {}
        for ch in ransomNote:
            if ch == " ":
                continue
            mapping[ch] = mapping.get(ch, 0) + 1

        for ch in magazine:
            if ch in mapping and mapping[ch] > 0:
                mapping[ch] -= 1

        for key, val in mapping.items():
            if val != 0:
                return False

        return True


        

        

        