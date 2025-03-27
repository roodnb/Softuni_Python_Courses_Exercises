def number_increment(numbers):

    def increase():
        new_nums = [ele + 1 for ele in numbers]
        # for ele in numbers:
        #     new_nums.append(ele + 1)
        return new_nums
    return increase()


print(number_increment([1, 2, 3]))