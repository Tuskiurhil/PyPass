#!/usr/bin/env python3

import PySimpleGUI as sg, random, string

def generate_password(total_length, upper, lower, digits, symbols):
    set = []
    if upper == '1':
        set.append(string.ascii_uppercase)
    if lower == '1':
        set.append(string.ascii_lowercase)
    if digits == '1':
        set.append(string.digits)
    if symbols == '1':
        set.append(string.punctuation)
    selection = ''.join(set)
    password = ''.join([random.SystemRandom().choice(selection) for _ in range(total_length)])
    print( password)
    
def main():
    sg.theme('dark grey 5')

    layout = [[sg.Text('Uppercase letters'), sg.Push(), sg.Checkbox("", default=True, key="-UPPER-")],
                [sg.Text('Lowercase letters'), sg.Push(), sg.Checkbox("", default=True, key="-LOWER-")],
                [sg.Text('Digits'), sg.Push(), sg.Checkbox("", default=True, key="-DIGITS-")],
                [sg.Text('Symbols'), sg.Push(), sg.Checkbox("", default=True, key="-SYMBOLS-")],
                [sg.Text('Password Length'), sg.Push(), sg.Slider(range=(4, 128), orientation='h', size=(20, 8), default_value=8, k='-LENGTH-')],
                    [sg.Button('Generate Password'), sg.Cancel()]]      

    window = sg.Window('Password Generator', layout)    

    event, values = window.read()  

    while True:
        if event == "Generate Password":
            if values["-UPPER-"] == True:
                upper = "1"
            elif values["-UPPER-"] == False:
                upper = "0"
            if values["-LOWER-"] == True:
                lower = "1"
            elif values["-LOWER-"] == False:
                lower = "0"
            if values["-DIGITS-"] == True:
                digits = "1"
            elif values["-DIGITS-"] == False:
                digits = "0"
            if values["-SYMBOLS-"] == True:
                symbols = "1"
            elif values["-SYMBOLS-"] == False:
                symbols = "0"
            total_length = int(values['-LENGTH-'])
            print('Creating a '+str(total_length)+' character long password')
            generate_password(total_length, upper, lower, digits, symbols)
            break
        if event == sg.WINDOW_CLOSED or event == 'Quit' or event == 'Cancel':
            break
            window.close()

if __name__ == '__main__':
    main()