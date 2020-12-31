class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if len(points) <= K:
            return points

        return self.optimized(points, K)

    @staticmethod
    def optimized(points, K):
        return sorted(points, key=lambda x:x[0]**2+x[1]**2)[:K]

    @staticmethod
    def brute_force(points, K):
        result = []
        points_distance = []

        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]

            distance = (x ** 2 + y ** 2) ** 0.5
            point_dist = {"distance": distance, "point": [x, y]}
            points_distance.append(point_dist)

        points_distance.sort(key=lambda i: (i['distance']))

        j = 0
        for i in range(K, 0, -1):
            result.append(points_distance[j]['point'])
            j += 1

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.kClosest([[3,3],[5,-1],[-2,4]], 2))

