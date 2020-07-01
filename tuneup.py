#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

__author__ = "???"

import cProfile
import pstats
import functools
import timeit


def profile(func):
    """A cProfile decorator function that can be used to
    measure performance.
    """
    def cprofile(*args, **kwargs):
        profile = cProfile.Profile()
        try:
            ##enables timer
            profile.enable()
            ## invokes original fun and passes in all args and kwargs
            result = func(*args, **kwargs)
            ## disables timer
            profile.disable()
            return result

        finally:
            ##creat a stat object
            stats = pstats.Stats(profile)
            ## sort the stats by cumtime
            stats.sort_stats('cumulative')
            ##print stats
            stats.print_stats()
    return cprofile
    # Be sure to review the lesson material on decorators.
    # You need to understand how they are constructed and used.
    # raise NotImplementedError("Complete this decorator function")


def read_movies(src):
    """Returns a list of movie titles."""
    movie_dictionary={}
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        for movie in f.read().splitlines():
            if movie not in movie_dictionary:
                movie_dictionary[movie] = 1
            else:
                movie_dictionary[movie] += 1
    return movie_dictionary
    


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list."""
    movies = read_movies(src)
    duplicates = []
    # while movies:
    #     movie = movies.pop()
    #     if is_duplicate(movie, movies):
    #         duplicates.append(movie)
    # return duplicates
    for movie in movies:
        if movies[movie] > 1:
            duplicates.append(movie)
    return duplicates
            


def timeit_helper():
    """Part A: Obtain some profiling measurements using timeit."""
    # YOUR CODE GOES HERE
    t = timeit.Timer(stmt="find_duplicate_movies('movies.txt')",
    setup="from tuneup import find_duplicate_movies")
    result = t.repeat(repeat=7, number=5)
    return min(result) / 5

def main():
    """Computes a list of duplicate movie entries."""
    result = find_duplicate_movies('movies.txt')
    print(f'the best time from 7 repeats of 5 runs per repeat: {timeit_helper()} seconds.')
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))


if __name__ == '__main__':
    main()
