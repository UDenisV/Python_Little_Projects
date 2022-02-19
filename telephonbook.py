import argparse
book = {"Masha": 89778881539, "Pasha": 89778081476, "Natasha": 89771231536}

parser = argparse.ArgumentParser(description='Telephon book')
parser.add_argument('-a', "--add", dest="param1")
parser.add_argument('-d', "--delete", dest="param2")
parser.add_argument('-s', "--show", dest="param3", default="all")

args = parser.parse_args()

while True:
    #добавить
    if args.param1:
        name, tele = args.param1.split(":")
        if name in book:
            book[name] = [book.get(name), int(tele)]
            print("Контакт с именем ", name, " обновлён")
            print(name, ":", book[name])
            print(book)
            break
        else:
            book[name] = int(tele)
            print("Контакт с именем ", name, " добавлен")
            print(name, ":", book[name])
            print(book)
            break
    #удалить
    elif args.param2:
        name = args.param2
        if name == "all":
            print("Словарь успешно очищен")
            book.clear()
            print(book)
            break
        elif name in book:
            print("Контакт с именем ", name, " удален")
            del book[name]
            print(book)
            break
        else:
            print("Ошибка! Контакт с именем ", name, " не найден")
            break
    #вывод
    elif args.param3:
        name = args.param3
        if name == "all":
            print(book)
            break
        elif name in book:
            print(book.get(name, 0))
            break
        else:
            print("Ошибка! Контакт с именем ", name, " не найден")
            break