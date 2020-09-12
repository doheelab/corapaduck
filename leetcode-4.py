


s = "PAYPALISHIRING"
numRows = 3 
# 'PAHNAPLSIIGYIR'

s = "PAYPALISHIRING"
numRows = 4
# 'PINALSIGYAHRPI'

def convert(s):
    
    if len(s)<=2 or numRows==1:
        return s
            
    result = []
    length = len(s)
    
    # 첫번째 줄    
    i = 0
    while 1+2*(numRows-1)*i<=length:
        result.append(1+2*(numRows-1)*i)
        i+=1

    for j in range(2, numRows):
        
        # 첫번째 숫자
        if j <= length:
            result.append(j)
        else:
            break
        
        # 번갈아 더할 숫자들의 리스트
        add_list = [2*(numRows-j), 2*(j-1)]
        
        # 번갈아가며 더해주기
        i = 0
        while j+add_list[i%2]<=length:
            result.append(j+add_list[i%2])
            j += add_list[i%2]
            i+=1

    # 마지막 줄            
    i = 0
    while numRows+2*(numRows-1)*i<=length:
        result.append(numRows+2*(numRows-1)*i)
        i+=1

    return ''.join([s[i-1] for i in result])