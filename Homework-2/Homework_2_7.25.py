# John Rick Santillan                 ID# 1910045



def exact_change(user_total):
    dollar = user_total // 100
    user_total = user_total % 100
    quarter = user_total // 25
    user_total = user_total % 25
    dime = user_total // 10
    user_total = user_total % 10
    nickel = user_total // 5
    user_total = user_total % 5
    penny = user_total // 1
    return dollar,quarter,dime,nickel,penny
def main():
    inputval = int(input())
    numdollars,numquarters,numdimes,numnickles,numpennies = exact_change(inputval)
    if inputval <=0:
        print('no change')
    else:
        if numdollars == 1:
            print(numdollars, 'dollar')
        if numdollars > 1:
            print(numdollars, 'dollars')
        if numquarters == 1:
            print(numquarters, 'quarter')
        if numquarters > 1:
            print(numquarters, 'quarters')
        if numdimes == 1:
            print(numdimes, 'dime')
        if numdimes > 1:
            print(numdimes, 'dimes')
        if numnickles == 1:
            print(numnickles, 'nickel')
        if numnickles > 1:
            print(numnickles, 'nickels')
        if numpennies == 1:
            print(numpennies, 'penny')
        if numpennies > 1:
            print(numpennies, 'pennies')


if __name__ =='__main__':
    main()