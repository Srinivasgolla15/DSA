class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
# -----------------2D DP TLE---------------
# Time  : O(2^n)
# Space : O(n)


        # n = len(stations)

        # def dfs(station_index, current_position, current_fuel):

        #     # We can already reach the target
        #     if current_position + current_fuel >= target:
        #         return 0

        #     # No more stations
        #     if station_index == n:
        #         return float('inf')

        #     station_position, station_fuel = stations[station_index]

        #     # Distance from current position to this station
        #     distance = station_position - current_position

        #     # Cannot reach this station
        #     if current_fuel < distance:
        #         return float('inf')

        #     # Fuel left after reaching the station
        #     remaining_fuel = current_fuel - distance

        #     # Choice 1: Don't refuel
        #     skip = dfs(
        #         station_index + 1,
        #         station_position,
        #         remaining_fuel
        #     )

        #     # Choice 2: Refuel
        #     take = 1 + dfs(
        #         station_index + 1,
        #         station_position,
        #         remaining_fuel + station_fuel
        #     )

        #     # Take the choice requiring fewer stops
        #     return min(skip, take)

        # answer = dfs(0, 0, startFuel)

        # return -1 if answer == float('inf') else answer



        heap = []
        currfuel = startFuel
        currpos = 0
        count = 0

        # Treat target like a final station with 0 fuel
        stations.append([target, 0])

        for station, stationgas in stations:

            distance = station - currpos

            # Keep refueling until we can reach this station
            while currfuel < distance:

                if not heap:
                    return -1

                currfuel += -heapq.heappop(heap)
                count += 1

            # We can reach the station
            currfuel -= distance
            currpos = station

            # Store its fuel for future use
            heapq.heappush(heap, -stationgas)

        return count