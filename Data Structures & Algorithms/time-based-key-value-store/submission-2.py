class TimeMap:

    def __init__(self):
       self.d = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            self.d[key]["ts"].append(timestamp)
            self.d[key]["val"].append(value)
        else:
            self.d[key] = {"ts" : [timestamp], "val": [value]}

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        xi = self.d[key]["ts"]
        xi2 = self.d[key]["val"]
        # print(self.d,xi, xi2, timestamp)
        low = 0
        high = len(xi)-1
        if xi[low] > timestamp:
            return ""
        while low<=high:
            mid = (low+high)//2
            if xi[mid]<=timestamp:
                low = mid + 1
            else:
                high = mid - 1
        return xi2[high]