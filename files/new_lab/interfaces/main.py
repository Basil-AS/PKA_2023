from tkinter import *
from tkinter.ttk import Combobox



window = Tk()
window.title("Добро пожаловать программу шифрования")
window.geometry('1280x840'), window.config(background="#808080")


class EntryWithPlaceholder(Entry):
    def __init__(self, master=None, placeholder=None):
        self.entry_var = StringVar()
        super().__init__(master, textvariable=self.entry_var)

        if placeholder is not None:
            self.placeholder = placeholder
            self.placeholder_color = 'grey'
            self.default_fg_color = self['fg']
            self.placeholder_on = False
            self.put_placeholder()
            self.entry_var.trace("w", self.entry_change)

            # При всех перечисленных событиях, если placeholder отображается, ставить курсор на 0 позицию
            self.bind("<FocusIn>", self.reset_cursor)
            self.bind("<KeyRelease>", self.reset_cursor)
            self.bind("<ButtonRelease>", self.reset_cursor)

    def entry_change(self, *args):
        if not self.get():
            self.put_placeholder()
        elif self.placeholder_on:
            self.remove_placeholder()
            self.entry_change()  # На случай, если после удаления placeholder остается пустое поле

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color
        self.icursor(0)
        self.placeholder_on = True

    def remove_placeholder(self):
        # Если был вставлен какой-то символ в начало, удаляем не весь текст, а только placeholder:
        text = self.get()[:-len(self.placeholder)]
        self.delete('0', 'end')
        self['fg'] = self.default_fg_color
        self.insert(0, text)
        self.placeholder_on = False

    def reset_cursor(self, *args):
        if self.placeholder_on:
            self.icursor(0)


#Поле для ввода Ключа
key = EntryWithPlaceholder(window, "Введите ключ")
key.grid(column=650, row=0)


#Поле выбора шифрования
combo = Combobox(window)
combo['values'] = (""
                   "Цезаря", "Атабаш", "Полибея", #1
                   "Белазо", "Атабаш", "Тритемия", #2
                   "Матричный", "Плейфора", #3
                   "Решетка Кардано", "Вертикальной перестановки", "Фейстеля", #4
                   "ГОСТ 28147-89", "Блокнот Шенонна", #5
                   "A5", #6
                   "AES", "Кузнечик", "Магма", #7
                   "ECC", "Elgamal", "RSA", #8
                   "Elgamal", "RSA", #9
                   "ГОСТ R-34 10 94", "ГОСТ R-34 10 2012", #10
                   "Деффи-Хеллмана"
                   )
combo.current(1)
combo.grid(column=640, row=0)


#Поле для ввода пословицы
proverb_comment = Label(window, text="ОТКРЫТЫЙ ТЕКСТ:", font=("Arial Bold", 24),background="#808080")
proverb_comment.grid(column=70, row=40)
proverb = Text(window, height=25, width=75,
              bg="#D3D3D3")
proverb.grid(column=70, row=50)


#Поле для ввода шифртекста
ecription_comment = proverb_comment = Label(window, text="ШИФРТЕКСТ:", font=("Arial Bold", 24),background="#808080")
proverb_comment.grid(column=700, row=40)
encription_text = Text(window, height=25, width=75,
              bg="#D3D3D3")
encription_text.grid(column=700, row=50)


#Поле для ввода дешефровки
decription_comment = Label(window, text="РАЗШИФРОВКА:", font=("Arial Bold", 24),background="#808080")
decription_comment.grid(column=70, row=700)
proverb = Text(window, height=15, width=75,
              bg="#D3D3D3")
proverb.grid(column=70, row=710)


def show_massage():
    label.config(text=combo.get(), font= ('Helvetica 13'))
    label1.config(text=method.get(), font=('Helvetica 13'))


btn = Button(text="Click", command=show_massage)
btn.grid(column=660, row=0)


label = Label()
label.grid(column=700, row=70)
label1 = Label()
label1.grid(column=700, row=80)


method = Combobox(window)
method['values'] = ("Шифровать", "Дешифровать")
method.current(1)
method.grid(column=700, row=60)

window.mainloop()
mainloop()


