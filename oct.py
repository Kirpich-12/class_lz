from main import Octagon

def func():#выполнение задания
    usr_inp = input('Введите сторону восьмиугольника\n')
    oct = Octagon(int(usr_inp))
    print(f'Радиус описсанной около восьмиугольника окружности{oct.rad_opis()}')
    print(f'Радиус вписсаной в восьмиугольник окружности {oct.rad_vpis()}')
    print(f'Площадь описсанной около восьмиугольника окружности{oct.s_opis()}')
    print(f'Площадь вписсаной в восьмиугольник окружности {oct.s_vpis()}')
    oct.s()
    oct.paint()
    oct.per()


def main():
    func()

if __name__ == '__main__':
    main()