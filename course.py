# The canFinish method determines if all courses can be completed given a list of prerequisites, using a cycle detection approach in a directed graph.

# Initialization:
#   - 'preMap' is a dictionary mapping each course to its list of prerequisites.
#   - 'visiting' is a set used to track courses currently on the DFS path to detect cycles.

# Helper Function (dfs):
#   - Performs a depth-first search to check if a course can be completed:
#       - If a course is already in 'visiting', a cycle is detected, so return False.
#       - If a course has no prerequisites (preMap[crs] is empty), return True.
#       - Add the course to 'visiting' and recursively check all its prerequisites.
#       - If any prerequisite leads to a cycle, return False.
#       - Remove the course from 'visiting' and mark its prerequisites as cleared (preMap[crs] = []).
#       - Return True if the course and its prerequisites can be completed.

# Main Execution:
#   - Iterate through all courses and call dfs on each course.
#   - If any course results in a cycle, return False.
#   - If no cycles are detected, return True, indicating all courses can be completed.

# TC: O(n + e), where n is the number of courses and e is the number of prerequisites (edges in the graph).
# SC: O(n), due to the recursion stack and the visiting set.


from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Store all courses along the current DFS path
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                # Cycle detected
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True