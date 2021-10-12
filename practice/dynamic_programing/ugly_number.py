from time import time
"""
    because every number can only be divided by 2, 3, 5, one way to look at the sequence is to 
    split the sequence to three groups as below: 
     (1) 1×2, 2×2, 3×2, 4×2, 5×2, 6x2, 8x2 … 
     (2) 1×3, 2×3, 3×3, 4×3, 5×3, 6x3, 8x3 … 
     (3) 1×5, 2×5, 3×5, 4×5, 5×5, 6x5, 8x5 …
     Every subsequence is the ugly-sequence itself(1, 2, 3, 4, 5, 6, 8, ...)
     Every step we get an ugly number from the 3 subsequences, and we choose the smallest one
     and move one step after.
"""
def find_nth_ugly_number(num):
    # initialize first ugly number
    ugly_number_list = [1]
    # initialize 3 array index variables to point to first element of the ugly array
    index_2, index_3, index_5 = 0, 0, 0
    next_nultiple_of_2 = ugly_number_list[index_2] * 2
    next_nultiple_of_3 = ugly_number_list[index_3] * 3
    next_nultiple_of_5 = ugly_number_list[index_5] * 5
    
    # print("next_nultiple_of_2",
    #       "next_nultiple_of_3",
    #       "next_nultiple_of_5", 
    #       "next_ugly_num")    
    for index in range(1, num):
        # get next multiple of 2, 3 and 5. Find min among them
        next_ugly_num = min(next_nultiple_of_2,
                            next_nultiple_of_3,
                            next_nultiple_of_5)
        
        ugly_number_list.append(next_ugly_num)
        if next_ugly_num == next_nultiple_of_2:
            index_2 += 1
            next_nultiple_of_2 = ugly_number_list[index_2]*2
        if next_ugly_num == next_nultiple_of_3:
            index_3 += 1
            next_nultiple_of_3 = ugly_number_list[index_3]*3
        if next_ugly_num == next_nultiple_of_5:
            index_5 += 1
            next_nultiple_of_5 = ugly_number_list[index_5]*5
        # print(next_nultiple_of_2,
        #       next_nultiple_of_3,
        #       next_nultiple_of_5, 
        #       next_ugly_num)

    return ugly_number_list[num - 1]




while True:
    try:
        n = int(input("Enter the nth value: "))
        # n = 150
        start_time = time()
        print(find_nth_ugly_number(n))
        print("Duration:", time() - start_time)
        # break
    except Exception as e:
        # print(e)
        print("quit")
        break