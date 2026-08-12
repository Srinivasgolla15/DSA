class Solution(object):
    def carFleet(self, target, position, speed):

        # Sort cars by position from closest to target
        # to farthest from target.

        # cars = []
        # for i in range(len(position)):
        #     cars.append([position[i], speed[i]])  ORR
        cars = list(zip(position, speed))

        cars.sort(reverse=True)

        stack = []

        for car in cars:

            # pos = car[0]
            # spd = car[1]

            # Time needed to reach the target
            time = (target - car[0]) / float(car[1])

            # No fleet yet OR this car cannot catch
            # the fleet in front.
            if not stack or time > stack[-1]:
                stack.append(time)

            # Otherwise, this car catches the fleet
            # in front and becomes part of that fleet.

        return len(stack)