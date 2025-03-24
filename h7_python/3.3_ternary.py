condition = True


if condition:
    answer = "Да"
else:
    answer = "Нет"
# ternary-operator
answer = "Да" if condition else "Нет"


# Practice
age = int(input('Введите возраст посетителя: '))
price_ticket = 20 if age >= 18 else 8
print(f"Цена билета составит {price_ticket} тугриков")
