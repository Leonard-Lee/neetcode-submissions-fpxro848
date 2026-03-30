class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for str in strs:
            arr = [0] * 26 # array presents 26 letters
            for c in str:
                arr[ord(c) - ord('a')] += 1

            map[tuple(arr)].append(str)
        
        return list(map.values())