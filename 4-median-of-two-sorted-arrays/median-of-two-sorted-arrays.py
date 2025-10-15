import math
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """   
        med=0.0 #tworze zmienna do zwrocenia wyniku
        tab=[] #tworze tablice
        tab=nums1 #dodaje do jednej tablicy 2 inne
        tab+=nums2
        dlugosc=len(tab) #zczytuje dlugosc poloczanych tablic
        tab.sort() #funkcja sortujaca tablice
        if(dlugosc%2==0): #jezeli dlugosc nie ma reszty tak jak w matmie
            miejsce1=float(dlugosc) #zamieniam liczbe na zmiennoprzecinkowa
            miejsce1=int(math.ceil(dlugosc/2)) # bo tutaj by mi wyszlo zle
            miejsce2=miejsce1-1 # i odejmuje 1 od tego aby znac srodeklisty
            med=float(tab[miejsce1]+tab[miejsce2])/2 # obliczan mediane
            return med #zwracam mediane 
        else:
            miejsce=float(dlugosc) #to samo tylko ze tutaj obliczam
            miejsce=int(math.ceil(dlugosc/2)) #dla tablicy o wielkosc 3,5..
            med=float(tab[miejsce])
            return med