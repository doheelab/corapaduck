# -*- coding: utf-8 -*-
"""
2020 KAKAO BLIND RECRUITMENT 문자열 압축 풀이
"""

def compress(word, n):
    result = ""
    while len(word)>0:
        count = 1
        
        # 비교하기
        while word[(count-1)*n:count*n] == word[count*n:(count+1)*n] and len(word)>0: 
            count += 1
            
        # count가 1 이상인 경우
        if count > 1:
            result += str(count) + word[:n]
            word = word[n*count:]

        # count가 1인 경우
        else:
            result += word[:n]
            word = word[n:]
            
    return len(result)


def solution(word):

    # 길이가 1인 경우
    if len(word)==1:
        return 1
    
    length = len(word)
    shortest = len(word)
    
    # 길이 1부터 length//2까지 확인
    for n in range(1, length//2+1):
        current = compress(word, n)
        if current < shortest:
            shortest = current
    
    return shortest