class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)
        l = 0
        r = n-1
    
        for i in range (n/2):
            if l==r:
                return s
            else:
                temp = s[l]
                s[l] = s[r]
                s[r] = temp
                l+= 1
                r+= -1

