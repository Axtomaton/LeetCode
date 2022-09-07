


def Dict(nums, target): #Return indexes
    Dictionary = {}
    for i in range(len(nums)):
        Dictionary[nums[i]] = i
    for i in range(len(nums)):
        Other_term = target - nums[i]
        if Other_term in Dictionary.keys():
            return i, Dictionary[Other_term]


def main():
    nums = [1, 5, 6, 7]
    print (Dict(nums, 11))




if __name__ == "__main__":
    main()