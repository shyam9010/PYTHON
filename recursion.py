def number(k):
    if k > 0:
        # print(k)
        result = k + number(k - 1)
        print(result)
    else:
        result = 0
    return result


number(10)
