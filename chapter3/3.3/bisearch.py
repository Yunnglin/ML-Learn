from collections import defaultdict


def bisearch_right(arr,target):
    left,right = 0, len(arr)-1
    while left < right:
        mid = left + right + 1 >> 1
        if arr[mid]<=target:
            # 不断移动左端点
            left = mid
        else:
            right = mid - 1
    return right

def bisearch_left(arr,target):
    left,right = 0, len(arr)-1
    while left < right:
        mid = left + right >> 1
        if arr[mid]>=target:
            # 不断移动右端点
            right = mid
        else:
            left = mid + 1
    return left

arr = [5,7,7,10]
target = 4
left = bisearch_left(arr,target)
right = bisearch_right(arr,target)
print(left)
print(right)

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 时间戳单增，可使用二分法
        self.store = defaultdict(list)
    
    def bisearch(self,arr,target):
        left,right = 0, len(arr)-1
        while left<=right:
            mid = left + (right-left) // 2
            if arr[mid][1]>=target:
                right = mid-1
            else:
                left = mid+1
        return left            


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # 不存在
        if key not in self.store:
            return ''
        # 无该timestamp前的记录
        arr = self.store[key]
        if arr[0][1] > timestamp:
            return ''
        if arr[-1][1] <= timestamp:
            return arr[-1][0]
        # 二分查找
        index = self.bisearch(arr,timestamp)
        return arr[index][0]
        
        

# # Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(*["love","high",10])
# obj.set(*["love","low",20])
# p1 = obj.get(*["love",5])
# p2 = obj.get(*["love",10])
# p3 = obj.get(*["love",15])
# print(p1)
# print(p2)