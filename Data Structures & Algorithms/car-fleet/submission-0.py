class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
      carInfo = [(p, s) for p,s in zip(position, speed)]  
      carInfo.sort(reverse=True)
      timesStack = []
      
      for p, s in carInfo:
        time = (target- p)/ s
        if not timesStack or time > timesStack[-1]:
            timesStack.append(time)
    

      return len(timesStack)