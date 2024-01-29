def plusMinus(arr):
    # Write your code here
    positive = 0
    negative = 0
    zero = 0
    denominator = 0
    
    for item in arr:
        denominator += 1
        if item == 0:
            zero += 1
        elif item < 0:
            negative += 1
        elif item > 0:
            positive +=1
    
    f_positive = float(positive / denominator)
    f_negative = float(negative / denominator)
    f_zero = float(zero / denominator)
    print(f_positive)
    print(f_negative)
    print(f_zero)
    
    
test = [9,6,5,-1,-3,0]

plusMinus(test)