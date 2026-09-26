import random
import time

# Список букв, из которых будем выбирать
letters = ['ц', 'е', 'д', 'з', 'и', 'п']

print("Запуск бесконечного рандомайзера букв... (Для остановки нажмите Ctrl + C)")

# Бесконечный цикл while
while True:
    # Выбираем одну случайную букву из списка
    random_letter = random.choice(letters)
    
    # Принтуем её в консоль
    print(random_letter)
    
    # Делаем паузу в 0.5 секунды, чтобы ловить логи глазами
    time.sleep(0.5)
