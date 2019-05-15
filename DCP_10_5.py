# topological sort
# We are given a hashmap associating each sourseId key with a list of sourceIds value, which tells us that the prerequisites of courseId are courseIds. 
# Return a sorted ordering of courses such that we can complete the curriulum

# E.g. 
# {
#     'CSC300':['CSC100', 'CSC200']
#     'CSC200':['CSC100']
#     'CSC100':[]

# }

# Output: ['CSC100', CSC200', 'CSC300]

# Make each course a vertex and draw an edge from course A to course B if A is a prerequisite for B.
# The problem becomes one of traversing this directed graph in order to efficiently find out which verticies come before other ones
# topological sort, there can be more than one topological sorting for a graph
# topological sort is a linear ordering of its nodes in which each node comes before all nodes to which it has outbound edges. Every Directed Acyclic Graph (DAG) has one or more topological sorts

# O(V+E) time due to dfs
# O(V) space for result, O(E) for all the prerequisites relationships
from collections import defaultdict, deque
# course_to_prereqs is the input dictionary
def find_order(course_to_prereqs):
    # python set has remove time complexity of O(N)
    course_to_prereqs = {c:set(p) for c, p in course_to_prereqs.items()}

    # start off to-do list with all courses without prerequisites
    # bfs, start taking course where there is no prerequesite
    # the condition of adding a course to todo is this course has prerequiste fulfilled already
    todo = deque([c for c, p in course_to_prereqs.items() if not p])
    
    # create a new data structure to map prereqs to successor courses
    # from course-prereqs mapping to prereqs-course mapping
    # the graph is represented by adjacency list (python dictionary)
    prereq_to_courses = defaultdict(list)
    for course, prereqs in course_to_prereqs.items():
        for prereq in prereqs:
            prereq_to_courses[prereq].append(course)

    result = []
    
    while todo:
        prereq = todo.popleft()
        result.append(prereq)

        # iterate the courses that depend on current course (prereq)
        for c in prereq_to_courses[prereq]:
            # remove prereq from course_to_prereqs mappings since we already taken prereq (prereq being added into the result)
            course_to_prereqs[c].remove(prereq)
            # if course c (course needs to be taken after current prereq) has no other dependencies, we will add this course to todo deque
            if not course_to_prereqs[c]:
                todo.append(c)
    
    # circular dependencies, length of result shall be equal to number of course in the input dictionary
    if len(result) < len(course_to_prereqs):
        return None

    return result

if __name__ == "__main__":
    course_to_prereqs = {
            'CSC300':['CSC100', 'CSC200'],
            'CSC200':['CSC100'],
            'CSC100':[]
            }
    
    print(find_order(course_to_prereqs))