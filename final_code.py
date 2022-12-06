import random
import tkinter as tk

class Contestant:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        """returns string representation of contestant object"""
        return f"{self.name}"

class Pairs:
    def __init__(self):
        """initializes 4 arrays (contestants, random pairs, finished pairs and perfect pairs) and counter"""
        self.weeks = 0
        self.list_c = []
        self.random_pairs = [] 
        self.perfect_pairs = set()
        self.finished_pairs = set()
    
    def create_contestants(self, n=16):
        """creates contestants and adds them to a list"""
        if self.list_c:
            return

        c1 = Contestant("Sam")
        c2 = Contestant("Mike")
        c3 = Contestant("Joey")
        c4 = Contestant("Rachel")
        c5 = Contestant("Liam")
        c6 = Contestant("Noel")
        c7 = Contestant("Travis")
        c8 = Contestant("Mavis")
        c9 = Contestant("Kyle")
        c10 = Contestant("Taylor")
        c11 = Contestant("Greg")
        c12 = Contestant("Talia")
        c13 = Contestant("Leo")
        c14 = Contestant("Cass")
        c15 = Contestant("Jason")
        c16 = Contestant("James")

        temp_l = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16]

        for i in range(n):
            temp = temp_l[i]
            self.list_c.append(temp)

    def create_random_pairs(self, temp_l = None, random_list = None):
        """takes in list of contestants and creates list of random pairs"""
        if temp_l is None and random_list is None:
            temp_l = set()
            random_list = []
        
        if len(self.list_c)//2 == len(random_list):
            return
        else:
            temp = tuple(random.sample(self.list_c, 2))
            c1 = temp[0]
            c2 = temp[1]

            if temp not in self.finished_pairs:
                if c1 not in temp_l and c2 not in temp_l:
                    random_list.append(temp)
                    temp_l.add(c1)
                    temp_l.add(c2)
            
            self.create_random_pairs(temp_l, random_list)
        
        self.random_pairs = random_list

    def create_perfect_pairs(self, temp_l=None):
        """creates the list of perfect pairs randomly"""
        if temp_l is None:
            temp_l = set()

        if len(self.perfect_pairs) == len(self.list_c)//2:
            return
        else:
            temp = tuple(random.sample(self.list_c, 2))
            c1 = temp[0]
            c2 = temp[1]

            if temp not in self.perfect_pairs:
                if c1 not in temp_l and c2 not in temp_l:
                    self.perfect_pairs.add(temp)
                    temp_l.add(c1)
                    temp_l.add(c2)
            
            self.create_perfect_pairs(temp_l)

    def truth_booth(self, pair):
        """takes in pair from list of random pairs, then checks pair with list of perfect pair - returns true or false"""
        if pair in self.perfect_pairs:
            return True
        return False

    def truth_booth_2(self, pair):
        """takes in pair from list of random pairs, then checks pair with list of perfect pair - returns true or false"""
        for p in self.perfect_pairs:
            if pair[0] in p and pair[1] in p:
                return True
        return False

    def correct_num_pairs(self):
        """returns how many pairs from random pairs list is a perfect pair"""
        counter = 0

        for pair in self.random_pairs:
            if self.truth_booth(pair) or self.truth_booth_2(pair):
                counter += 1
        
        if counter == 1:
            return f"There is {counter} perfect pair within the random pairs."
        else:
            return f"There are {counter} perfect pairs within the random pairs."
    
    def remove_pair(self, pair):
        """removes pair from play (meaning it can't be a choice again) and adds it to finished pairs list"""
        self.finished_pairs.add(pair)
        c1 = pair[0]
        c2 = pair[1]

        self.list_c.remove(c1)
        self.list_c.remove(c2)

    def quick_simulator(self, n=16):
        """simulates quick play"""
        self.create_contestants(n)
            
        self.create_perfect_pairs()
        txt = ""

        while self.finished_pairs != self.perfect_pairs:
            self.weeks += 1
            txt += f"\n  Week {self.weeks}:"
            txt += "\n"
            txt += f"    Contestants: {self.list_c}"
            txt += "\n"

            self.create_random_pairs()
            txt += (f"    Week's Pairings: {self.random_pairs}")
            txt += "\n"

            txt += f"    {self.correct_num_pairs()}"
            txt += "\n"

            ind = random.randint(0, len(self.random_pairs) - 1)
            rand_pair = self.random_pairs[ind]

            if self.truth_booth(rand_pair):
                self.remove_pair(rand_pair)
            
            txt += (f"    Perfect pairs: {self.perfect_pairs}")
            txt += "\n"
            txt += (f"    Perfect pairs found: {self.finished_pairs}")
            txt += "\n"
        
        txt += (f"\n  {self.weeks} weeks with perfect pairs: {self.finished_pairs}\n")
        return txt

    def create_c(self, entry, label, textbox):
        """creats contestants in gui"""
        var = int(entry.get())
        self.create_contestants(var)

        self.create_perfect_pairs()
        print(self.perfect_pairs)

        label.destroy()
        entry.destroy()
        txt=f"\n    Contestants: {self.list_c}\n"
        textbox.insert(tk.INSERT, txt)

    def truth_booth_input(self, textbox, entry, l4, button, window):
        """takes in pair of user's choice and checks if it's a perfect pair"""
        var = int(entry.get())
        pair = self.random_pairs[var-1]

        txt = f"\n                                                                You have chosen {pair}.\n"
        textbox.insert(tk.INSERT, txt)

        if self.truth_booth_2(pair):
            self.remove_pair(pair)
            txt2 = "\n                                                                     You've found a match!\n"
            textbox.insert(tk.INSERT, txt2)

            txt3 = f"\n    Perfect pairs found: {self.finished_pairs}\n"
            textbox.insert(tk.INSERT, txt3)

            if len(self.list_c) == 0:
                w3 = tk.Toplevel(window, bg="#6fbcd6")
                w3.title("Congrats!")
                w3.geometry("700x50")

                lab = tk.Label(w3, text=f"Congratulations, you've found all pairs in {self.weeks} weeks!", bg="#6fbcd6", font=("Arial", 30))
                lab.pack(side="top")

        else:
            txt4 = "\n                                                               Sorry, this is not a perfect pair.\n"
            textbox.insert(tk.INSERT, txt4)

        entry.destroy()
        l4.destroy()
        button.destroy()

    def next_move(self, window, textbox):
        """moves through the weeks; creates random pairs and simulates game"""
        self.weeks += 1
        txt = f"\n                                                                           Week {self.weeks}:\n"
        textbox.insert(tk.INSERT, txt)

        l4 = tk.Label(window, text="Pick a pair to go to the truth booth? \nInput a number.")
        l4.pack(side="top")

        e2 = tk.Entry(window, width= 10)
        e2.focus_set()
        e2.pack(side="top")

        self.create_random_pairs()
        txt2 = f"\n    The pairs formed this round were {self.random_pairs}\n\n                                                     {self.correct_num_pairs()}\n"
        textbox.insert(tk.INSERT, txt2)

        truth_booth_button = tk.Button(window, text="Truth Booth", command=lambda: (self.truth_booth_input(textbox, e2, l4, truth_booth_button, window)))
        truth_booth_button.pack(side="top")

    def simulation(self, w1):
        """sets up gui for simulation window"""

        text = tk.Text(w1, height="47", width="160", bg="#5aa36d")
        text.pack(side="top")

        l1 = tk.Label(w1, text="How many contestants would you like?")
        l1.pack(side="top")

        e1 = tk.Entry(w1, width= 10)
        e1.focus_set()
        e1.pack(side="top")

        create_button = tk.Button(w1, text="Create Contestants", command=lambda: (self.create_c(e1, l1, text)))
        create_button.pack(side="top")

        play_button = tk.Button(w1, text="Next Move", command= lambda: (self.next_move(w1, text)))
        play_button.pack(side="top")