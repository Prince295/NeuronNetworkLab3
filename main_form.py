import tkinter as interface
from widjets import *
from tkinter.filedialog import *
from main import *



Forms.form.pack(in_ = Root.root, side = 'right', expand = True, fill = 'both')
Forms.nav.pack(in_ = Root.root, side = 'left', fill = 'y')
label1 = ThemedLabel(text = 'Входные данные')
label2 = ThemedLabel(text = 'Выход')
label1.pack(in_ = Forms.form, side = 'top', fill = 'x')

message = [None, None, None, None, None, None, None, None, None, None]
button = [None, None, None, None]

container1 = ThemedForm()
container1.pack(in_ = Forms.form, side = 'top', fill = 'x')

container2 = ThemedForm()
container2.pack(in_ = Forms.form, side = 'bottom', fill = 'x')
label2.pack(in_ = Forms.form, side = 'bottom', fill = 'x')

button[0] = ThemedButton(text='Добавить', command = lambda : askopenfilename(filetypes = [("Image Files","*.jpg")], initialdir = "C:/Users/днс/Desktop/Моделирование систем/NeuronNetworkLab3"))
button[1] = ThemedButton(text='Удалить')
button[2] = ThemedButton(text='Изменить', command = get_menu)
button[3] = ThemedButton(text='s')

message[0] = ThemedMessage(text = x[0])
message[1] = ThemedMessage(text = x[1])
message[2] = ThemedMessage(text = x[2])
message[3] = ThemedMessage(text = x[3])
message[4] = ThemedMessage(text = x[4])

for i in range(1,len(T)):
    message[i+4] = ThemedMessage(text = T[i])
for i in range(len(message)):
    if message[i] == None:
        message[i] = ThemedMessage()

button[0].pack(in_ = Forms.nav, side = 'top', pady = 5)
button[1].pack(in_ = Forms.nav, side = 'top', pady = 5)
button[2].pack(in_ = Forms.nav, side = 'top', pady = 5)
button[3].pack(in_ = Forms.nav, side = 'top', pady = 5)

message[0].pack(in_ = container1, side = 'left', padx = 20, pady = 40)
message[1].pack(in_ = container1, side = 'left', padx = 20, pady = 40)
message[2].pack(in_ = container1, side = 'left', padx = 20, pady = 40)
message[3].pack(in_ = container1, side = 'left', padx = 20, pady = 40)
message[4].pack(in_ = container1, side = 'left', padx = 20, pady = 40)

message[5].pack(in_ = container2, side = 'left', padx = 20, pady = 40)
message[6].pack(in_ = container2, side = 'left', padx = 20, pady = 40)
message[7].pack(in_ = container2, side = 'left', padx = 20, pady = 40)
message[8].pack(in_ = container2, side = 'left', padx = 20, pady = 40, fill = 'both', expand = True)
message[9].pack(in_ = container2, side = 'left', padx = 20, pady = 40, fill = 'both', expand = True)
Root.root.mainloop()


