# siyahi=[]
# def bolunen(x,y):
#     for i in range(x,y):
#         if i%6==0:
#             siyahi.append(i)
#     print(siyahi)
# x=int(input("x-i daxil edin:"))
# y=int(input("y-i daxil edin:"))
# bolunen(x,y)

# #lambda 

# def square(n):
#     return n*n

# print(square(5))

# square=lambda n:n*n
# print(square(6))

# numbers = [1,2,3,4,5]

# squared_numbers = list(map(lambda n: n*n, numbers))


# check_prime_numbers() -> list funksiyasını yazın .input() vasitəsilə 6 tam ədəd daxil edin, 
# lambda funksiyası istifadə edərək yalnız sadə ədədləri seçib siyahı şəklində qaytarsın.
sadeededler=[]

def check_prime_numbers():
    
    numbers = []
    for _ in range(6):
        num = int(input("Tam ədəd daxil edin: "))
        numbers.append(num)
        
    for num in numbers: 
        count=0
        for x in range(1, num+1):
            if num % x == 0:
                count += 1
        if count == 2:
            sadeededler.append(num)
            
    return sadeededler
                
        


print(check_prime_numbers())



