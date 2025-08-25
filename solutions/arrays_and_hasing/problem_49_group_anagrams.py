from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        res = defaultdict(list) #dict: key = sorted word, value = list of words
        for s in strs: # iterate each word in the input list
            sortedS = ''.join(sorted(s)) # sort letters to form a signature, e.g "eat" -> "aet"
            res[sortedS].append(s) # group original word under its signature
        return list(res.values()) # return group as a list of lists