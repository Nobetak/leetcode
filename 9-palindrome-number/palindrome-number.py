class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        palindrom=str(x)
        palindrom1=palindrom[::-1]
        if(palindrom==palindrom1):
            return True
        else:
            return False

        