#problem Statment:
# n people gathered in a room with m tables (n≥2m). They want to play the Hat k times. Thus, k games will be played at each table. Each player will play in k games.
#
# To do this, they are distributed among the tables for each game. During each game, one player plays at exactly one table. A player can play at different tables.
#
# Players want to have the most "fair" schedule of games. For this reason, they are looking for a schedule (table distribution for each game) such that:
#
# At any table in each game there are either ⌊nm⌋ people or ⌈nm⌉ people (that is, either n/m rounded down, or n/m rounded up). Different numbers of people can play different games at the same table.
# Let's calculate for each player the value bi — the number of times the i-th player played at a table with ⌈nm⌉ persons (n/m rounded up). Any two values of bimust differ by no more than 1. In other words, for any two players i and j, it must be true |bi−bj|≤1.
# For example, if n=5, m=2 and k=2, then at the request of the first item either two players or three players should play at each table. Consider the following schedules:
#
# First game: 1,2,3 are played at the first table, and 4,5 at the second one. The second game: at the first table they play 5,1, and at the second  — 2,3,4. This schedule is not "fair" since b2=2 (the second player played twice at a big table) and b5=0 (the fifth player did not play at a big table).
# First game: 1,2,3 are played at the first table, and 4,5 at the second one. The second game: at the first table they play 4,5,2, and at the second one  — 1,3. This schedule is "fair": b=[1,2,1,1,1] (any two values of bi differ by no more than 1).
# Find any "fair" game schedule for n people if they play on the m tables of k games.
#
# Input
# The first line of the input contains an integer t (1≤t≤104) — the number of test cases in the test.
#
# Each test case consists of one line that contains three integers n, m and k (2≤n≤2⋅105, 1≤m≤⌊n2⌋, 1≤k≤105) — the number of people, tables and games, respectively.
#
# It is guaranteed that the sum of nk (n multiplied by k) over all test cases does not exceed 2⋅105.
#
# Output
# For each test case print a required schedule  — a sequence of k blocks of m lines. Each block corresponds to one game, a line in a block corresponds to one table. In each line print the number of players at the table and the indices of the players (numbers from 1 to n) who should play at this table.
#
# If there are several required schedules, then output any of them. We can show that a valid solution always exists.
#
# You can output additional blank lines to separate responses to different sets of inputs.

# solution
import math
for _ in range(int(input())):
    n,m,k=map(int,input().split())
    bigger=math.ceil(n/m)
    last=0
    for __ in range(k):
        for ___ in range(n%m):
            print(bigger,end=' ')
            for ____ in range(bigger):
                print(last%n+1,end=' ')
                last+=1
            print('')
        temp=last
        for ___ in range(m-n%m):
            print(n//m,end=' ')
            for ____  in range(n//m):
                print(temp%n+1,end=' ')
                temp+=1
            print('')
