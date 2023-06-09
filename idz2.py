import sys

print("Эта программа проверяет правильность скобочной записи с тремя видами скобок: '[]', '{}', '()',\n"
      "содержащей буквы латинского алфавита. Внутри фигурных скобок обязательно должны быть квадратные, \n"
      "но могут быть круглые, внутри квадратных должны быть круглые или бесскобочные выражения, \n"
      "внутри круглых только бесскобочные арифметические выражения. Также, если один из операндов является скобкой, \n"
      "то и второй должен быть скобкой (не может быть буквой). Могут быть “лишние” скобки, \n"
      "но одна буква не может браться в скобки. В конце строки поставьте 0.\n"
      "Пример правильной записи: {[(a-b)]*(a+b)}/[(a+b*c)]-(a-c)*(a+c)0\n"
      "Пример неправильной записи: {(a+b)*(a-b)}/[a+b/c]((c)-(b-c*d))0\n"
      "Введите: ")


signs = "+-*/"


def read():
    global ch, i
    i += 1
    ch = instr[i]


def error():
    print('Запись неверна:( ')
    chk = input("Хотите ввести еще одну запись? Да - 'y', нет - 'n':\n")
    if chk == 'n':
        sys.exit()
    elif chk == 'y':
        print('Введите запись: ')
        main()



class MainClass:
    def formula(self):
        self.brex()
        self.signbr()
        if ch == '0':
            print('Запись верна:)')
        else:
            print('Запись неверна:(')

    def brex(self):
        if ch == '{':
            if ch == '{':
                read()
            else:
                error()
            self.curbr()
            if ch == '}':
                read()
            else:
                error()
        elif ch == '[':
            if ch == '[':
                read()
            else:
                error()
            self.sqbr()
            if ch == ']':
                read()
            else:
                error()
        elif ch == '(':
            if ch == '(':
                read()
            else:
                error()
            self.nobr()
            if ch == ')':
                read()
            else:
                error()

    def signbr(self):
        if ch in signs:
            self.sign()
            self.brex()
            self.signbr()

    def nobr(self):
        self.letter()
        self.sign()
        self.letter()
        self.signlet()

    def signlet(self):
        if ch in signs:
            self.sign()
            self.letter()
            self.signlet()

    def sqbr(self):
        if ch.isalpha() and ch.islower():
            self.nobr()
        elif ch == '(':
            if ch == '(':
                read()
            else:
                error()
            self.nobr()
            if ch == ')':
                read()
            else:
                error()
            self.signno()
        else:
            error()

    def signno(self):
        if ch in signs:
            self.sign()
            if ch == '(':
                read()
            else:
                error()
            self.nobr()
            if ch == ')':
                read()
            else:
                error()
            self.signno()

    def sqrnd(self):
        if ch == '[':
            if ch == '[':
                read()
            else:
                error()
            self.sqbr()
            if ch == ']':
                read()
            else:
                error()
        elif ch == '(':
            if ch == '(':
                read()
            else:
                error()
            self.nobr()
            if ch == ')':
                read()
            else:
                error()
        else:
            error()

    def rndsign(self):
        if ch == '(':
            if ch == '(':
                read()
            else:
                error()
            self.nobr()
            if ch == ')':
                read()
            else:
                error()
            self.sign()
            self.signno()

    def aftersq(self):
        if ch in signs:
            self.sign()
            self.sqrnd()
            self.aftersq()

    def curbr(self):
        self.rndsign()
        if ch == '[':
            read()
        else:
            error()
        self.sqbr()
        if ch == ']':
            read()
        else:
            error()
        self.aftersq()

    def letter(self):
        if ch.isalpha() and ch.islower():
            if ch.isalpha() and ch.islower():
                read()
            else:
                error()
        else:
            error()

    def sign(self):
        if ch in signs:
            if ch in signs:
                read()
            else:
                error()
        else:
            error()


def main():
    global ch
    global instr
    global i
    instr = input()
    i = 0
    ch = instr[0]
    m = MainClass()
    m.formula()
    chk = input("Хотите ввести еще одну запись? Да - 'y', нет - 'n':\n")
    if chk == 'n':
        sys.exit()
    elif chk == 'y':
        print('Введите запись: ')
        main()


main()
