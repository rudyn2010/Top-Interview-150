class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Map each course to a prereq list
        preMap = { i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)
            
        #visitSet = all courses along the curr DFS path
        visitedSet = set()
        def dfs(course):
            if course in visitedSet:
                return False
            if preMap[course] == []:
                return True
            
            visitedSet.add(course)
            for pre in preMap[course]:
                if not dfs(pre): return False
            visitedSet.remove(course)
            preMap[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course): return False
        return True