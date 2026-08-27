class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        if not strs:
                return strs
        for word in strs:
            key="".join(sorted(word))
            groups[key]=groups.get(key,[])
            groups[key].append(word)
        return list(groups.values())
