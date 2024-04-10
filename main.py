# Count the decimal places of a Float in Python

my_float = 3.14567

# ✅ Count decimal places in a float
count_after_decimal = str(my_float)[::-1].find('.')
print(count_after_decimal)  # 👉️ 5