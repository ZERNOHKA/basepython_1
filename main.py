# Задача 1
def get_sum(a, b):
    total = a + b
    return total


# Задача 2
def count_capital_letters(text):
    count = 0
    for i in range(len(text)):
        if text[i] >= 'A' and text[i] <= 'Z':
            count = count + 1
    return count


# Задача 3
def decode_string(s):
    s_lower = s.lower()
    result = ""
    for i in range(len(s_lower)):
        c = s_lower[i]
        if s_lower.count(c) == 1:
            result = result + "("
        else:
            result = result + ")"
    return result


# Задача 4
def get_odd_count(nums):
    count = 0
    for i in range(len(nums)):
        n = int(nums[i])
        if n % 2 != 0:
            count = count + 1
    return count


# Задача 5
def check_access(has_key, has_finger, alarm, daylight):
    if alarm == True:
        return False
    if has_finger == True:
        return True
    if has_key == True:
        if daylight == True:
            return True
        else:
            return False
    return False

print("Сумма 1+2 =", get_sum(1, 2))
print("Заглавные буквы в 'Hello World' =", count_capital_letters("Hello World"))
print("Декодирование 'Success' =", decode_string("Success"))
print("Нечётные в '01234567' =", get_odd_count("01234567"))

print("Доступ 1:", check_access(True, False, False, True))
print("Доступ 2:", check_access(True, False, False, False))
print("Доступ 3:", check_access(False, True, False, False))
print("Доступ 4:", check_access(False, True, True, True))
print("Доступ 5:", check_access(True, True, False, True))
print("Доступ 6:", check_access(False, False, False, True))
