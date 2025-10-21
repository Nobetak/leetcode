class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""

        najdluzszy_palindrom = ""
        
        # Funkcja pomocnicza do rozszerzania od środka
        def rozszerz_od_srodka(lewy, prawy):
            while lewy >= 0 and prawy < len(s) and s[lewy] == s[prawy]:
                lewy -= 1
                prawy += 1
            # Zwraca znaleziony palindrom
            return s[lewy + 1:prawy]

        # Iteracja przez każdy znak jako potencjalny środek
        for i in range(len(s)):
            # Palindrom o nieparzystej długości (środek to s[i])
            palindrom_nieparzysty = rozszerz_od_srodka(i, i)
            if len(palindrom_nieparzysty) > len(najdluzszy_palindrom):
                najdluzszy_palindrom = palindrom_nieparzysty

            # Palindrom o parzystej długości (środek między s[i] i s[i+1])
            palindrom_parzysty = rozszerz_od_srodka(i, i + 1)
            if len(palindrom_parzysty) > len(najdluzszy_palindrom):
                najdluzszy_palindrom = palindrom_parzysty
        
        return najdluzszy_palindrom
