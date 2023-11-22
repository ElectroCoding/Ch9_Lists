# find_max


def find_max(nums):
    max_so_far = float("-inf")
    # max = nums[0]

    for i in range(0, len(nums)):

        if nums[i] > max_so_far:
            max_so_far = nums[i]
    return max_so_far


attack_points = [-1, -1, -1]

# print(attack_points[0])


max = find_max(attack_points)

print(f"Max attack points was {max}") 

