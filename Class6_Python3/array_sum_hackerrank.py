#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):

    summe = 0
    for number in ar:
        summe += number
    return summe

def test_simpleArraySum():
    assert simpleArraySum([1,2,3]) == 6
    assert simpleArraySum([100, 200, 50]) == 350
    assert simpleArraySum([1, 10, 100, 2, 20, 200, 3000]) == 3333


if __name__ == '__main__':
    test_simpleArraySum()
    print("Success")