nums = set(map(int, input("Enter numbers: ").split()))
print(f"Unique numbers: {nums}")
print(f"Count={len(nums)}, Sum={sum(nums)}, Avg={sum(nums)/len(nums):.2f}, Max={max(nums)}, Min={min(nums)}")