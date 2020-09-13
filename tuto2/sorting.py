def sorting(num):
    num.sort()
    return num

sortedNum=[]
num=[2,5,1,3,4]
sortedNum=sorting(num)
print("Sort in Ascending")
for i in range(len(sortedNum)):
    print(int(sortedNum[i]))