# name = input("Ismingiz nima?: ")
# age = int(input(f"Salom, {name.title()}. Yoshingiz nechida?: "))
# height = float(input("Bo'yingiz necha metr?: "))

# print(f"Mening ismim {name.title()}, yoshim {age} da, bo'yim {height}m")

# num = 1
# while num <= 5:
#     print(num, end=" ")
#     num = num + 1

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Yaxshi korgan kitobingizni kirting: "
# savol = savol + "Dasturni tugatish uchun 'stop' deb yozing: "

# oson versiya
# qiymat = ""
# while qiymat.lower() != "exit" and qiymat.lower() != "chiqish":
#     qiymat = input(savol)
#     if qiymat.lower() != "exit" and qiymat.lower() != "chiqish":
#         print(float(qiymat)  2)

# Flag versiya
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == "exit" or qiymat == "chiqish":
#         ishora = False
#     else:
#         print(float(qiymat)  2)

# Break versiya

# while True:
#     qiymat = input(savol)
#     if qiymat.lower() == "exit" or qiymat.lower() == "chiqish":
#         break
#     else:
#         print(float(qiymat)  2)

# nums = list(range(1, 11))
# for num in nums:
#     if num == 5:
#         break
#     print(num  2)

# nums = list(range(1, 11))
# for num in nums:
#     if num == 5:
#         continue
#     print(num)

# num = 0

# while num < 10:
#     num += 1
#     if num % 2 != 0:
#         continue
#     else:
#         print(num)


# 1. Foydalanuvchidan yaxshi ko'rgan kitoblarini 
# kiritishni so'rang. Foydalanuvchi stop so'zini 
# yozishi bilan dasturni to'xtating.

# savol = "Yaxshi korgan kitobingizni kirting: "
# savol = savol + "Dasturni tugatish uchun 'stop' deb yozing: "
# kitoblar  = []
# while True:
#     qiymat = input(savol)
#     if qiymat == "stop":
#         print(kitoblar)
#         break
#     else:
#         kitoblar.append(qiymat)
        
# age_prompt = "Yoshingizni kiriting: "
# while True:
#     age_input = input(age_prompt)
#     if age_input == 'exit' or age_input == 'chiqish':
#         break
#     age = int(age_input)

#     if age < 7:
#         narx = 2000
#     elif 7 <= age < 18:
#         narx = 3000
#     elif 18 <= age < 65:
#         narx = 10000
#     else:
#         narx = 0 
    
#     if narx == 0:
#         print("sizga bepul")
#     else:
#         print(f"Chipta narxi {narx} som")

ismlar = []
print("Yaqin dostingizni royxatinni tuzamiz.")

n = 1

while True:
    savol = f"{n}-dostingizni ismini kiriting: "
    ism = input(savol)
    ismlar.append(ism)
    jovob = input("Yana ism qoshasizmi? (ha/yoq): ")
    if jovob == 'ha':
        n += 1
    else:
        print(ismlar)
        break

