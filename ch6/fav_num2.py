fav_num = {
    'bob': [69,12], 'frank': [23,90], 'sarah': [42,712],
}

for name, nums in fav_num.items():
    print(f"{name.title()}'s favorite numbers are: ")
    for num in nums:
        print(num)