# You are given a list of (website, user) pairs that represent users visiting websites. Come up with a program that identifies the top k pairs of websites with the greatest similarity

# E.g. k = 1, list of tuples:
# [('google.xcom', 1), ('google.com', 3), ('google.com',5),
# ('pets.com',1), ('pets.com',2), ('yahoo.com',6),
# ('yahoo.com',2), ('yahoo.com',3), ('yahoo.com',4), ('yahoo.com',5),
# ('wikipedia.org',4), ('wikipedia.org',5), ('wikipedia.org',6),
# ('wikipedia.org',7), ('bing.com',1), ('bing.com',3), ('bing.com',5),
# ('bing.com',6)]

# to compute the similarity between two websites you should ompute the number of users they have in common divided by the number of users who have visited either site in total (Jaccard index)

# E.g. We conclude that google.com and bing.com are the most similar with a score of 3/4 = 0.75

from collections import defaultdict
from itertools import combinations

# O(m) time complexity
def compute_sim(a,b,visitors):
    return len(visitors[a].intersection(visitors[b])) / len(visitors[a].union(visitors[b]))

# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
# O(n^2*m) time to iterate through all possible pairs
# O(n^2) space domainated by the visitors dictionary. similarities dictionary also has space complexity of O(n^2)
def top_pairs(logs,k):
    visitors = defaultdict(set)
    similarities = {}

    for domain, user in logs:
        visitors[domain].add(user)
    
    sites = list(visitors.keys())
    pairs = combinations(sites,2)

    for pair in pairs:
        similarities[pair] = compute_sim(pair[0],pair[1], visitors)
        print(pair, similarities[pair])
    
    # sort takes O(nlog(n))
    result = sorted(similarities, key=similarities.get, reverse=True)
    return (result[:k])

# O(n^2) space and O(m^2*n) time complexity
# space complexity dominated by the visitors dictionary
# improved space complexity as it uses a heap instead of an additional dictionary similarities
# save the time of sorting too since the heap with fixed size k maintains the 
# Whenever you are asked to find the top k or minimum k values, a heap should be the first thing that comes to mind. 
import heapq
def top_pairs_1(logs,k):
    visitors = defaultdict(set)
    for domain, user in logs:
        visitors[domain].add(user)
    pairs = []
    sites = list(visitors.keys())

    for _ in range(k):
        heapq.heappush(pairs, (0,('','')))

    # when the heap is full, it will automatically pop the 
    for i in range(len(sites)-1):
        for j in range(i+1, len(sites)):
            score = compute_sim(sites[i], sites[j], visitors)
            # heappushpop maintains the size of the heap to be k, headppushpop add the new score to the heap while pop the pairs with smallest score
            heapq.heappushpop(pairs, (score, (sites[i],sites[j])))
    print(pairs)
    return [pair[1] for pair in pairs]

if __name__ == "__main__":
    logs = [('google.com', 1), ('google.com', 3), ('google.com',5),
    ('pets.com',1), ('pets.com',2), ('yahoo.com',6),
    ('yahoo.com',2), ('yahoo.com',3), ('yahoo.com',4), ('yahoo.com',5),
    ('wikipedia.org',4), ('wikipedia.org',5), ('wikipedia.org',6),
    ('wikipedia.org',7), ('bing.com',1), ('bing.com',3), ('bing.com',5),
    ('bing.com',6)]

    k = 5
    print(top_pairs(logs, k))
    print("------------------")
    print(top_pairs_1(logs,k))
