#affix zeroes
def zeroes(a,b,n):
    
    for i in range(a,b+1):
        num_str = str(i)
        num_len = len(num_str)
        affixzeroes = n - num_len

        if affixzeroes > 0 :
            num_str = '0'*affixzeroes + num_str
        print(num_str,end = ',')
            
# main area

a = int(input("Enter the start value(a):"))
b = int(input("Enter the end value(b):"))
n = int(input("Enter the desired length :"))

zeroes(a,b,n)