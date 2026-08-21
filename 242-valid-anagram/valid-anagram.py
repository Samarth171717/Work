class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen={}
        for ch in s:
            seen[ch]=seen.get(ch,0)+1

        seen1={}
        for ch in t:
            seen1[ch]=seen1.get(ch,0)+1
            
        if seen1==seen:
            return True
        return False

    

        