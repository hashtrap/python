class Sorter:

    # Method for doing a bubble sort in descending or ascending order
    def BubbleSort(self, target, desc):
        if (desc):
            for i in range(0, len(target)):
                for j in range(1, len(target) - i):
                    if target[j - 1] < target[j]:
                        target[j], target[j - 1] = target[j - 1], target[j]
            return
        else:
            for i in range(0, len(target)):
                for j in range(1, len(target) - i):
                    if target[j - 1] > target[j]:
                        target[j], target[j - 1] = target[j - 1], target[j]

            return