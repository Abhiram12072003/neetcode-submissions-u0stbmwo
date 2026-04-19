class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = [(p,s) for p,s in zip(position,speed)]
        ans = 0
        ps.sort(reverse=True)
        fleets = 1
        prevTime = (target-ps[0][0])/ps[0][1]
        for i in range(1,len(ps)):
            currCar = ps[i]
            currTime = (target-currCar[0])/currCar[1]
            if currTime > prevTime:
                fleets += 1
                prevTime = currTime
        return fleets 