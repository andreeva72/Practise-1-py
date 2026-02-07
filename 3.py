
A = True # Сегодня идет дождь
B = False # На улице холодно

conjunction = A and B 
disjunction = A or B 
negation_A = not A
implication = not A or B 

print(f"A: {A}, B: {B}"),
print(f"A и B: {conjunction}")
print(f"A или B: {disjunction}")
print(f"нe A: {negation_A}")
print(f"A влечет B: {implication}")
