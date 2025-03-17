def logical_pahase(n):
    change ={
        500:0,
        100:0,
        50:0,
        20:0,
        10:0,
        5:0,
        2:0,
        1:0
    }
    balence=[]
    if n>=500:
        change.update({500:n//500})
        n=n%500
    if n>=100:
        change.update({100:n//100})
        n=n%100
    if n>=50:
        change.update({50:n//50})
        n=n%50
    if n>=20:
        change.update({20:n//20})
        n=n%20
    if n>=10:
        change.update({10:n//10})
        n=n%10
    if n>=5:
        change.update({5:n//5})
        n=n%5
    if n>=2:
        change.update({2:n//2})
        n=n%2
    if n>=1:
        change.update({1:n//1})
    return change    
if __name__ =="__main__":
    Currency = int(input("Enter the amount :"))
    print("the required change is ",logical_pahase(Currency))