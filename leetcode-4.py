s = 'abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa'

def isPalindrome(s, left, right, memo):
    if memo[left][right]!=None:
        return memo[left][right]
    if s[left] == s[right]:
        return isPalindrome(s, left+1, right-1, memo)
    else:
        return 0
    
class Solution:
    def longestPalindrome(self, s: str) -> str:        
        
        if len(s)<=1:
            return s
        longest = s[0]
        
        length = len(s)
        memo = [[None]*length for _ in range(length)]
        for i in range(length-1):
            memo[i][i] = 1
            memo[i][i+1] = int(s[i]==s[i+1])
            
        memo[length-1][length-1] = 1
        
        
        for j in range(length):
            for k in range(j+1, length):
                result = isPalindrome(s, j, k, memo)
                memo[j][k] = result
                if result:
                    if k-j+1>len(longest):
                        longest = s[j:k+1]
        return longest
    
    
sol = Solution()
print(sol.longestPalindrome(s))

#%%


s = "cabbac"

class Solution:
    def longestPalindrome(self, s: str) -> str:        
        
        if len(s)<=1:
            return s
        longest = s[0]
        
        length = len(s)
        memo = [[None]*length for _ in range(length)]
        for i in range(length-1):
            memo[i][i] = 1
            memo[i][i+1] = int(s[i]==s[i+1])
            
        memo[length-1][length-1] = 1
        
        for j in range(length, -1, -1):
            for k in range(j+1, length):
                print(j,k)
                if s[j] == s[k]:
                    if j+1>k-1:
                        memo[j][k] = 1
                    else:
                        memo[j][k] = memo[j+1][k-1]
                    if memo[j][k] and (k-j+1 > len(longest)):
                        longest = s[j:k+1]
                else:
                    memo[j][k] = 0
        return longest
    
sol = Solution()
print(sol.longestPalindrome(s))


#%%

s = 'abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa'

class Solution(object):
   def longestPalindrome(self, s):
      dp = [[False for i in range(len(s))] for i in range(len(s))]
      for i in range(len(s)):
         dp[i][i] = True
      max_length = 1
      start = 0
      count = 0 
      for l in range(2,len(s)+1):
         for i in range(len(s)-l+1):
            count +=1
            end = i+l
            if l==2:
               if s[i] == s[end-1]:
                  dp[i][end-1]=True
                  max_length = l
                  start = i
            else:
               if s[i] == s[end-1] and dp[i+1][end-2]:
                  dp[i][end-1]=True
                  max_length = l
                  start = i
      print(count)
      return s[start:start+max_length]
ob1 = Solution()
print(ob1.longestPalindrome(s))