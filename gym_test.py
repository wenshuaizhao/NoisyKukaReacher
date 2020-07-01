
def test():
    for i in range(10):
        print(i)
        if i>=5:
            break
    print('Has skipped this loop!')

    return i

if __name__=='__main__':

    n=test()
    print(n)


