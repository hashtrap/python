import math

class Sorter:


    def MergeSort(self,target,left,right):
        if len(target)>1:
            mid=math.floor((right+left)/2)
            arr1=[0]*(mid-1)
            print(len(arr1))


sort=Sorter()
arr=[1,3,2]

sort.MergeSort(arr,right=0,left=len(arr)-1)