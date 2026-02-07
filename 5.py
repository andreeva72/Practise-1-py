def de_morgan_and(A, B):
    "Возвращаем результат"
    return not (A and B)

def de_morgan_or(A, B):
    "Возвращаем результат"
    return not (A or B)

def law_of_de_morgan(A, B):
    left_side1 = de_morgan_and (A, B)
    right_side1 = (not A) or (not B)
    left_side2 = de_morgan_or(A, B)
    right_side2 = (not A) and (not B)

    return (left_side1 == right_side1, left_side2 == right_side2)

# Таблица истинности
for A in [True, False]:
    for B in [True, False]:
        result1 = de_morgan_and(A, B)
        result2 = (not A) or (not B)

        result3 = de_morgan_or(A, B)
        result4 = (not A) and (not B)

        comparison1 = result1 == result2
        comparison2 = result3 == result4

print(f"{A}\t{B}\t{result1}\t\t{result2}\t\t{result3}\t\t{result4}\t\t{comparison1}\t{comparison2}")