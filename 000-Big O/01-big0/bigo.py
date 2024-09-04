# def print_numbers(n):
#     for i in range(n+1):
#         print(i)

# print_numbers(10)

# O(n)

def print_items(n):
    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                print(i,j,k)

print_items(10)





# O(n**2) distributive property