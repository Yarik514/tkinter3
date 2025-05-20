from tkinter import *
from random import *
from tkinter import messagebox

a = []
def mas():
    n = edit1.get()
    if not n:
        messagebox.showerror('Помилка', 'Розмірність масиву не вказана')
        return

    n = int(n)

    a.clear()
    listbox1.delete(0, END)
    listbox2.delete(0, END)
    for i in range(n):
        a.append(randint(-50, 50))
        listbox1.insert(END, a[i])

def sort():
    n = len(a)
    # метод екстремальних елементів
    for j in range(n - 1):
        min = j
        for i in range(j, n):
            if a[i] > a[min]:
                a[i], a[min] = a[min], a[i]
    listbox2.delete(0, END)
    for i in range(n):
        listbox2.insert(END, a[i])


def compute_positives():
    c = 0
    for element in a:
        if element > 0:
            c += 1
    label4['text'] = 'positives = ' + str(c)


def about_author():
    messagebox.showinfo('Про автора', 'Автор: Киця Ярослав\nEmail: yaroslavkytsia@gmail.com')


def problem_statement():
    messagebox.showinfo('Умова задачі', '''Підрахувати кількість додатних елементів у даному одновимірному масиві.
Виконати сортування елементів масиву за спаданням, використовуючи метод
екстремальних елементів.''')


def set_light_theme():
    root['bg'] = 'lightgray'
    listbox1['bg'] = 'white'
    listbox2['bg'] = 'white'
    label1['bg'] = 'lightgray'
    label2['bg'] = 'lightgray'
    label3['bg'] = 'lightgray'
    label4['bg'] = 'lightgray'
    label1['fg'] = 'black'
    label2['fg'] = 'black'
    label3['fg'] = 'black'
    label4['fg'] = 'black'
    edit1['bg'] = 'white'


def set_dark_theme():
    root['bg'] = 'black'
    listbox1['bg'] = 'gray80'
    listbox2['bg'] = 'gray80'
    label1['bg'] = 'black'
    label2['bg'] = 'black'
    label3['bg'] = 'black'
    label4['bg'] = 'black'
    label1['fg'] = 'white'
    label2['fg'] = 'white'
    label3['fg'] = 'white'
    label4['fg'] = 'white'
    edit1['bg'] = 'gray80'


def set_default_theme():
    root['bg'] = '#F0F0F0'
    listbox1['bg'] = '#FFFFFF'
    listbox2['bg'] = '#FFFFFF'
    label1['bg'] = '#F0F0F0'
    label2['bg'] = '#F0F0F0'
    label3['bg'] = '#F0F0F0'
    label4['bg'] = '#F0F0F0'
    label1['fg'] = '#F0F0F0'
    label2['fg'] = '#F0F0F0'
    label3['fg'] = '#F0F0F0'
    label4['fg'] = '#F0F0F0'
    edit1['bg'] = '#FFFFFF'


x = y = 0


def do_popup(event):
    global x, y
    x = event.x
    y = event.y
    popupmenu.post(event.x_root, event.y_root)


root = Tk()
root.title('Масиви')
root.geometry('600x300')

label1 = Label(text='Вихідний масив')
label2 = Label(text='Посортований масив')
label1.place(x=20, y=30)
label2.place(x=200, y=30)

listbox1 = Listbox(height=10, width=20)
listbox2 = Listbox(height=10, width=20)
listbox1.place(x=20, y=70)
listbox2.place(x=200, y=70)

label3 = Label(text='Кількість елементів масиву:')
label3.place(x=400, y=30)

edit1 = Entry()
edit1.place(x=400, y=70)

button1 = Button(text='Заповнити', width=20, command=mas)
button1.place(x=400, y=100)

button2 = Button(text='Сортувати за спаданням', width=20, command=sort)
button2.place(x=400, y=130)

button3 = Button(text='Кількість додатних', width=20, command=compute_positives)
button3.place(x=400, y=160)

label4 = Label(text='positives =')
label4.place(x=400, y=210)

# Головне меню
main_menu = Menu(root)
root.config(menu=main_menu)

# Пункт "Дії з масивом"
array_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Дії з масивом', menu=array_menu)
array_menu.add_command(label='Заповнити', command=mas)
array_menu.add_command(label='Сортувати за спаданням', command=sort)
array_menu.add_command(label='Кількість додатних', command=compute_positives)

# Пункт "Про програму"
about_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Про програму', menu=about_menu)
about_menu.add_command(label='Про автора', command=about_author)
about_menu.add_command(label='Умова задачі', command=problem_statement)

# Контекстне меню
popupmenu = Menu(root, tearoff=0)
popupmenu.add_command(label="Світлий", command=set_light_theme)
popupmenu.add_command(label="Темний", command=set_dark_theme)
popupmenu.add_command(label="Відновити початкові кольори", command=set_default_theme)
root.bind("<Button-3>", do_popup)

root.mainloop()