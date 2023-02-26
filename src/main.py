from const import MAIN_MENU, GOODS_MENU


def start():
    while True:
        print(MAIN_MENU)
        try:
            choice = int(input())
            if choice == 0:
                break
            elif choice == 1:
                while True:
                    print(GOODS_MENU)
                    choice = int(input())
                    if choice == 0:
                        break
                    if choice == 1:
                        print(1)
                    else:
                        print('Select a number from the suggested')
            elif choice == 2:
                print(2)
            elif choice == 3:
                print(3)
            else:
                print('Select a number from the suggested')
        except ValueError:
            print('Choice must be number. Try again')


if __name__ == '__main__':
    start()
