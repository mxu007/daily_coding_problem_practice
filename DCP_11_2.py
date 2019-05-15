# Disjoint-set data structure
# a classroom consists of n students, whose friendships can be represented in an adjacency list
# E.g. 
# {
#     0:[1,2],
#     1:[0,5],
#     2:[0],
#     3:[6],
#     4:[],
#     5:[1],
#     6:[3]
# }

# each student can be placed in a friend group, which can be defined as the transitive closure of that student's friendship relations. In other words, this is the smallest set such that no student in the group has any friends outside this group

# Given a friendship list, determine the number of friends groups in the class

# output: {0,1,2,5}, {3,6}, {4}
# https://www.youtube.com/watch?v=0jNmHPfA_yE
# https://www.youtube.com/watch?v=VHRhJWacxis

# O(n) space to store the group membership of n students
# O(1) time for find and union operation, (E) time where E is number of edges represented in the adjacency list, 
class DisjointSet:
    def __init__(self,n):
        # at initialization, each student (represented by index from 0 to n-1) having n groups with only themselves in each group, every node is a root node themselves
        # enable us to construct array-based union find
        # the index of the sets (which is a list) represent the student index
        # the value at each index represents the group membership of that student
        self.sets = list(range(n))
        # the sizes for each group
        self.sizes = [1] * n
        # no.of total groups
        self.count = n

    # discover the current group of x, if index of student does not equal to the group number, keep doing group = self.sets[group] until we find the membership (the node index equals the value, which indicating the membership)
    # O(1) time complexity
    def find(self,x):
        # group that x currently belongs
        group = self.sets[x]
        # until self loop is reached
        while group != self.sets[group]:
            group = self.sets[group]
        
        # update the membership info of x, stores at the list with index x
        # path compression, O(1) lookup once we perform the compression before
        self.sets[x] = group
        return group
    
    # O(1) time complexity for update the membership
    def union(self, x, y):
        x, y = self.find(x), self.find(y)

        # if x and y are currently not in the same group, assign them to the same group
        # assign students from the smaller set to the arger set
        if x != y:
            # after swap, x belongs to a larger group
            if self.sizes[x] < self.sizes[y]:
                x, y = y, x
            
            # assume x belongs to a larger group
            # merge group y belongs to into x
            self.sets[y] = x
            self.sizes[x] += self.sizes[y]
            # reduce the count of total groups
            self.count -= 1

# For each friendship in the input, call union methods to place the students in the same set
def friend_groups(students):
    groups = DisjointSet(len(students))

    for student, friends in students.items():
        for friend in friends:
            groups.union(student, friend)

    return groups.count


if __name__ == "__main__":
    students = {
                0:[1,2],
                1:[0,5],
                2:[0],
                3:[6],
                4:[],
                5:[1],
                6:[3]
                }
    
    print(friend_groups(students))