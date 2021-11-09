from random import*
from keyboard import *
def start():
    """Делаем выбор с кем будем играть.
    Возвращаем М параметр 
    
    :rtype: int
    """
    print("Давай сыграем в игру выбери: Камень , ножницы или бумагу.")
    print()
    suk=0
    while suk not in [1,2,3]:
        try:
            suk=int(input("Ты хочешь сыграть с роботом или с другом или посмотреть фильм робот с роботом  => ") ) 
        except TypeError:
            print("Можно только 1 или 2 или 3!")
    return suk

def bot_vs_bot(b:list,g:list):
    """Игра роботов
    Показывает на экране имя
    :param list b: список для первого работа
    :param list g: список для второго работа
    :rtype: int
    """
    bot=0
    gamer=0
    nic=0
    god=0
    b=0
    while True:
        print("Ты хочешь продолжить смотреть за битвой (Нажми backspace) или закочить (Нажми enter)?")
        print()
        try:
            if read_key()=="backspace":
                print()
                print("Продолжаем просмотр.")
                print()
                pass
        except:
             ValueError
        try:
            if read_key()=="enter":
                 print()
                 print("Спасибо за просмотр!")
                 print()
                 print()
                 print(f"Ничьих было {nic} , Побед у первого робота было {gamer} , Побед у второго робота было {bot}.")
                 break
        except:
              ValueError
        b = randint(1,3)
        g = randint(1,3)
        print()
        if b == 1:
            print("Робот 1 выбрал камень.")
            print()
        elif b == 2:
            print("Робот 1 выбрал ножницы.")
            print()
        elif b == 3:
            print("Робот 1 выбрал бумагу.")
            print()
        if g== 1:
            print("Робот 2 выбрал камень.")
            print()
        elif g == 2:
            print("Робот 2 выбрал ножницы.")
            print()
        elif g == 3:
            print("Робот 2 выбрал бумагу.")
            print()
        if b==g:
            print("Ничья")
            nic+=1
        elif b==1 and g==2 or b==2 and g==3 or b==3 and g==1:
            gamer+=1
            print("Выиграл робот 1")
        elif b==1 and g==3 or b==2 and g==1 or b==3 and g==2:
            bot+=1
            print("Выиграл робот 2")

def igrok_vs_igrok(c:list,b:list):
    """ Игорк с игроком
    """
    bot=0
    gamer=0
    nic=0
    god=0
    while True:
        print("Ты хочешь продолжить (Нажми backspace) или закочить (Нажми enter)?")
        print()
        try:
             if read_key()=="backspace":
                print()
                print("Продолжаем игру.")
                print()
                pass
        except:
                ValueError
        try:
            if read_key()=="enter":
                print()
                print("Спасибо за игру!")
                print()
                print(f"Ничьих было {nic} , Побед у первого игрока {gamer} , Побед у второго игрока было {god}.")
                break
        except:
                ValueError
        c=0
        while c not in [1,2,3] :
            try:
                c=int(input("1 - камень, 2 - ножницы, 3 - бумага. "))
            except TypeError:
                print("Можно только 1,2,3!")
            print()
            if c == 1:
                print("Вы выбрали камень.")
                print()
            elif c == 2:
                print("Вы выбрали ножницы.")
                print()
            elif c == 3:
                print("Вы выбрали бумагу.")
                print()
        b=0
        while b not in [1,2,3] :
            try:
                b=int(input("1 - камень, 2 - ножницы, 3 - бумага. "))
            except TypeError:
                print("Можно только 1,2,3!")
            print()
            if b == 1:
                print("Игрок 2 выбрал камень.")
                print()
            elif b == 2:
                print("Игрок 2 выбрал ножницы.")
                print()
            elif b == 3:
                 print("Игрок 2 выбрал бумагу.")
                 print()
        if b==c:
            print("Ничья")
            print()
            nic+=1
        elif b==1 and c==2 or b==2 and c==3 or b==3 and c==1:
            gamer+=1
            print("Выиграл игрок 1")
        elif b==1 and c==3 or b==2 and c==1 or b==3 and c==2:
            god+=1
            print()
            print("Выиграл игрок 2")
def bot_vs_igrok(b:list,g:list):
    bot=0
    gamer=0
    nic=0
    god=0
    while True:
        print("Ты хочешь продолжить (Нажми backspace) или закочить (Нажми enter)?")
        print()
        try:
             if read_key()=="backspace":
                print()
                print("Продолжаем игру.")
                print()
                pass
        except:
                ValueError
        try:
            if read_key()=="enter":
                print()
                print("Спасибо за игру!")
                print()
                print()
                print(f"Ничьих было {nic} , Побед у игрока {gamer} , Побед у робота было {bot}.")
                break
        except:
                ValueError
        c=0
        while c not in [1,2,3] :
            try:
                c=int(input("1 - камень, 2 - ножницы, 3 - бумага. "))
            except TypeError:
                print("Можно только 1,2,3!")
            print()
            if c == 1:
                print("Вы выбрали камень.")
                print()
            elif c == 2:
                print("Вы выбрали ножницы.")
                print()
            elif c == 3:
                print("Вы выбрали бумагу.")
                print()
            b = randint(1,3)
            print()
            if b == 1:
                print("Компьютер выбрал камень.")
                print()
            elif b == 2:
                print("Компьютер выбрал ножницы.")
                print()
            elif b == 3:
                 print("Компьютер выбрал бумагу.")
                 print()
        if b==c:
            print("Ничья")
            print()
            nic+=1
        elif b==1 and c==2 or b==2 and c==3 or b==3 and c==1:
            gamer+=1
            print("Выиграл игрок 1")
            print()
        elif b==1 and c==3 or b==2 and c==1 or b==3 and c==2:
            bot+=1
            print()
            print("Выиграл Робот")