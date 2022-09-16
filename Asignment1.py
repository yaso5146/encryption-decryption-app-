import tkinter as tk 
from tkinter import N, Entry, ttk
from math import gcd 
import re

def calc_keys():
     d_var = 3
     while(True):
          if (int(e.get()) * d_var) % int(z.get()) == 1:
               d.set(d_var)
               break
          d_var = d_var + 1
def calc_n_z():
     n.set(int(p.get())*int(q.get()))
     z.set(int(p.get()-1)*int(q.get()-1))
     prime_a = int(z.get())
     prime_b = 3
     while(True): 
          if gcd(prime_a,prime_b) == 1 and prime_b < n.get():
               e.set(prime_b)
               break
          elif prime_b >= n.get():
               break
          prime_b = prime_b + 1
     
def encrypt():
    hex_text =""
    string_ver = ""
    for x in plain_text.get():
        dec_number = (ord(x)**int(e.get())) % int(n.get())
        hex_text = hex_text+str(format(dec_number, 'x').zfill(4))
        string_ver = string_ver + str(dec_number)+','
    string_ver = string_ver[:-1]
    hexadecimal_number.set(hex_text)
    encrypted_text.set(string_ver)

def decrypt():
    int_text =""
    text_value = ""
    four_character = ""
    hex_list = []
    for x in cipher_text.get():
        four_character = four_character + x
        if len(four_character) >= 4:
            hex_list.append(four_character)
            four_character=""
    for x in hex_list:
        int_number = int(x,base=16)
        int_text = int_text + str(int_number) +','
        text_value = text_value + chr((int_number**int(d.get()))%int(n.get()))
    int_text = int_text[:-1]
    decrypted_text.set(int_text)
    plain_decrypted_text.set(text_value)


# root window
root = tk.Tk()
root.resizable(False, False)
root.geometry('710x280')
root.title('Assignment 1 - ISE 426 - Nilay Yasemin Canlar & Öktem Demircigil')

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# create frames
frame1 = ttk.Frame(notebook, width=700, height=700)
frame2 = ttk.Frame(notebook, width=700, height=700)
frame3 = ttk.Frame(notebook, width=700, height=700)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)


# add frames to notebook

notebook.add(frame1, text='Key Selection')
notebook.add(frame2, text='Encryption')
notebook.add(frame3, text='Decryption')


# Manupilate Frames
#Frame 1
p_label = ttk.Label(frame1, text = "Enter Prime Number(p): ").grid(row = 0, column= 0, padx=10, pady=10)
q_label = ttk.Label(frame1, text = "Enter Prime Number(q): ").grid(row = 0, column= 3)
n_label = ttk.Label(frame1, text = "n is: ").grid(row = 2, column= 0, padx=10, pady=10)
z_label = ttk.Label(frame1, text = "z is: ").grid(row = 2, column= 3)
e_label = ttk.Label(frame1, text = "Enter e (e<n, prime to z) : ").grid(row = 3, column= 0, padx=10, pady=10)
public_label = ttk.Label(frame1, text = "Your public key is (e),(n) : ").grid(row = 4, column= 0, padx=10, pady=10)
private_label = ttk.Label(frame1, text = "Your private key is (d),(n) : ").grid(row = 5, column= 0, padx=10, pady=10)
#Frame 2
public_label = ttk.Label(frame2, text = "Your public key is (e),(n) : ").grid(row = 0, column= 0, pady=5)
plain_text_label = ttk.Label(frame2, text = "Enter Plaintext : ").grid(row = 1, column= 0,pady=5)
encrypted_text_label = ttk.Label(frame2, text = "Cipher text (int) : ").grid(row = 3, column= 0,pady=5)
hexadecimal_number_label = ttk.Label(frame2, text = "Cipher text(in hex) : ").grid(row = 4, column= 0,pady=5)
#Frame 3
private_label = ttk.Label(frame3, text = "Your private key is (d),(n) : ").grid(row = 0, column= 0, pady=5)
plain_text_label = ttk.Label(frame3, text = "Enter Cypher : ").grid(row = 1, column= 0,pady=5)
encrypted_text_label = ttk.Label(frame3, text = "Plain text (int) : ").grid(row = 3, column= 0,pady=5)
hexadecimal_number_label = ttk.Label(frame3, text = "Plain text : ").grid(row = 4, column= 0,pady=5)

# Veriables

p = tk.IntVar()
q = tk.IntVar()
n = tk.IntVar()
z = tk.IntVar()
e = tk.IntVar()
d = tk.IntVar()
plain_text = tk.StringVar()
encrypted_text = tk.StringVar()
hexadecimal_number = tk.StringVar()
cipher_text = tk.StringVar()
decrypted_text = tk.StringVar()
plain_decrypted_text = tk.StringVar()

#Frame 1
p_entry = ttk.Entry(frame1, textvariable=p).grid(row = 0 ,column=1)
q_entry = ttk.Entry(frame1, textvariable=q).grid(row = 0 ,column=4)
n_value = ttk.Entry(frame1, textvariable=n).grid(row = 2 ,column=1)
z_value = ttk.Entry(frame1, textvariable=z).grid(row = 2 ,column=4)
e_value = ttk.Entry(frame1, textvariable=e).grid(row = 3 ,column=1)
e_value = ttk.Entry(frame1, textvariable=e).grid(row = 4 ,column=1)
n_value = ttk.Entry(frame1, textvariable=n).grid(row = 4 ,column=2,padx=5)
d_value = ttk.Entry(frame1, textvariable=d).grid(row = 5 ,column=1)
n_value = ttk.Entry(frame1, textvariable=n).grid(row = 5 ,column=2,padx=5)

#Frame 2
e_value = ttk.Entry(frame2, textvariable=e).grid(row = 0 ,column=1)
n_value = ttk.Entry(frame2, textvariable=n).grid(row = 0 ,column=2,padx=5)
plain_text_value = ttk.Entry(frame2, textvariable=plain_text,width=80).grid(row = 1 ,column=1,padx=5,columnspan=5)
encrypted_text_value = ttk.Entry(frame2, textvariable=encrypted_text,width=80).grid(row = 3 ,column=1,padx=5,columnspan=5)
hexadecimal_number_value = ttk.Entry(frame2, textvariable=hexadecimal_number,width=80).grid(row = 4 ,column=1,padx=5,columnspan=5)

#Frame 3
d_value = ttk.Entry(frame3, textvariable=d).grid(row = 0 ,column=1)
n_value = ttk.Entry(frame3, textvariable=n).grid(row = 0 ,column=2,padx=5)
cipher_text_value = ttk.Entry(frame3, textvariable=cipher_text,width=80).grid(row = 1 ,column=1,padx=5,columnspan=5)
decrypted_text_value = ttk.Entry(frame3, textvariable=decrypted_text,width=80).grid(row = 3 ,column=1,padx=5,columnspan=5)
plain_decrypted_text_value = ttk.Entry(frame3, textvariable=plain_decrypted_text,width=80).grid(row = 4 ,column=1,padx=5,columnspan=5)

# Buttons
#Frame 1
calc_nz = ttk.Button(frame1,text="Calculate n and z",command =calc_n_z).grid(row = 1 ,column=2,padx=15)
calc_keys = ttk.Button(frame1,text="Calculate Keys",command =calc_keys).grid(row = 3 ,column=2,padx=15)
#Frame 2
encrypt_keys = ttk.Button(frame2,text="Encrypt",command =encrypt).grid(row = 2 ,column=2,padx=15)
#Frame 3
decrypt_keys = ttk.Button(frame3,text="Decrypt",command = decrypt).grid(row = 2 ,column=2,padx=15)




root.mainloop()