class Solution(object):
    def twoSum(self, nums, target):
        List={} #dictionary slownik gdzie 1 wartosc odpowiada 2 np mim:23
        tablica=[] 
        tablica=nums
        for index, wartosc in enumerate(tablica):
            roznica=target-wartosc
            if(roznica in List):
                return [List[roznica],index]
            List[wartosc]=index          


        