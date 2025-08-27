class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000,}

        summ = 0
        n = len(s)
        p = 0

        while p < n:
            if p < n-1 and d[s[p]] < d[s[p+1]]: 
                summ+= d[s[p+1]]-d[s[p]]
                p+=2
            else:
                summ += d[s[p]]
                p+=1
        
        return summ
