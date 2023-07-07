def isThereSubsetSum(arr,sum):
    if sum == 0 or sum < 1:
        return False
    elif len(arr) == 0:
        return False
    else:
        if arr[0] == sum:
            #return [arr[0]]
            return True
        else:
            with_v = isThereSubsetSum(arr[1:],(sum - arr[0])) 
            if with_v:
                #return [arr[0]] + with_v
                return True
            else:
                return isThereSubsetSum(arr[1:],sum)
            
def giveSubsetSum(arr,sum,result):
    if sum == 0 or sum < 1:
        return []
    elif len(arr) == 0:
        return []
    else:
        if arr[0] == sum:
            result[-len(arr)] = 1
            return [arr[0]]
        else:
            with_v = giveSubsetSum(arr[1:],(sum - arr[0]),result) 
            if with_v:
                result[-len(arr)] = 1
                return [arr[0]] + with_v
            else:
                return giveSubsetSum(arr[1:],sum,result)

# prints every multiset of size a with integers between 0 and b that sums to m while not containing a subset that sums to p
def print_all_sum(m, a, b, p):
    result = []
    print_all_sum_rec(m, a, b, p, 0, 1, result, a)

def print_all_sum_rec(m, a, b, p, current_sum, start, result, max_size):
    if current_sum == m:
        if len(result) == a and not isThereSubsetSum(result, p):
            print(result)
    for i in range(start, b+1):
        temp_sum = current_sum + i
        if temp_sum <= m and max_size > 0:
            result.append(i)
            print_all_sum_rec(m, a, b, p, temp_sum, i, result, max_size-1)
            result.pop()
        else:
            return