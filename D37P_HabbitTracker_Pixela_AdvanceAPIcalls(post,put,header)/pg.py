nums = [3, 3, 4]
target = 6

dicti = {}

for i in range(len(nums)):
    dicti[] = i
    complement = target - nums[i]
    print(dicti)
    if complement in dicti.keys():
        j = dicti[complement]
        print([i, j])