class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = defaultdict(list)
        for str in strs:
            freq = [0] * 26;
            for c in str:
                freq[ord(c) - ord('a')] += 1 

            ret[tuple(freq)].append(str)

        return list(ret.values())

        