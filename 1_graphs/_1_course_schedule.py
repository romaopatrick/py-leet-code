# 1. Course Schedule: https://leetcode.com/problems/course-schedule/

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = {}

        for course_couple in prerequisites:
            (course, dep) = course_couple

            if visited[dep] & course == visited[dep]:
                return False

            visited[course] = dep

        return True
