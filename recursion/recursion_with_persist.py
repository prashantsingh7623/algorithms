arr=  []
def fact(n: int) -> list:
    if n < 2: return 1
    result = n * fact(n-1)
    arr.append(result)
    return result

# def fact(n: int):
#     if n < 2: return 1
#     return n * fact(n-1)

n = 4
tot = fact(n)
print(tot)
print(arr)
# print('arr : {}'.format(arr))