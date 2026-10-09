

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strs:
            counts = [0] * 26
            for s in string:
                i = ord(s) - ord('a')
                counts[i] += 1 
            groups[tuple(counts)].append(string)
            
        
        return [group for counts, group in groups.items()]

            
        