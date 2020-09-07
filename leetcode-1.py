def twoSum(nums, target):
    # key: target-현재값, value: 현재 인덱스
    residual = {}
    for idx in range(len(nums)):
        current = nums[idx]
        # 저장된 나머지와 일치하는 경우
        if current in residual:
            return [residual[current], idx]
        # 각 원소를 target에서 뺀 나머지를 저장
        residual[target-current] = idx
        