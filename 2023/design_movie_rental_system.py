"""
https://leetcode.com/problems/design-movie-rental-system/
"""


from heapq import heappush, heappop
from collections import defaultdict


class MovieRentingSystem:

    def __init__(self, n: int, entries: list[list[int]]):
        self.unRentedMovies = {}
        self.rentedMovies = []
        self.prices = {}
        self.movies = defaultdict(list)

        for s, m, p in entries:
            self.prices[(s, m)] = p
            self.unRentedMovies[(s, m)] = True
            heappush(self.movies[m], (p, s))

    def search(self, movie: int) -> list[int]:
        if movie not in self.movies:
            return []
        
        rslt, temp = [], []
        heap = self.movies[movie]
        while len(rslt) < 5 and heap:
            p, s = heappop(heap)
            temp.append((p, s))
            if self.unRentedMovies[(s, movie)]:
                rslt.append(s)
        
        for p, s in temp:
            heappush(heap, (p, s))
        
        return rslt
        
    def rent(self, shop: int, movie: int) -> None:
        self.unRentedMovies[(shop, movie)] = False
        p = self.prices[(shop, movie)]
        heappush(self.rentedMovies, (p, shop, movie))
        

    def drop(self, shop: int, movie: int) -> None:
        self.unRentedMovies[(shop, movie)] = True
        

    def report(self) -> list[list[int]]:
        rslt = []
        while len(rslt) < 5 and self.rentedMovies:
            p, s, m = heappop(self.rentedMovies)
            if not self.unRentedMovies[(s, m)] and (not rslt or rslt[-1] != (p, s, m)):
                rslt.append((p, s, m))

        for p, s, m in rslt:
            heappush(self.rentedMovies, (p, s, m))
        
        return [[s, m] for _, s, m in rslt]

        