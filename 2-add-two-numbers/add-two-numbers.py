# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        Li1=l1
        Li2=l2
        tab=ListNode()
        obecny=tab
        zmienna=0
        while Li1 or Li2:
            value1=Li1.val if Li1 else 0
            value2=Li2.val if Li2 else 0
            suma=value1+value2+zmienna
            zmienna=0
            if suma>=10: 
                zmienna=int(str(suma)[0])
                suma-=zmienna*10
                obecny.next=ListNode(suma)
                obecny=obecny.next 
            else:
                obecny.next=ListNode(suma)
                obecny=obecny.next
            if Li1: Li1=Li1.next
            if Li2: Li2=Li2.next    
        if(zmienna!=0):
            obecny.next=ListNode(zmienna)
        return tab.next

            


        