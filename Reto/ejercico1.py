def rearrange_and_filter(nums, S):


    filtered_nums = []

    for num in nums:


        num_str = str(num)
        filtered_num_str = ""

        for digit_char in num_str:


            digit = int(digit_char)

            if digit < S:

                filtered_num_str += digit_char

        if filtered_num_str:

            filtered_nums.append(int(filtered_num_str))


    result = sorted(filtered_nums, reverse=True)

    return result



print(rearrange_and_filter([1, 2, 3, 4, 5, 6], 8))
print(rearrange_and_filter([10, 20, 30, 40], 8))
print(rearrange_and_filter([6], 8))
print(rearrange_and_filter([66], 8))
print(rearrange_and_filter([65], 8))
print(rearrange_and_filter([6, 2, 1], 8))
print(rearrange_and_filter([60, 6, 5, 4, 3, 2, 7, 7, 29, 1], 8))
