class Solution:
    def addDigits(self, num: int) -> int:
        while num>9:
            sm = 0
            while num:
                sm+= num%10
                num = num//10
            num = sm
        return num
        
