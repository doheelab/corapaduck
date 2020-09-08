

s = "abcabcbb"

#%%
# Solution 1

# O(n)
def longest(s):
    count = set()
    for el in s:
        if el in count:
            return len(count)
        count.add(el)
    return len(s)

# O(n)
def lengthOfLongestSubstring(s):
    result= 0
    for i in range(len(s)):
        length = longest(s[i:])
        if result<length:
            result=length
    return result
   
lengthOfLongestSubstring(s)

#%%

# Solution 2 : O(n)
def lengthOfLongestSubstring(s):
    count = {}
    start = 0
    result = 0
    for i, elem in enumerate(s):
        if elem in count:
            if start < count[elem]+1:
                start = count[elem]+1 
        count[elem] = i
        if i-start+1>result:
            result = i-start+1
    return result

lengthOfLongestSubstring(s)
