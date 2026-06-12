# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)

    def mergeSortHelper(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:
        if e - s + 1 <= 1:
            return pairs

        mid = (e + s) // 2
        self.mergeSortHelper(pairs, s, mid)
        self.mergeSortHelper(pairs, mid + 1, e)
        self.merge(pairs, s, mid, e)

        return pairs

    def merge(self, pairs: List[Pair], s: int, mid: int, e: int) -> None:
        left = pairs[s: mid + 1]
        right = pairs[mid + 1: e + 1]

        i, j, k = 0, 0, s

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                pairs[k] = left[i]
                i += 1
            else:
                pairs[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            pairs[k] = left[i] 
            k += 1
            i += 1

        while j < len(right):
            pairs[k] = right[j] 
            k += 1
            j += 1
