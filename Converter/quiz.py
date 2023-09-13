import tkinter
from tkinter import ttk
import Pmw
from tkinter import messagebox as msg


class Length:
    length_units = {'Meter': 1, 'Kilometer': 0.001, 'Centimeter': 100, 'Millimeter': 1000}

    def __init__(self, value, unit):
        self.unit = unit
        self.value = value

    def __str__(self):
        return f'{self.value} {self.unit}'

    @staticmethod
    def convert_to():
        try:
            if length_combo.current() != -1 and length_var.get() != " ":
                current = Length(float(length_entry.get()), length_var.get())
                print(current)
                newValue = current.value * Length.length_units[len_values[length_combo.current()]] \
                           / Length.length_units[current.unit]
                new = Length(newValue, len_values[length_combo.current()])
                length_result.set(new)
            else:
                msg.showerror('Error!', 'Please, enter a number and select the desired value!')

        except ValueError or KeyError:
            msg.showerror('Error!', 'Please, enter a number and select the desired value!')


class Weight:
    weight_units = {'Kilograms': 0.001, 'Grams': 1, 'Milligrams': 1000, 'Pounds': 0.00220462}

    def __init__(self, value, unit):
        self.unit = unit
        self.value = value

    def __str__(self):
        return f'{self.value} {self.unit}'

    @staticmethod
    def convert_to():
        try:
            if weight_combo.current() != -1 and weight_var.get() != " ":
                current_weight = Weight(float(weight_entry.get()), weight_var.get())
                newValue = current_weight.value / Weight.weight_units[weight_var.get()] * Weight.weight_units[
                    weight_values[weight_combo.current()]]
                new = Weight(newValue, weight_values[weight_combo.current()])
                weight_result.set(new)
            else:
                msg.showerror('Error!', 'Please, enter a number and select the desired value!')

        except ValueError or KeyError:
            msg.showerror('Error!', 'Please, enter a number and select the desired value!')


class Temperature:

    def __init__(self, value, unit):
        self.unit = unit
        self.value = value

    def __str__(self):
        return f'{self.value} {self.unit}'

    @staticmethod
    def convert_to():
        try:
            if temp_combo.current() != -1 and temp_var.get() != " ":
                current_temp = Temperature(float(temp_entry.get()), temp_var.get())
                if current_temp.unit == 'Celsius':
                    myDict = {}
                    myDict.update({"Celsius": (float(temp_entry.get()))})
                    myDict.update({"Fahrenheit": (float(temp_entry.get()) * 9 / 5 + 32)})
                    myDict.update({"Kelvin": (273.15 + (float(temp_entry.get())))})
                    newValue = myDict[temp_values[temp_combo.current()]]
                    new = Temperature(newValue, temp_values[temp_combo.current()])
                    temp_result.set(new)
                if current_temp.unit == 'Fahrenheit':
                    myDict = {}
                    myDict.update({"Celsius": (float(temp_entry.get()) - 32) * 5 / 9})
                    myDict.update({"Fahrenheit": float(temp_entry.get())})
                    myDict.update({"Kelvin": (273.15 + (float(temp_entry.get()) - 32) * 5 / 9)})
                    newValue = myDict[temp_values[temp_combo.current()]]
                    new = Temperature(newValue, temp_values[temp_combo.current()])
                    temp_result.set(new)
                if current_temp.unit == 'Kelvin':
                    myDict = {}
                    myDict.update({"Celsius": (float(temp_entry.get()) - 273.15)})
                    myDict.update({"Fahrenheit": (float(temp_entry.get()) - 273.15) * 9 / 5 + 32})
                    myDict.update({"Kelvin": float(temp_entry.get())})
                    newValue = myDict[temp_values[temp_combo.current()]]
                    new = Temperature(newValue, temp_values[temp_combo.current()])
                    temp_result.set(new)
            else:
                msg.showerror('Error!', 'Please, enter a number and select the desired value!')
        except ValueError or KeyError:
            msg.showerror('Error!', 'Please, enter a number and select the desired value!')


# საერთო
win = tkinter.Tk()
win.geometry('470x340')
win.title('Conversion Calculator')
win.resizable(width=False, height=False)
win.iconbitmap('icon.ico')

# first tab
ttk.Style().configure('TFrame', background='#FF5C3E', foreground='007CFF')
ttk.Style().configure('TLabel', background='#FF5C3E', foreground='white', bg='white', fg="black")
ttk.Style().configure('TLabelframe', background='#FF5C3E', foreground='#FF5C3E', bg='#FF5C3E', fg="black")
ttk.Style().configure('new.TNotebook', background='white', foreground='#007CFF')
ttk.Style().configure('TRadiobutton', background='#FF5C3E', foreground='white')

# second tab
ttk.Style().configure('second.TFrame', background='#007CFF', foreground='007CFF')
ttk.Style().configure('second.TLabel', background='#007CFF', foreground='white')
ttk.Style().configure('second.TLabelframe', background='#007CFF', foreground='#007CFF', bg='#007CFF', fg="black")
ttk.Style().configure('second.TRadiobutton', background='#007CFF', foreground='white')

nb = ttk.Notebook(win, style='new.TNotebook')

nb.pack(fill='both', expand=1)

tab1 = ttk.Frame(nb, style='TFrame')
nb.add(tab1, text="Length", underline=0)
tab2 = ttk.Frame(nb, style='second.TFrame')
nb.add(tab2, text="Weight", underline=0)
tab3 = ttk.Frame(nb)
nb.add(tab3, text="Temperature", underline=0)

# length
img = tkinter.PhotoImage(file='length.png')
img = img.subsample(3)
ttk.Label(tab1, image=img, compound='center', style='TLabel').pack()
label = ttk.Label(text="Do it!", style='TLabel')
lb_fr = ttk.Labelframe(tab1, height=60, labelwidget=label, style='TLabelframe')
lb_fr.pack(fill='both', expand=1, padx=20, pady=10)

convert_label = ttk.Label(lb_fr, text='Convert', style='new.TLabel')
length_entry = ttk.Entry(lb_fr, width=20)

convert_label.grid(row=0, column=0)
length_entry.grid(row=0, column=1)

length_var = tkinter.StringVar()
length_var.set(" ")
metres = ttk.Radiobutton(lb_fr, text='Meter', value='Meter', variable=length_var, style='TRadiobutton')
centimetres = ttk.Radiobutton(lb_fr, text='Centimeter', value='Centimeter', variable=length_var,
                              style='TRadiobutton')
kilometres = ttk.Radiobutton(lb_fr, text='Kilometer', value='Kilometer', variable=length_var, style='TRadiobutton')
millimetres = ttk.Radiobutton(lb_fr, text='Millimeter', value='Millimeter', variable=length_var,
                              style='TRadiobutton')

metres.grid(row=1, column=1, sticky='w')
centimetres.grid(row=2, column=1, sticky='w')
kilometres.grid(row=3, column=1, sticky='w')
millimetres.grid(row=4, column=1, sticky='w')

to_label = tkinter.Label(lb_fr, text="To", width=10, background='#FF5C3E', foreground='white')
to_label.grid(row=0, column=3, sticky='e')

len_var = 'აირჩიეთ მნიშვნელობა'
len_values = ['Meter', 'Centimeter', 'Kilometer', 'Millimeter']
length_combo = ttk.Combobox(lb_fr, text=len_var, state='readonly', width=20, values=len_values)

length_combo.grid(row=0, column=4)

tkinter.Button(lb_fr, width=30, text='Convert',
               command=Length.convert_to, background='#007CFF').grid(row=2, column=3, columnspan=2, sticky='e')

question_img = tkinter.PhotoImage(file='question.png')
question_img = question_img.subsample(60)

balloon = Pmw.Balloon(lb_fr)


def show_length(i):
    length_result.set(i)


meter_question = tkinter.Button(lb_fr, image=question_img, background='#007CFF',
                                command=lambda: show_length("1 Meter = 100 Centimetres"))
meter_question.grid(row=1, column=0)
balloon.bind(meter_question, "1 Meter = 100 Centimetres")

centi_question = tkinter.Button(lb_fr, image=question_img, background='#007CFF',
                                command=lambda: show_length("1 Centimeter = 0,01 Meter"))
centi_question.grid(row=2, column=0)
balloon.bind(centi_question, "1 Centimeter = 0,01 Meter")

kilo_question = tkinter.Button(lb_fr, image=question_img, background='#007CFF',
                               command=lambda: show_length("1 Kilometer = 1000 Meter"))
kilo_question.grid(row=3, column=0)
balloon.bind(kilo_question, "1 Kilometer = 1000 Meter")

milli_question = tkinter.Button(lb_fr, image=question_img, background='#007CFF',
                                command=lambda: show_length("1 Millimeter = 0,001 Meter"))
milli_question.grid(row=4, column=0)
balloon.bind(milli_question, "1 Millimeter = 0,001 Meter")

length_result = tkinter.StringVar()

ttk.Label(lb_fr, textvariable=length_result, background='#FF5C3E', foreground='white').grid(row=4, column=3,
                                                                                            columnspan=2)


def length_number_entry(event):
    Length.convert_to()


length_entry.bind('<Return>', length_number_entry)

# weight

weight_img = tkinter.PhotoImage(file='weight.png')
weight_img = weight_img.subsample(3)
ttk.Label(tab2, image=weight_img, compound='center', style='second.TLabel').pack()
label2 = ttk.Label(text="Do it!", style='second.TLabel')
lb_fr2 = ttk.Labelframe(tab2, labelwidget=label2, height=60, style='second.TLabelframe')
lb_fr2.pack(fill='both', expand=1, padx=20, pady=10)

convert_label = tkinter.Label(lb_fr2, text='Convert', background='#007CFF', foreground='white')
weight_entry = tkinter.Entry(lb_fr2, width=20)

convert_label.grid(row=0, column=0)
weight_entry.grid(row=0, column=1)

weight_var = tkinter.StringVar()
weight_var.set(" ")
kilograms = ttk.Radiobutton(lb_fr2, text='Kilograms', value='Kilograms', variable=weight_var,
                            style='second.TRadiobutton')
grams = ttk.Radiobutton(lb_fr2, text='Grams', value='Grams', variable=weight_var, style='second.TRadiobutton')
milligrams = ttk.Radiobutton(lb_fr2, text='Milligrams', value='Milligrams', variable=weight_var,
                             style='second.TRadiobutton')
pounds = ttk.Radiobutton(lb_fr2, text='Pounds', value='Pounds', variable=weight_var, style='second.TRadiobutton')

kilograms.grid(row=1, column=1, sticky='w')
grams.grid(row=2, column=1, sticky='w')
milligrams.grid(row=3, column=1, sticky='w')
pounds.grid(row=4, column=1, sticky='w')

weight_to = tkinter.Label(lb_fr2, text="To", width=8, background='#007CFF', foreground='white')
weight_to.grid(row=0, column=3, sticky='e')

weight_values = ['Kilograms', 'Grams', 'Milligrams', 'Pounds']
weight_combo = ttk.Combobox(lb_fr2, state='readonly', width=22, values=weight_values)

weight_combo.grid(row=0, column=4)

tkinter.Button(lb_fr2, width=30, text='Convert',
               command=Weight.convert_to, background='#FF5C3E').grid(row=2, column=3, columnspan=2, sticky='e')

weight_result = tkinter.StringVar()

ttk.Label(lb_fr2, textvariable=weight_result, style='second.TLabel').grid(row=4, column=3, columnspan=2)


def show_weight(i):
    weight_result.set(i)


kilo_question = tkinter.Button(lb_fr2, image=question_img, background='#007CFF',
                               command=lambda: show_weight("1 Kilogram = 1000 Grams"))
kilo_question.grid(row=1, column=0)
balloon.bind(kilo_question, "1 Kilogram = 1000 Grams")

gram_question = tkinter.Button(lb_fr2, image=question_img, background='#007CFF',
                               command=lambda: show_weight("1 Gram = 0,001 Kilogram"))
gram_question.grid(row=2, column=0)
balloon.bind(gram_question, "1 Gram = 0,001 Kilogram")

milli_question = tkinter.Button(lb_fr2, image=question_img, background='#007CFF',
                                command=lambda: show_weight("1 Gram = 0,001 Kilogram"))
milli_question.grid(row=3, column=0)
balloon.bind(milli_question, "1 Gram = 0,001 Kilogram")

pounds_question = tkinter.Button(lb_fr2, image=question_img, background='#007CFF',
                                 command=lambda: show_weight("1 Pound = 0,454 Kilogram"))
pounds_question.grid(row=4, column=0)
balloon.bind(pounds_question, "1 Pound = 0,454 Kilogram")


def weight_number_entry(event):
    Weight.convert_to()


weight_entry.bind('<Return>', weight_number_entry)

# temperature

temperature_img = tkinter.PhotoImage(file='termo.png')
temperature_img = temperature_img.subsample(3)
ttk.Label(tab3, image=temperature_img, compound=tkinter.RIGHT, style='TLabel').pack(side='left', fill='y')
label3 = ttk.Label(text="Do it!", style='TLabel')
lb_fr3 = ttk.Labelframe(tab3, labelwidget=label3, height=60)
lb_fr3.pack(fill='both', expand=1, padx=20, pady=10)

convert_label = tkinter.Label(lb_fr3, text='Convert', background='#FF5C3E', foreground='white')
temp_entry = tkinter.Entry(lb_fr3, width=20)

convert_label.grid(row=0, column=0)
temp_entry.grid(row=0, column=1)

temp_var = tkinter.StringVar()
temp_var.set(" ")
fahrenheit = ttk.Radiobutton(lb_fr3, text='Celsius', value='Celsius', variable=temp_var, style='TRadiobutton')
celsius = ttk.Radiobutton(lb_fr3, text='Fahrenheit', value='Fahrenheit', variable=temp_var, style='TRadiobutton')
kelvin = ttk.Radiobutton(lb_fr3, text='Kelvin', value='Kelvin', variable=temp_var, style='TRadiobutton')

fahrenheit.grid(row=1, column=1, sticky='w', pady=10)
celsius.grid(row=2, column=1, sticky='w', pady=10)
kelvin.grid(row=3, column=1, sticky='w', pady=10)

to_label = tkinter.Label(lb_fr3, text="To", width=8, background='#FF5C3E', foreground='white')
to_label.grid(row=4, column=0, sticky='e', pady=10)

temp_values = ['Celsius', 'Fahrenheit', 'Kelvin']
temp_combo = ttk.Combobox(lb_fr3, state='readonly', width=22, values=temp_values)

temp_combo.grid(row=4, column=1)

tkinter.Button(lb_fr3, width=20, text='Convert', command=Temperature.convert_to, background='#007CFF'). \
    grid(row=5, column=0, columnspan=2, pady=10, sticky='e')
temp_result = tkinter.StringVar()

ttk.Label(lb_fr3, textvariable=temp_result).grid(row=6, column=0, columnspan=2, sticky='n', pady=10, )


def temp_number_entry(event):
    Temperature.convert_to()


def show_temp(i):
    temp_result.set(i)


temp_entry.bind('<Return>', temp_number_entry)

celsius_question = tkinter.Button(lb_fr3, image=question_img, background='#007CFF',
                                  command=lambda: show_temp("0 Celsius = 32 Fahrenheit"))
celsius_question.grid(row=1, column=0)
balloon.bind(celsius_question, "0 Celsius = 32 Fahrenheit")

fahren_question = tkinter.Button(lb_fr3, image=question_img, background='#007CFF',
                                 command=lambda: show_temp("0 Fahrenheit = -17,8 Celsius"))
fahren_question.grid(row=2, column=0)
balloon.bind(fahren_question, "0 Fahrenheit = -17,8 Celsius")

kelvin_question = tkinter.Button(lb_fr3, image=question_img, background='#007CFF',
                                 command=lambda: show_temp("0 Kelvin = -273,15 Celsius"))
kelvin_question.grid(row=3, column=0)
balloon.bind(kelvin_question, "0 Kelvin = -273,15 Celsius")

win.mainloop()
