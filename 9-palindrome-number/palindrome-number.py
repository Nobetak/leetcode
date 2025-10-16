class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x1=str(x)
        x2=x1[::-1]
        if(x2==x1):
            return True
        else:
            return False

        