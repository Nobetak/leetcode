class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def czypalindrom(x):
            odwroconyx=x[::-1]
            if(x==odwroconyx):
                return x
            else: 
                return ""
        maksymalna=""
        for i in  range(len(s)):
            for j in range(i+1,len(s)+1):
                zmienna=s[i:j]
                if(zmienna==zmienna[::-1]):
                    if(len(maksymalna)<len(zmienna)):
                        maksymalna=zmienna
        return maksymalna