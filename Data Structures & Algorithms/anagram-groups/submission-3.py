class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = 0
        groups = {}
        while n < len(strs):
            newstr = strs[n]
            key = tuple(sorted(newstr))

            if key not in groups:
                groups[key] = []
            groups[key].append(newstr)
            n += 1
        return list(groups.values())