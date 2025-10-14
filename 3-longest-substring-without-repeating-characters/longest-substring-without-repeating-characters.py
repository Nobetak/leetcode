class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        widziane={}
        start=0
        mwielkosc=0
        for index, wartosc in enumerate(s):
            if(wartosc in widziane):
                if(widziane[wartosc]>=start):
                    start=widziane[wartosc]+1
            if(mwielkosc<=(index-start+1)):
                mwielkosc=(index-start+1)
            widziane[wartosc]=index
        return mwielkosc