def power(a,b):
    if not((isinstance(a,int) or isinstance(a,float)) and isinstance(b,int)):
       return "invalid input"
    if(b==1):
        return(a)
    if(b!=1):
        return(a*power(a,b-1))
if __name__ == '__main__':
    print("Result:",power(3,4))
print("Result:",power(2,3))
