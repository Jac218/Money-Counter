import os

class Money_Counter():
    def __init__(self):
        #define vars
        self.one = self.five = self.ten = self.twenty = self.fifty = self.hundo = 0
        self.v1 = self.v2 = self.v3 = self.v4 = self.v5 = self.v6 = 0
        self.fl1 = self.fl2 = self.fl3 = self.fl4 = self.fl5 = self.fl6 = False
        self.cd = False

    #saves flags
    def save(self):
        self.x1 = self.fl1
        self.x2 = self.fl2
        self.x3 = self.fl3
        self.x4 = self.fl4
        self.x5 = self.fl5
        self.x6 = self.fl6

    #sets to save
    def set(self):
        self.fl1 = self.x1
        self.fl2 = self.x1
        self.fl3 = self.x3
        self.fl4 = self.x4
        self.fl5 = self.x5
        self.fl6 = self.x6

    #sets flags true
    def fltrue(self):
        self.fl1 = self.fl2 = self.fl3 = self.fl4 = self.fl5 = self.fl6 = True

    #changes to 1s
    def cd1(self):
        cd = True
        self.save()
        self.fl1 = False
        self.mon()

    #changes to 5s
    def cd5(self):
        cd = True
        self.save()
        #self.fltrue()
        self.fl1 = True
        self.fl2 = False
        self.mon()

    #changes to 10s
    def cd10(self):
        cd = True
        self.save()
        #self.fltrue()
        self.fl1 = self.fl2 = True
        self.fl3 = False
        self.mon()

    #changes to 20s
    def cd20(self):
        cd = True
        self.save()
        #self.fltrue()
        self. fl1 = self.fl2 = self.fl3 = True
        self.fl4 = False
        self.mon()

    #changes to 50s
    def cd50(self):
        cd = True
        self.save()
        #self.fltrue()
        self.fl1 = self.fl2 = self.fl3 = self.fl4 = True
        self.fl5 = False
        self.mon()

    #changes to 100s
    def cd100(self):
        cd = True
        self.save()
        #self.fltrue()
        self.fl1 = self.fl2 = self.fl3 = self.fl4 = self.fl5 = True
        self.fl6 = False
        self.mon()

    #changes to count
    def cdcount(self):
        self.fltrue()
        self.mon()

    #prints error
    def interror(self):
            print('..... Must Be A Whole Number .....')

    #sets up variables and displays the header
    def status(self):
        try:
            m1 = int(self.v1)
            n1 = m1
            z1 = False
        except:
            m1 = 0
            n1 = '_'
            z1 = True

        try:
            m2 = int(self.v2)
            n2 = m2
            z2 = False
        except:
            m2 = 0
            if z1 == True:
                n2 = '*'
                z2 = True
            else:
                n2 = '_'
                z2 = True
        try:
            m3 = int(self.v3)
            n3 = m3
            z3 = False
        except:
            m3 = 0
            if z2 == True:
                n3 = '*'
                z3 = True
            else:
                n3 = '_'
                z3 = True

        try:
            m4 = int(self.v4)
            n4 = m4
            z4 = False
        except:
            m4 = 0
            if z3 == True:
                n4 = '*'
                z4 = True
            else:
                n4 = '_'
                z4 = True

        try:
            m5 = int(self.v5)
            n5 = m5
            z5 = False
        except:
            m5 = 0
            if z4 == True:
                n5 = '*'
                z5 = True
            else:
                n5 = '_'
                z5 = True

        try:
            m6 = int(self.v6)
            n6 = m6
        except:
            m6 = 0
            if z5 == True:
                n6 = '*'
            else:
                n6 = '_'

        self.clear()
        self.fin = m1 + (m2*5) + (m3*10) + (m4*20) + (m5*50) + (m6*100)
        print(f' #1:{n1} | #5:{n2} | #10:{n3} | #20:{n4} | #50:{n5} | #100:{n6} | ${self.fin}')
        print('\nExit: "e"   | Restart: "r"   | Total: "t"\n')

    #displays back
    def back(self):
        print('\n<-- \nBack')

    #clears at start
    def clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    #clears and restarts
    def restart(self):
        self.v1 = self.v2 = self.v3 = self.v4 = self.v5 = self.v6 = 0
        self.fl1 = self.fl2 = self.fl3 = self.fl4 = self.fl5 = self.fl6 = False
        self.clear()
        self.mon()

    #after program finishes, propose an exit or restart.
    def end(self):
        while True:
            x = input('\n > ')
            if x == 'e':
                exit()
            elif x == 'r':
               self.restart()
            elif x == '#1':
                self.cd1()
            elif x == '#5':
                self.cd5()
            elif x == '#10':
                self.cd10()
            elif x == '#20':
                self.cd20()
            elif x == '#50':
                self.cd50()
            elif x == '#100':
                self.cd100()
            elif x == 't':
                self.count()
            else:
                print('..... Invalid .....')

    #asks user how many ones
    def f1(self):
        self.v1 = 0
        ie = False
        while True:
            self.status()
            if ie == True:
                ie = False
                self.interror()
            else:
                try:
                    one = input('How many 1s?\n > ')
                    o = int(one)
                    self.fl1 = True
                    return o

                except:
                #navigation
                    if one == 'e':
                        exit()
                    elif one == 'r':
                        self.restart()
                    elif one == '#1':
                        self.cd1()
                    elif one == '#5':
                        self.cd5()
                    elif one == '#10':
                        self.cd10()
                    elif one == '#20':
                        self.cd20()
                    elif one == '#50':
                        self.cd50()
                    elif one == '#100':
                        self.cd100()
                    elif one == 't':
                        self.cdcount()
                    else:
                    #sets to display error on next cycle
                        ie = True

    #asks user how many fives
    def f2(self):
        self.v2 = 0
        ie = False
        while True:
            self.status()
            if ie == True:
                ie = False
                self.interror()
            else:
                try:
                    five = input('How many 5s?\n > ')
                    f = int(five)
                    self.fl2 = True
                    return f

                except:
                #navigation
                    if five == 'e':
                        exit()
                    elif five == 'r':
                        self.restart()
                    elif five == '#1':
                        self.cd1()
                    elif five == '#5':
                        self.cd5()
                    elif five == '#10':
                        self.cd10()
                    elif five == '#20':
                        self.cd20()
                    elif five == '#50':
                        self.cd50()
                    elif five == '#100':
                        self.cd100()
                    elif five == 't':
                        self.cdcount()
                    else:
                    #sets error to display on next cycle
                        ie = True

    #asks user how many tens
    def f3(self):
        self.v3 = 0
        ie = False
        while True:
            self.status()
            if ie == True:
                ie = False
                self.interror()
            else:
                try:
                    ten = input('How many 10s?\n > ')
                    t = int(ten)
                    self.fl3 = True
                    return t

                except:
                #navigation
                    if ten == 'e':
                        exit()
                    elif ten == 'r':
                        self.restart()
                    elif ten == '#1':
                        self.cd1()
                    elif ten == '#5':
                        self.cd5()
                    elif ten == '#10':
                        self.cd10()
                    elif ten == '#20':
                        self.cd20()
                    elif ten == '#50':
                        self.cd50()
                    elif ten == '#100':
                        self.cd100()
                    elif ten == 't':
                        self.cdcount()
                    else:
                    #sets error to display on next cycle
                        ie = True

    #asks user how many twenties
    def f4(self):
        self.v4 = 0
        ie = False
        while True:
            self.status()
            if ie == True:
                ie = False
                self.interror()
            else:
                try:
                    twenty = input('How many 20s?\n > ')
                    tw = int(twenty)
                    self.fl4 = True
                    return tw

                except:
                #navigation
                    if twenty == 'e':
                        exit()
                    elif twenty == 'r':
                        self.restart()
                    elif twenty == '#1':
                        self.cd1()
                    elif twenty == '#5':
                        self.cd5()
                    elif twenty == '#10':
                        self.cd10()
                    elif twenty == '#20':
                        self.cd20()
                    elif twenty == '#50':
                        self.cd50()
                    elif twenty == '#100':
                        self.cd100()
                    elif twenty == 't':
                        self.cdcount()
                    else:
                    #sets error to display on next cycle
                        ie = True

    #asks user how many fifties
    def f5(self):
        self.v5 = 0
        ie = False
        while True:
            self.status()
            if ie:
                ie = False
                self.interror()
            else:
                try:
                    fifty = input('How many 50s?\n > ')
                    fif = int(fifty)
                    self.fl5 = True
                    return fif

                except:
                #navigation
                    if fifty == 'e':
                        exit()
                    elif fifty == 'r':
                        self.restart()
                    elif fifty == '#1':
                        self.cd1()
                    elif fifty == '#5':
                        self.cd5()
                    elif fifty == '#10':
                        self.cd10()
                    elif fifty == '#20':
                        self.cd20()
                    elif fifty == '#50':
                        self.cd50()
                    elif fifty == '#100':
                        self.cd100()
                    elif fifty == 't':
                        self.cdcount()
                    else:
                    #sets error to display on next cycle
                        ie = True

    #asks user how many hundreds
    def f6(self):
        self.v6 = 0
        ie = False
        while True:
            self.status()
            if ie == True:
                ie = False
                self.interror()
            else:
                try:
                    hundo = input('How many 100s?\n > ')
                    hun = int(hundo)
                    self.fl6 = True
                    return hun

                except:
                    if hundo == 'e':
                        self.exit()
                    elif hundo == 'r':
                        self.restart()
                    elif hundo == '#1':
                        self.cd1()
                    elif hundo == '#5':
                        self.cd5()
                    elif hundo == '#10':
                        self.cd10()
                    elif hundo == '#20':
                        self.cd20()
                    elif hundo == '#50':
                        self.cd50()
                    elif hundo == '#100':
                        self.cd100()
                    elif hundo == 't':
                        self.cdcount
                    else:
                    #sets error to be displayed on next cycle
                        ie = True

    #count the bills and add the value. Print in a user friendly output.
    def count(self):
        self.status()
        print(f'Bill ~ # \n1 ~~~~ {self.v1} \n5 ~~~~ {self.v2} \n10 ~~~ {self.v3} \n20 ~~~ {self.v4} \n50 ~~~ {self.v5} \n100 ~~ {self.v6} \nTotal: ${self.fin}')
        self.end()

    #runs the program
    def mon(self):
        while True:
            self.clear()
            if self.fl1 == False:
                if self.cd == True:
                    self.cd = False
                    self.set()
                self.v1 = self.f1()

            elif self.fl2 == False:
                if self.cd == True:
                    self.cd = False
                    self.set()
                self.v2 = self.f2()

            elif self.fl3 == False:
                if self.cd == True:
                    self.cd = False
                    self.set()
                self.v3 = self.f3()

            elif self.fl4 == False:
                if self.cd == True:
                    self.cd = False
                    self.set()
                self.v4 = self.f4()

            elif self.fl5 == False:
                if self.cd == True:
                    self.cd = False
                    self.set()
                self.v5 = self.f5()

            elif self.fl6 == False:
                if self.cd == True:
                    self.cd = False
                    self.set()
                self.v6 = self.f6()

            else:
                self.count()

#Runs program
pro = Money_Counter()
pro.mon()