import math
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """   
     # tworze zmienna
        tab=[]
        tab=nums1
        tab+=nums2
        dlugosc=len(tab)
        tab.sort()
        if(dlugosc%2==0):
            miejsce1=float(dlugosc)
            miejsce1=int(math.ceil(dlugosc/2))
            miejsce2=miejsce1-1
            med=float(tab[miejsce1]+tab[miejsce2])/2
            return med
        else:
            miejsce=float(dlugosc)
            miejsce=int(math.ceil(dlugosc/2))
            med=float(tab[miejsce])
            return med