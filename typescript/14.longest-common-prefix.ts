/*
 * @lc app=leetcode id=14 lang=typescript
 *
 * [14] Longest Common Prefix
 */

// @lc code=start
function longestCommonPrefix(strs: string[]): string {
    // Handle edge cases
    if (strs.length === 0) return "";
    if (strs.length === 1) return strs[0];

    // Take the first string as the prefix
    let prefix = strs[0];

    // Iterate through the remaining strings
    for (let i = 1; i < strs.length; i++) {
        // Keep reducing prefix until it matches
         while (strs[i].indexOf(prefix) !== 0) {
            prefix =prefix.slice(0, prefix.length - 1);
            // If prefix becomes empty, return ""
            if (prefix.length === 0) return "";
         }
    }

    return prefix;
   
    
};
// @lc code=end

