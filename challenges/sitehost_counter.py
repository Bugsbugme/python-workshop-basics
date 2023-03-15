"""
Print numbers from 1 to 100
Every multiple of 3 should print the string "Site" instead of the number
Every multiple of 5 should print the string "Host" instead of the number
If the number is a multiple of both 3 and 5, print the string "SiteHost"
"""

num = 0

while num != 100:
    num = num + 1
    if num % 3 == 0 and num % 5 == 0:
        print("SiteHost")
    elif num % 3 == 0:
        print("Site")
    elif num % 5 == 0:
        print("Host")
    else:
        print(num)
