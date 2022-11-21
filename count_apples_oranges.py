#!/bin/python3

def countApplesAndOranges(s, t, a, b, apples, oranges):
    dist_apples = [a+t for t in apples]
    dist_oranges = [b+o for o in oranges]
    count_a, count_b = 0,0
    for i in dist_apples:
        if i>=s and  i<=t:
            count_a+=1
    for j in dist_oranges:
        if j>=s and j<=t:
            count_b+=1
    print(count_a)
    print(count_b)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])
    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)
