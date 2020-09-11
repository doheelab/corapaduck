s = "cabbac"

def longestPalindrome(s):      
    
    longest = s[0]
    length = len(s)
    
    # 길이가 1이하인 경우
    if len(s)<=1:
        return s
    
    # palindromic 여부 저장
    memo = [[None]*length for _ in range(length)]
    
    # memo 채우기 (대각 성분)
    for i in range(length-1):
        memo[i][i] = 1
        memo[i][i+1] = int(s[i]==s[i+1])
        
    memo[length-1][length-1] = 1
    
    # memo 채우기 (나머지)
    for j in range(length, -1, -1):
        for k in range(j+1, length):
            # 양 끝의 문자가 같은 경우
            if s[j] == s[k]:
                if j+1>k-1:
                    memo[j][k] = 1
                else:
                    memo[j][k] = memo[j+1][k-1]
                # 가장 긴 부분문자열 발견한 경우
                if memo[j][k] and (k-j+1 > len(longest)):
                    longest = s[j:k+1]
            else:
                memo[j][k] = 0
    return longest

