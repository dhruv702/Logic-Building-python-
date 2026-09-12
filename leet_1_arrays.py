# leet code 1 (array)
# 1. condition:- take an arays of elements andtake the target variqable as input.
# after it in the output get the those two array elementt whose sum = target variable value

# input:- arr=[5,3,2,4,7,6,8,1] ,target=9
# output:- [9,2]

class TowSum:
    def __init__(self,array,target):
        self.array=array
        self.target=target

    def sum(self):
        arr=self.array
        arr_target=self.target
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                sum=arr[i]+arr[j]
                if sum!=arr_target:
                    continue
                else:
                    print(f"the elements are:[{i},{j}]")
                    break

arr_input=[5,3,2,4,7,6,8,1,9]
target_input=int(input("Enter the target value"))

sum1=TowSum(arr_input,7)
sum1.sum()
