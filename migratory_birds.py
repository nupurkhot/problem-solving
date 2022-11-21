#!/bin/python3

# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.

def migratoryBirds(arr):
    id_lst, count_lst = [],[]
    for i in set(arr):
        cnt = arr.count(i)
        id_lst.append(i)
        count_lst.append(cnt)
    mx_cnt = max(count_lst)
    max_id_lst = []
    for cnt in count_lst:
        if cnt == mx_cnt:
            idx = count_lst.index(cnt) 
            max_id_lst.append(id_lst[idx])   
    return min(max_id_lst)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
