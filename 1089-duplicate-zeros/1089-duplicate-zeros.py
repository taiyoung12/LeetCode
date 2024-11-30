class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        original = len(arr)
        index = 0

        while index < original:
            if arr[index] == 0:
                arr[::] = arr[:index+1] + [0] + arr[index+1:-1]
                if len(arr) > original :
                    arr.pop(-1)
                index+=2
            else:
                index+=1