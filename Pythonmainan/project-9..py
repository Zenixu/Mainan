from tkinter import *
import random 

root = Tk() 
root.geometry('400x300') 
root.title('Love Calculator') 

def lovecalculate(): 
    st = '0123456789'
    digit = 2
    temp = "".join(random.sample(st, digit)) 
    result.config(text=temp) 


heading = Label(root, text='Love Calculator') 
heading.pack() 


slot1 = Label(root, text="Masukan Nama Kamu:") 
slot1.pack() 
name1 = Entry(root, border=5) 
name1.pack() 

slot2 = Label(root, text="Masukan Nama Pasanganmu:") 
slot2.pack() 
name2 = Entry(root, border=5) 
name2.pack() 

bt = Button(root, text="Menghitung", height=1, 
            width=9, command=lovecalculate) 
bt.pack() 


result = Label(root, text='persentase cinta di antara kalian berdua: ') 
result.pack() 


root.mainloop() 