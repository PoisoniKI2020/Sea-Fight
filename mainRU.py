# -*- coding: utf-8 -*-
import socket

win ="""╔╗╔╗╔╦══╦╗─╔╗
║║║║║╠╗╔╣╚═╝║
║║║║║║║║║╔╗─║
║║║║║║║║║║╚╗║
║╚╝╚╝╠╝╚╣║─║║
╚═╝╚═╩══╩╝─╚╝"""
def decode(x):
    return x.decode("utf-8")

def encode(x):
    return x.encode("utf-8")

def check(s):
    if(not inp[0:-2].isdigit()):
        print("Некорректные кординаты")
        return False
    if(not inp[0:-2].isdigit()):
        print("Некорректные кординаты")
        return False
    return True
def cout_mt(two = True):
    print("  a b c d e f g h i j", end = "")
    if(two):
        print("    a b c d e f g h i j", end = "")
    print()
    for i in range(10):
        if(i == 9):
            print(i + 1, end = "")
        else:
            print(i + 1, end = " ")
        for j in range(10):
            if mt[i][j] == -3:
                print("*", end = " ")
            elif mt[i][j] == -2:
                print("#", end = " ")
            elif mt[i][j] == 0:
                print("С", end = " ")
            elif mt[i][j] > 0 and mt[i][j] < 3:
                print("Д", end = " ")
            elif mt[i][j] > 2 and mt[i][j] < 6:
                print("И", end = " ")
            elif mt[i][j] >= 6:
                print("Р", end = " ")
            else:
                print("_", end = " ")
        if(two):
            print("  ", end = "")
            if(i == 9):
                print(i + 1, end = "")
            else:
                print(i + 1, end = " ")
            for j in range(10):
                if mt2[i][j] == -1:
                    print("_", end = " ")
                elif mt2[i][j] == 0:
                    print("*", end = " ")
                elif mt2[i][j] == 1:
                    print("#", end = " ")
        print()
ships = []
mt = []
mt2 = []
for i in range(10):
    mt.append([-1] * 10)
    mt2.append([-1] * 10)

now_id = 0

for i in range(1):
    while(True):
        inp = input("Расположите свою Космическую Станцию (размер 4 клетки)")
        x = int(inp[0:-2]) - 1
        y = (ord(inp[-2]) - ord("a"))
        v = inp[-1]
        if(x > 9 - 3 or x < 0 or y > 9 - 3 or y < 0):
            print("Введённые кординаты вне поля")
            continue
        if(v == "h"):
            if(mt[x][y] + mt[x][y + 1] + mt[x][y + 2] + mt[x][y + 3] == -4):
                mt[x][y] = now_id
                mt[x][y + 1] = now_id
                mt[x][y + 2] = now_id
                mt[x][y + 3] = now_id
                now_id += 1
                break
            else:
                print("Корабли пересекаются!")
                continue
        else:
            if(mt[x][y] + mt[x + 1][y] + mt[x + 2][y] + mt[x + 3][y] == -4):
                mt[x][y] = now_id
                mt[x + 1][y] = now_id
                mt[x + 2][y] = now_id
                mt[x + 3][y] = now_id
                now_id += 1
                break
            else:
                print("Корабли пересекаются!")
                continue
    ships.append(4)
    cout_mt(False)
for i in range(0):
    while(True):
        inp = input("Расположите свой Дредноут (размер 3 клетки)")
        x = int(inp[0:-2]) - 1
        y = ord(inp[-2]) - ord("a")
        v = inp[-1]
        if(x > 9 - 2 or x < 0 or y > 9 - 2 or y < 0):
            print("Введённые кординаты вне поля")
            continue
        if(v == "h"):
            if(mt[x][y] + mt[x][y + 1] + mt[x][y + 2] == -3):
                mt[x][y] = now_id
                mt[x][y + 1] = now_id
                mt[x][y + 2] = now_id
                now_id += 1
                break
            else:
                print("Корабли пересекаются!")
                continue
        else:
            if(mt[x][y] + mt[x + 1][y] + mt[x + 2][y] == -3):
                mt[x][y] = now_id
                mt[x + 1][y] = now_id
                mt[x + 2][y] = now_id
                now_id += 1
                break
            else:
                print("Корабли пересекаются!")
                continue
    ships.append(3)
    cout_mt(False)
for i in range(0):
    while(True):
        inp = input("Расположите свой Звёздный Истребитель (размер 2 клетки)")
        x = int(inp[0:-2]) - 1
        y = ord(inp[-2]) - ord("a")
        v = inp[-1]
        if(x > 9 - 1 or x < 0 or y > 9 - 1 or y < 0):
            print("Введённые кординаты вне поля")
            continue
        if(v == "h"):
            if(mt[x][y] + mt[x][y + 1] == -2):
                mt[x][y] = now_id
                mt[x][y + 1] = now_id
                now_id += 1
                break
            else:
                print("Корабли пересекаются!")
                continue
        else:
            if(mt[x][y] + mt[x + 1][y] == -2):
                mt[x][y] = now_id
                mt[x + 1][y] = now_id
                now_id += 1
                break
            else:
                print("Корабли пересекаются!")
                continue
    ships.append(2)
    cout_mt(False)
for i in range(0):
    while(True):
        inp = input("Расположите свой Разведчик (размер 1 клетки)")
        x = int(inp[0:-2]) - 1
        y = ord(inp[-2]) - ord("a")
        v = inp[-1]
        if(x > 9 or x < 0 or y > 9 or y < 0):
            print("Введённые кординаты вне поля")
            continue
        if(v == "h"):
            if(mt[x][y] == -1):
                mt[x][y] = now_id
                now_id += 1
                break
            else:
                print("Корабли пересекаются!")
                continue
        else:
            if(mt[x][y] == -1):
                mt[x][y] = now_id
                now_id += 1
                break
            else:
                print("Корабли пересекаются!")
                continue
    ships.append(1)
    cout_mt(False)

role = input("Кем вы будете? (S - Сервер, C - Клиент)")
match_end = False
if(role == "S"):
    socket1 = socket.socket()
    socket1.bind(('', 9090))
    print(socket.gethostbyname(socket.gethostname()))
    print("Сообщите клиенту IP-адрес\nОжидание подключения")
    socket1.listen(1)
    conn, addr = socket1.accept()
    print("Клиент подключён")
    while(True):
        answer = "1"
        while(answer == "1" or answer == "2"):
            ok = False
            while(not ok):
                attack = input("Выберите клетку в которую будете бить")
                if(not check(attack)):
                    continue
                x = int(inp[0:-2]) - 1
                y = ord(inp[-2]) - ord("a")
                if(x > 9 or x < 0 or y > 9 or y < 0):
                    print("Введённые кординаты вне поля")
                    continue
                elif mt2 != -1:
                    print("Вы уже стреляли в эту точку")
                    continue
                else:
                    ok = True
            conn.send(encode(attack))
            print("Ожидаем результат")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                answer = decode(data)
                break
            if(answer == "0"):
                mt2[x][y] = 0
                print("Мимо!")
            if(answer == "1"):
                mt2[x][y] = 1
                print("Попал!")
            if(answer == "2"):
                mt2[x][y] = 1
                print("Взорвал!")
            if(answer == "3"):
                mt2[x][y] = 1
                print("Взорвал!\nПобеда!")
                print(win)
                match_end = True
                break
        if(match_end):
            break
        our_ans = 1
        while(our_ans == 1 or our_ans == 2):
            quest = ""
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                quest = decode(data)
                break
            x = int(quest[0:-1]) - 1
            y = ord(quest[-1]) - ord("a")
            if(mt[x][y] >= 0):
                ships[mt[x][y]] -= 1
                if sum(ships) == 0:
                    conn.send(encode("3"))
                    our_ans = 3
                    print("Наш корабль взорвали!\nПоражение")
                    break
                    match_end = True
                elif(ships[mt[x][y]] == 0):
                    our_ans = 2
                    conn.send(encode("2"))
                    print("Наш корабль взорвали!")
                else:
                    our_ans = 1
                    conn.send(encode("1"))
                    print("Наш корабль подбили!")
                mt[x][y] = -2
            else:
                mt[x][y] = -3
                conn.send(encode("0"))
                our_ans = 0
                print("Противник промахнулся!")
            cout_mt()
        if(match_end):
            break
    conn.close()
else:
    sock = socket.socket()
    ip = input("Введите IP-Адрес")
    sock.connect((ip, 9090))
    print("Подключено")
    while(True):
        our_ans = 1
        while(our_ans == 1 or our_ans == 2):
            quest = ""
            data = sock.recv(1024)
            quest = decode(data)
            x = int(quest[0:-1]) - 1
            y = ord(quest[-1]) - ord("a")
            if(mt[x][y] >= 0):
                ships[mt[x][y]] -= 1
                if sum(ships) == 0:
                    sock.send(encode("3"))
                    our_ans = 3
                    print("Наш корабль взорвали!\nПоражение")
                    match_end = True
                elif(ships[mt[x][y]] == 0):
                    our_ans = 2
                    print("Наш корабль взорвали!")
                    sock.send(encode("2"))
                else:
                    our_ans = 1
                    print("Наш корабль подбили!")
                    sock.send(encode("1"))
                mt[x][y] = -2
            else:
                mt[x][y] = -3
                our_ans = 0
                print("Противник промахнулся!")
                sock.send(encode("0"))
            cout_mt()
        if(match_end):
            break
        answer = "1"
        while(answer == "1" or answer == "2"):
            ok = False
            while(not ok):
                attack = input("Выберите клетку в которую будете бить")
                if(not check(attack)):
                    continue
                x = int(inp[0:-2]) - 1
                y = ord(inp[-2]) - ord("a")
                if(x > 9 or x < 0 or y > 9 or y < 0):
                    print("Введённые кординаты вне поля")
                    continue
                elif mt2 != -1:
                    print("Вы уже стреляли в эту точку")
                    continue
                else:
                    ok = True
            sock.send(encode(attack))
            print("Ожидаем результат")
            data = sock.recv(1024)
            answer = decode(data)
            if(answer == "0"):
                mt2[x][y] = 0
                print("Мимо!")
            if(answer == "1"):
                mt2[x][y] = 1
                print("Попал!")
            if(answer == "2"):
                mt2[x][y] = 1
                print("Взорвал!")
            if(answer == "3"):
                mt2[x][y] = 1
                print("Взорвал!\nПобеда!")
                print(win)
                match_end = True
    sock.close()
input("Выход...")
