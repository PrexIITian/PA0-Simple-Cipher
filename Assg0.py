import tkinter as tk
first = tk.Tk()
first.title("Encryption/Decryption")
first.geometry('400x300')
tk.Label(first, text="Plain Text",bg='#abc').grid(row=0, column=1,padx=5,pady=15)
tk.Label(first, text="Cipher Text",bg='#def').grid(row=0, column=4,padx=5,pady=15)
tk.Label(first, text="Cipher Text",bg='#def').grid(row=4, column=1,padx=5,pady=15)
tk.Label(first, text="Plain Text",bg='#abc').grid(row=4, column=4,padx=5,pady=15)         
def enc_dec(key):#this is main function that will computationally cipher and decipher the text available in respective input boxes
    #inp=key.char
    if(first.focus_get()==e):
        plain=e.get()
        inp=plain[len(plain)-1]
        if(inp.isalpha()):
            x=chr(ord('a')+ord('z')-ord(inp))#this is the core logic that will encrypt
            en.insert("end",x)#ord gives the ascii of character and chr coverts ascii to character
        if(inp==" "):
            en.insert("end"," ")
    if(first.focus_get()==d):
        cipher=d.get()
        out=cipher[len(cipher)-1]
        if(out.isalpha()):
            y=chr(ord('a')+ord('z')-ord(out))#this is the core logic that will decrypt
            dn.insert("end",y)
        if(out==" "):
            dn.insert("end"," ")    
e = tk.Entry(first)
en = tk.Entry(first)
d = tk.Entry(first)
dn = tk.Entry(first)
e.grid(row=1, column=1,padx=5)
en.grid(row=1, column=4,padx=5)
d.grid(row=5, column=1,padx=5)
dn.grid(row=5, column=4,padx=5)
first.bind('<Key>',enc_dec)#this function is for taking value on each key press event and so will encrypt decrypt character by character as being entered
first.mainloop()