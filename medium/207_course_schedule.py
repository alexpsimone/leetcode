def canFinish(numCourses, prerequisites) -> bool:

    # 3, [[0,1][1,2]] --> True
    # 4, [[0,1][2,3]] --> True
    # 2, [[0,1][1,0]] --> False
    # 2, [[4,2]] --> True
    # 1, [[0,1][1,0]] --> False
    # 2, [[0,1][0,2][1,0]] --> False

    # if you find a cycle, then any node with a value in that cycle is unreachable
    # goal: to count the num edges NOT in a cycle
    # then compare that num to numCourses, return True/False

    # create an adjacency dict: {prereq: course }



    pass

if __name__ == '__main__':
    canFinish(numCourses, prerequisites)