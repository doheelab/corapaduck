def solution(w):
    # 1. 입력이 빈 문자열인 경우
    if w == "":
        return ""
    
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리
    counted = {'(': 0, ')': 0}
    correctness = 1
    for idx in range(len(w)):
        if w[idx]=='(':
            counted['(']+=1
        elif w[idx]==')':
            counted[')']+=1
        # 올바른 문자열 체크
        if counted[')']>counted['(']:
            correctness = 0 
        # 균형잡힌 문자열 체크
        if counted['('] == counted[')']:
            break

    u = w[:idx+1]
    v = w[idx+1:]
        
    # 3. 문자열 u가 "올바른 괄호 문자열"이라면
    if correctness==1:
        return u + solution(v)
    else:
        # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면
        another = "(" + solution(v) + ")"
        another += ''.join([')' if item == '(' else '(' for item in u[1:-1]])
        return another