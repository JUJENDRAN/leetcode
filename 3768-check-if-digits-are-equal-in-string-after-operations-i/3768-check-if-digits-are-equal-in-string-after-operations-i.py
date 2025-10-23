class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return False
        
        arr = []
        for i in s:
            arr.append(int(i))
        
        while len(arr) > 2:
            temp = []
            for i in range(len(arr) - 1):
                temp.append((arr[i] + arr[i+1]) % 10)
            arr = temp
        
        return arr[0] == arr[1]