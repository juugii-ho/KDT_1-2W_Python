# ----------------------------------------------------------
# 다양한 리스트 생성
# ----------------------------------------------------------
# 실수 데이터로 구성된 리스트 생성
floatNums = [4., 3.1, 6.3, 5.01]

# str 데이터로 구성된 리스트 생성
strNums = ['44', '56', '98']

# bool 데이터로 구성된 리스트 생성
boolNums = [False, False, True, True, True]

# 다양한 데이터 타입으로 구성된 리스트 생성
nums = ['100', 98, False, 7.12, 'Apple', True, 7>6]

print(floatNums, strNums, boolNums, nums)
# [4.0, 3.1, 6.3, 5.01] ['44', '56', '98'] [False, False, True, True, True] ['100', 98, False, 7.12, 'Apple', True, True]
# 빈 리스트 생성
nums = []
print(nums) #[]

# 리스트 안에 리스트로 구성된 리스트 생성
nums = [10, 20, "한글", ['A', 'B'], boolNums, 200, 10.0]
#        0   1   2       3          4       5    6
print(nums) # [10, 20, 30, ['A', 'B'], [False, False, True, True, True], 200, 100]

# 리스트의 요소 출력
print(f'nums[0] => {nums[0]}, {type(nums[0])}')
print(f'nums[1] => {nums[1]}, {type(nums[1])}')
print(f'nums[2] => {nums[2]}, {type(nums[2])}')
print(f'nums[3] => {nums[3]}, {type(nums[3])}')
print(f'nums[4] => {nums[4]}, {type(nums[4])}')
print(f'nums[5] => {nums[5]}, {type(nums[5])}')
print(f'nums[6] => {nums[6]}, {type(nums[6])}')

# B만 가져오려면?(3번의 1번)
print(f'nums[3][1] => {nums[3][1]}, {type(nums[3][1])}')

data = [1, [ [1,2,3], 'A']]
# 라고 했을 때 1차원은 [1, [ [1,2,3], 'A']]
#           2차원은 [ [1,2,3], 'A']
#           3차원은 [1,2,3]