class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        rows=[[] for _ in range(numRows)]
        row=0
        direction=1
        result=""
        for ch in s:
            rows[row].append(ch)
            if row==numRows-1:
                direction=-1
            if row==0:
                direction=1
            row+=direction
        for r in rows:
            result+="".join(r)
        return result