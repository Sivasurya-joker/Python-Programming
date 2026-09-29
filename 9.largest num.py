# Direct method 
nums = [20, 40, 60, 80, 100]
print("Largest:", max(nums))

# Indirect method 
lar = nums[0]
for n in nums:
    if n > lar:
        lar = n
print("Largest:", lar)