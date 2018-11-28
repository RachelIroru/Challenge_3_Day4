def compute_sum(list1):
    if not isinstance(list1, list):
        return 'Wrong input'
    mysum=0
    for a in list1:
        if isinstance(a,int):
            mysum+=a

        elif isinstance(a,list):
            mysum+=compute_sum(a)
        
    return mysum

if __name__ == '__main__':
    print(compute_sum(['3',4,[2,3]]))
