class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for str in strs:
            letter_list = [0] * 26
            for c in str:
                letter_list[ord(c) - ord('a')] += 1

            map[tuple(letter_list)].append(str)

        return list(map.values())
        