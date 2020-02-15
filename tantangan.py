def pentanacci(n):
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==1:
        return 1
    elif n==2: 
        return 1
    elif n==3: 
        return 1
    elif n==4: 
        return 1
    elif n==5: 
        return 5
    else: 
        return (pentanacci(n-1)+pentanacci(n-2)+pentanacci(n-3)+pentanacci(n-4)+pentanacci(n-5))
nilai=int(input("Masukkan angka"))
print(pentanacci(nilai))