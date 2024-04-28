import math
class Sorter:

      def BubbleSort(self,target,desc):
        if(desc):
          for i in range(0,len(target)):
               for j in range(1,len(target)-i):
                    if target[j-1]<target[j]:
                         target[j],target[j-1]=target[j-1],target[j]
          return target
        else:
             for i in range(0, len(target)):
                  for j in range(1, len(target) - i ):
                       if target[j - 1] > target[j]:
                            target[j], target[j - 1] = target[j - 1], target[j]
             return target



