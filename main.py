#life_zone - функция которая буждет выяснять средний радиус обитаемой зоны вокруг звезды
#pyramid- функция которая находит объем усеченной пирамиды с изначальными значениями площади верхнего и нижнего основания и высоту 


import life_zone as lz
import pyramid as pyr


def main():
    user_choise = int(input("CHOISE 1 if you want find out the average radius of the habitable zone around the star \n CHOISE 2 if you want the volume of the truncated pyramid"))
    if user_choise == 1:
        lz.main()
    elif user_choise == 2:
        pyr.main()
    else:
        print("!!!!ВЫ ВВЕЛИ НЕВЕРНОЕ ЧИСЛО!!!!")
        main()


if __name__ == "__main__":
    main()