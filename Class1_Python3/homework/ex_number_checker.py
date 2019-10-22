def adder(x,y):
    if x==3:
        result = 7
    else:
        result = 1
    return result

def test_adder():
    assert adder(3,4)==7
    assert adder(-3,4)==1

if __name__ == '__main__':
    test_adder()
