#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import defaultdict

class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		anagrams_dict = defaultdict(list)
		for s in strs:
			count = [0] * 26
			for c in s:
				count[ord(c) - ord('a')] += 1 #retrieves index coresponding  
				                                                  # asscii letter
			key = tuple(count)
			anagrams_dict[key].append(s)

		return anagrams_dict.values()  
# @lc code=end

