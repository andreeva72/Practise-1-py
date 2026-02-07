A = False # Сегодня идет дождь
В = True # Я взял с собой зонт

stay_dry = (not A) or B

if stay_dry: 
    print ("Мы останемся сухими.")
else:
    print( "Мы промокнем.")