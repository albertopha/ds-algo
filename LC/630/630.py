import heapq

class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        if len(courses) == 1:
            return 1
        
        # Sort by the end time
        courses.sort(key=lambda course: course[1])
        
        time = 0
        pq = [] # priority queue (max heap)
        
        for course in courses:
            if time + course[0] <= course[1]:
                time += course[0]
                heapq.heappush(pq, -course[0])
            elif pq and -pq[0] > course[0]:
                # https://leetcode.com/problems/course-schedule-iii/discuss/286526/Python-O(nlogn)-Patient-Sort
                # If 1's condition does not meet, we cannot take te course.
                #However, we should not just stop here. We should think:
                #Did we make a silly decision before? Maybe the current course's length
                # is pretty short, but the deadline is late, and we took some course with
                # earlier deadline but longer course length. For example,
                # we have course schedule: [[3,3], [2,4], [2,4]], if we take the [3,3] course,
                # we can not take the two [2,4] course any more. And obviously,
                # taking the [3,3] course is a silly decision. So we do the follwing:
                # If we previously took a course with length longer than the current course,
                # we withdraw that course and take this one. (Well, "withdraw" means cnt -= withDrawnCourseLength)
                time += course[0] + heapq.heappop(pq)
                heapq.heappush(pq, -course[0])
        
        # print(pq)
        return len(pq)
