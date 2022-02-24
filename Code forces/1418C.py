# You and your friend are playing the game Mortal Kombat XI. You are trying to pass a challenge tower.
# There are n bosses in this tower, numbered from 1 to n.
# The type of the i-th boss is ai.
# If the i-th boss is easy then its type is ai=0, otherwise this boss is hard and its type is ai=1.
#
# During one session, either you or your friend can kill one or two bosses (neither you nor your friend can skip the session, so the minimum number of bosses killed during one session is at least one).
# After your friend session, your session begins, then again your friend session begins, your session begins, and so on.
# The first session is your friend's session.
#
# Your friend needs to get good because he can't actually kill hard bosses.
# To kill them, he uses skip points. One skip point can be used to kill one hard boss.
#
# Your task is to find the minimum number of skip points your friend needs to use so you and your friend kill all n bosses in the given order.
#
# For example: suppose n=8, a=[1,0,1,1,0,1,1,1]. Then the best course of action is the following:
#
# your friend kills two first bosses, using one skip point for the first boss;
# you kill the third and the fourth bosses;
# your friend kills the fifth boss;
# you kill the sixth and the seventh bosses;
# your friend kills the last boss, using one skip point, so the tower is completed using two skip points.
# You have to answer t independent test cases.

# solution:
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))+[0,0]
    dp=[(0,0)]*(n+2)
    for i in range(n-1,-1,-1):
        dp[i]=(min(dp[i+1][1],dp[i+2][1]),min(dp[i + 1][0]+x[i], dp[i + 2][0]+x[i]+x[i+1]))
    print(dp[i][1])

