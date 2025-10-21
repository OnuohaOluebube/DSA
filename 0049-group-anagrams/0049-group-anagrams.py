
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        resMap = collections.defaultdict(list)
        res = []
        for str in strs:
            key = [0] * 26
            for s in str:
                key[ord(s) - ord("a")] += 1
            
            resMap[tuple(key)].append(str)
        return list(resMap.values())