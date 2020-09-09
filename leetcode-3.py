import heapq

def merge(list1, list2):
    # heap1, heap2 생성하기
    heap1 = []
    heap2 = []
    for i in list1:
        heapq.heappush(heap1, i)
    for i in list2:
        heapq.heappush(heap2, i)    
    
    heapq.heappush(heap1, 10**6+1)
    heapq.heappush(heap2, 10**6+1)
    
    result = []
    item1 = heapq.heappop(heap1)
    item2 = heapq.heappop(heap2)
    
    
    while (heap1 or heap2):
        if item1==10**6+1 and item2==10**6+1:
            break
        elif item1 > item2:
            result.append(item2)
            if heap2:
                item2 = heapq.heappop(heap2)
        elif item1 <= item2:
            result.append(item1)
            if heap1:                
                item1 = heapq.heappop(heap1)
    if item1 == 10**6+1:
        result.append(item2)
    else:
        result.append(item1)
    return result[:-1]


def merge(list1, list2):
    idx1 = 0
    idx2 = 0
    result = []
    while idx1<len(list1) or idx2<len(list2):
        if idx1<len(list1):
            item1 = list1[idx1]
        else:
            item1 = 10**6+1
        if idx2<len(list2):
            item2 = list2[idx2]
        else:
            item2 = 10**6+1
        if item1>item2:
            result.append(item2)
            idx2+=1
        else:
            result.append(item1)
            idx1+=1
    return result


def findMedian(nums1, nums2):
    merged = merge(nums1, nums2)
    if len(merged)==0:
        return 0
    elif len(merged)%2==0:
        return (merged[int(len(merged)/2)-1]+merged[int(len(merged)/2)])/2
    elif len(merged)%2==1:
        return merged[int(len(merged)/2)]
        
findMedian([1,2], [3,4,5])
