import os

class Money_Counter():
    def __init__(self):
        #define vars
        self.one = self.five = self.ten = self.twenty = self.fifty = self.hundo = 0
        self.v1 = self.v2 = self.v3 = self.v4 = self.v5 = self.v6 = 0
        self.fl1 = self.fl2 = self.fl3 = self.fl4 = self.fl5 = self.fl6 = False
        self.cd = False

    #saves flags
    def rsave(self):
        self.x1 = self.fl1
        self.x2 = self.fl2
        self.x3 = self.fl3
        self.x4 = self.fl4
        self.x5 = self.fl5
        self.x6 = self.fl6

    #sets to save
    def save(self):
        self.fl1 = self.x1
        self.fl2 = self.x1
        self.fl3 = self.x3
        self.fl4 = self.x4
        self.fl5 = self.x5
        self.fl6 = self.x6

    #sets flags true
    def fltrue(self):
        self.fl1 = self.fl2 = self.fl3 = self.fl4 = self.fl5 = self.fl6 = True

    def navigation(self, nvar):
        if nvar == 'e':
            exit()
        elif nvar == 'r':
            self.restart()
        elif nvar == '':
            return 0
        elif nvar == '#1':
            self.cd1()
        elif nvar == '#5':
            self.cd5()
        elif nvar == '#10':
            self.cd10()
        elif nvar == '#20':
            self.cd20()
        elif nvar == '#50':
            self.cd50()
        elif nvar == '#100':
            self.cd100()
        elif nvar == 't':
            self.cdcount()
        else:
        #sets to display error on next cycle
            return True

    #changes to 1s
    def cd1(self):
        cd = True
        self.fl1 = False
        self.mon()

    #changes to 5s
    def cd5(self):
        cd = True
        self.fl1 = True
        self.fl2 = False
        self.mon()

    #changes to 10s
    def cd10(self):
        cd = True
        self.fl1 = self.fl2 = True
        self.fl3 = False
        self.mon()

    #changes to 20s
    def cd20(self):
        cd = True
        self. fl1 = self.fl2 = self.fl3 = True
        self.fl4 = False
        self.mon()

    #changes to 50s
    def cd50(self):
        cd = True
        self.fl1 = self.fl2 = self.fl3 = self.fl4 = True
        self.fl5 = False
        self.mon()

    #changes to 100s
    def cd100(self):
        cd = True
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
    def status(self, error):
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
        bar = f"#1:{n1} | #5:{n2} | #10:{n3} | #20:{n4} | #50:{n5} | #100:{n6} | ${self.fin}"
        length = len(bar)
        evar = "-" * length
        svar = " " * length
        mvar = " " * (length - 49)
        print(f'+{evar}+')
        print(f'|#1:{n1} | #5:{n2} | #10:{n3} | #20:{n4} | #50:{n5} | #100:{n6} | ${self.fin}|')
        print(f'|{svar}|')
        print(f'| [E]xit         | [R]estart      | [T]otal       {mvar}|')
        print(f'+{evar}+')

        if error == True:
            error = False
            self.interror()

    #clears at start
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    #clears and restarts
    def restart(self):
        self.v1 = self.v2 = self.v3 = self.v4 = self.v5 = self.v6 = 0
        self.fl1 = self.fl2 = self.fl3 = self.fl4 = self.fl5 = self.fl6 = False
        self.clear()
        self.mon()

    #after program finishes, propose an exit or restart.
    def end(self):
        ie = False
        while True:
            if ie == True:
                self.interror()
            var = input('\n > ')
            ie = self.navigation(nvar=var)


    #asks user how many ones
    def f1(self):
        self.v1 = 0
        ie = False
        while True:
            self.status(error=ie)
            try:
                one = input('How many 1s?\n > ')
                if not one:
                    o = 0
                else:
                    o = int(one)
                self.fl1 = True
                return o
            except:
                ie = self.navigation(nvar= one)

    #asks user how many fives
    def f2(self):
        self.v2 = 0
        ie = False
        while True:
            self.status(error=ie)
            try:
                five = input('How many 5s?\n > ')
                if not five:
                    f = 0
                else:
                    f = int(five)
                self.fl2 = True
                return f
            except:
                ie = self.navigation(nvar= five)

    #asks user how many tens
    def f3(self):
        self.v3 = 0
        ie = False
        while True:
            self.status(error=ie)
            try:
                ten = input('How many 10s?\n > ')
                if not ten:
                    t = 0
                else:
                    t = int(ten)
                self.fl3 = True
                return t
            except:
                ie = self.navigation(nvar= ten)
                    
    #asks user how many twenties
    def f4(self):
        self.v4 = 0
        ie = False
        while True:
            self.status(error=ie)
            try:
                twenty = input('How many 20s?\n > ')
                if not twenty:
                    tw = 0
                else:
                    tw = int(twenty)
                self.fl4 = True
                return tw
            except:
                ie = self.navigation(nvar=twenty)
                    
    #asks user how many fifties
    def f5(self):
        self.v5 = 0
        ie = False
        while True:
            self.status(error=ie)
            try:
                fifty = input('How many 50s?\n > ')
                if not fifty:
                    fif = 0
                else:
                    fif = int(fifty)
                self.fl5 = True
                return fif
            except:
                ie = self.navigation(nvar=fifty)
                    
    #asks user how many hundreds
    def f6(self):
        self.v6 = 0
        ie = False
        while True:
            self.status(error=ie)
            try:
                hundo = input('How many 100s?\n > ')
                if not hundo:
                    hun = 0
                else:
                    hun = int(hundo)
                self.fl6 = True
                return hun
            except:
                ie = self.navigation(nvar=hundo)
                    
    #count the bills and add the value. Print in a user friendly output.
    def count(self):
        ie = False
        self.status(error=ie)

        rb = f"bill ~ #"
        r1 = f"1 ~~~~ {self.v1}"
        r2 = f"5 ~~~~ {self.v2}"
        r3 = f"10 ~~~ {self.v3}"
        r4 = f"20 ~~~ {self.v4}"
        r5 = f"50 ~~~ {self.v5}"
        r6 = f"100 ~~ {self.v6}"
        rf = f"Total: ${self.fin}"

        lb = len(rb)
        l1 = len(r1)
        l2 = len(r2)
        l3 = len(r3)
        l4 = len(r4)
        l5 = len(r5)
        l6 = len(r6)
        lf = len(rf)
        
        print(f'+{"-" * lf}+\n'
              f'|Bill ~ #{" " * (lf - lb)}|\n'
              f'|1 ~~~~ {self.v1}{" " * (lf - l1)}|\n'
              f'|5 ~~~~ {self.v2}{" " * (lf - l2)}|\n'
              f'|10 ~~~ {self.v3}{" " * (lf - l3)}|\n'
              f'|20 ~~~ {self.v4}{" " * (lf - l4)}|\n'
              f'|50 ~~~ {self.v5}{" " * (lf - l5)}|\n'
              f'|100 ~~ {self.v6}{" " * (lf - l6)}|\n'
              f'|Total: ${self.fin}|\n'
              f'+{"-" * lf}+')
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
