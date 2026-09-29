def rendu_yenkutal(nums, target):
    # dictionary use pannuvom -> number : index
    seen = {}
    for i, num in enumerate(nums):
        needed = target - num
        if needed in seen:
            return [seen[needed], i]  # pair found
        seen[num] = i   # current number store panrom
    return []  # pair kidaikkala
