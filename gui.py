import tkinter as tk
from final_code import Pairs, Contestant

main = tk.Tk()
main.geometry("200x200")
main.title("Start")

def sim():
    """simulates the more interactive simulator"""
    g = Pairs()
    w1 = tk.Toplevel(main)
    w1.title("Simulation")
    w1.geometry("1200x1000")

    g.simulation(w1)

def create_sim(e1, l1, window, button):
    """helper to print out text for quick_sim"""
    g1 = Pairs()
    var = int(e1.get())

    txt = g1.quick_simulator(var)

    l1.destroy()
    e1.destroy()
    button.destroy()

    text = tk.Text(window, height="200", width="200", bg="#5675a8")
    text.pack(side="left")

    text.insert(tk.INSERT, txt)

def quick_sim():
    """simulates quick simulator"""
    w2 = tk.Toplevel(main)
    w2.title("Simulation")
    w2.geometry("1100x1000")

    l1 = tk.Label(w2, text="How many contestants would you like?")
    l1.pack(side="top")

    e1 = tk.Entry(w2, width= 10)
    e1.focus_set()
    e1.pack(side="top")

    create_button = tk.Button(w2, text="Create Contestants", command=lambda: (create_sim(e1, l1, w2, create_button)))
    create_button.pack(side="top")


start_button = tk.Button(main, text="Start Simulation", command=sim)
start_button.pack(side="top")

quick_button = tk.Button(main, text="Quick Simulation", command=quick_sim)
quick_button.pack(side="top")

main.mainloop()
