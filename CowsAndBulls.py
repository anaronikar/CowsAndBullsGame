try:
    import Tkinter as tk
except:
    import tkinter as tk
import random as r
from tkinter import *
from tkinter import messagebox
import time


class SampleApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="COWS AND BULLS GAME", width=20, bg="aquamarine", font=("Times", "24", "bold italic")).pack(
            side="top", fill="x", pady=5)
        e = tk.Entry(self, width=70, font=("none", "9", "bold"))
        e.pack()
        e.insert(0, "Enter your name here!")  # Default text to be displayed as a prompt

        def g():
            f = open("E:\PESU DOCS\COMP\PROJECT\save.txt", 'a+')
            f.write(e.get() + "\n")
            f.close()
            global name
            name = e.get()
            print(e.get())

        tk.Button(self, text="\nCLICK HERE TO SAVE YOUR NAME\n", font=("none", "10", "bold"), width=50, height=1,
                  bg='orangered2', command=lambda: g()).pack()
        tk.Button(self, text="\nHOW TO PLAY?\n", font=("none", "10", "bold"), width=50, height=1, bg='darkgoldenrod1',
                  command=lambda: master.switch_frame(PageOne)).pack()
        tk.Button(self, text="\nSTART\n", font=("none", "10", "bold"), width=50, height=1, bg='deepskyblue2',
                  command=lambda: master.switch_frame(PageTwo)).pack()


class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="HOW THE GAME WORKS: \n>You have to guess the 4-digit number."
                            "\n>Number of Cows and Bulls will be displayed after each guess."
                            "\n>Number of Cows indicates the correct digit guessed, \nbut in the correct position"
                            "\n>Number of Bulls indicates the correct digit, \nand in the wrong position\n>You are given a limited time to guess the number \nand if the time is elapsed you will lose", bg='khaki1',
                 font=('Bookman Old Style', 13, "bold")).pack()
        tk.Button(self, text="<<BACK TO MAIN MENU", font=("none", "10", "bold"), width=50, height=1, bg='wheat3',
                  command=lambda: master.switch_frame(StartPage)).pack()


class PageTwo(tk.Frame):
    def __init__(self, master):
        master.geometry("400x400")
        tk.Frame.__init__(self, master)

        # timer start
        global seconds
        seconds = 30
        setseconds = seconds

        def timer():
            global seconds
            global mins, se
            if seconds > 0:
                seconds = seconds - 1
                mins = seconds // 60
                m = str(mins)

                if mins < 10:
                    m = '0' + str(mins)
                se = seconds - (mins * 60)
                s = str(se)

                if se < 10:
                    s = '0' + str(se)
                time.set(m + ':' + s)

                timer_display.config(textvariable=time)
                # call this function again in 1,000 milliseconds
                master.after(1000, timer)

            elif seconds == 0:
                messagebox.showinfo('GAME OVER', 'TIME UP!')
                master.quit()

        time = tk.StringVar()

        timer_display = tk.Label(master, font=('Trebuchet MS', 20, 'bold'))

        timer_display.pack(side="top")

        timer()
        # timer end
        tk.Label(self, text="BEGIN GUESSING!", bg='dodgerblue4', fg='light cyan', font=('Constantia',12, "bold")).pack(
            side="top", fill="x", pady=5)
        e = tk.Entry(self, width=50)
        e.pack(side='top', expand='yes')
        number = r.randint(1000, 9999)
        print(number)

        def cab():
            numberl = str(number)
            guess = e.get()
            guessl = str(guess)
            cows = 0
            bulls = 0
            for i in range(0, len(numberl)):
                if numberl[i] == guessl[i]:
                    cows += 1
                elif numberl[i] in guessl:
                    bulls += 1

            a = tk.Label(self, text="YOUR GUESS:{}\nCOWS:{} BULLS:{}".format(guessl, cows, bulls), bg='turquoise4',
                         fg='azure2', font=('Helvetica', 18, "bold"))
            a.pack(side="top", fill="x", pady=5)

            if cows == 4:
                me = mins * 60  # mins:minutes when won, se:seconds when won
                secondswon = me + se
                timediff = setseconds - secondswon  # time taket to win

                f = open("E:\PESU DOCS\COMP\PROJECT\save.txt", 'a+')
                f.write(str(timediff) + "\n")
                f.close()

                f = open("E:\PESU DOCS\COMP\PROJECT\save.txt", 'r+')
                users = {}  # dictionary of users
                usersrank = []
                a = f.readlines()
                for i in range(0, len(a), 2):
                    x = a[i].rstrip("\n")
                    users[x] = int(a[i + 1].rstrip("\n"))
                print(users)  # dictionary with name and time taken
                sorted_values = sorted(
                    users.values())  # Sort the values ,prints it in ascending order incase we want to show all their ranks
                sorted_dict = {}
                for i in sorted_values:
                    for k in users.keys():
                        if users[k] == i:
                            sorted_dict[k] = users[k]
                            break
                print(sorted_dict, ": the rankwise dictionary")
                for i in sorted_dict:
                    usersrank.append(i)
                f.close()
                messagebox.showinfo("RESULT",
                                    "YOU WON!\nLEADERBOARD\n1-{}\n2-{}\n3-{}\nYOUR RANK:{}".format(usersrank[0],
                                                                                                   usersrank[1],
                                                                                                   usersrank[2],
                                                                                                   usersrank.index(
                                                                                                       name) + 1))
                master.destroy()

        tk.Button(self, text="NEXT GUESS", font=('Helvetica', 11, "bold"), width=15, height=1, bg='lightblue1',
                  command=lambda: cab()).pack(side='top')


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()