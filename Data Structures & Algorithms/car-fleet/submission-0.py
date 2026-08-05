class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []
        n = len(position)
        for i in range(n):
            cars.append([position[i],speed[i]])

        cars.sort()
        stack = []

        for i in range(n-1,-1,-1):
            pos = cars[i][0]
            speed = cars[i][1]

            time = (target-pos)/speed

            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)