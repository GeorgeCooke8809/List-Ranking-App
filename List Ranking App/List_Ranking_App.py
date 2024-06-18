from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Ranking")

long_list_frames = Frame(root)
long_list_frames.rowconfigure(0, weight = 1)
long_list_frames.rowconfigure(1, weight = 9)

short_list_frames = Frame(root)
short_list_frames.rowconfigure(0, weight = 1)
short_list_frames.rowconfigure(1, weight = 9)

final_list_frames = Frame(root)
final_list_frames.rowconfigure(0, weight = 1)
final_list_frames.rowconfigure(1, weight = 9)

long_list = open("LongList.txt", "w+")
long_list_items = long_list.read()
long_list_items = long_list_items.split("\n")

short_list = open("ShortList.txt", "w+")
short_list_items = short_list.read()
short_list_items = short_list_items.split("\n")

final_list = open("FinalList.txt", "w+")
final_list_items = final_list.read()
final_list_items = final_list_items.split("\n")

if long_list_items[0] == "" and short_list_items[0] == "" and final_list_items[0] == "":
    full_list = open("FullList.txt", "r")
    full_list_items = full_list.read()
    full_list_items = full_list_items.split("\n")
    
    for lines in full_list_items:
        long_list.writelines(lines + "\n")
    long_list.close()
    
    long_list_items = full_list_items
    
number_of_long = len(long_list_items)

frames = []
for i in range(number_of_long):
    frame = Frame(long_list_frames, borderwidth = 2)
    frame.pack(fill = "x")
    frame.columnconfigure(0, weight = 1, minsize = 20)
    frame.columnconfigure(1, weight = 2)
    frame.columnconfigure(2, weight = 1, minsize = 20)

    label = Label(frame, text = long_list_items[i])
    label.grid(row = 0, column = 1)
    
    frames.append(frame)
    

number_of_short = len(short_list_items)

frames = []
for i in range(number_of_short):
    frame = Frame(short_list_frames, borderwidth = 2)
    frame.pack(fill = "x")
    frame.columnconfigure(0, weight = 1, minsize = 20)
    frame.columnconfigure(1, weight = 2)
    frame.columnconfigure(2, weight = 1, minsize = 20)

    label = Label(frame, text = short_list_items[i])
    label.grid(row = 0, column = 1)
    
    frames.append(frame)

long_list_frames.pack(padx = 10, side = LEFT)
short_list_frames.pack(padx = 10, side = LEFT)
final_list_frames.pack(padx = 10, side = LEFT)
root.mainloop()
