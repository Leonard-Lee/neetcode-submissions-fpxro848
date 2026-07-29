class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            
            # If the digit is less than 9, just add 1 and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # If the digit is 9, adding 1 makes it 10, so it becomes 0 
            # and the loop continues to carry the 1 to the next digit
            digits[i] = 0
            
        # If the loop finishes without returning, all digits were 9 (e.g., [9, 9, 9])
        # We need to prepend a 1 at the beginning
        return [1] + digits
        