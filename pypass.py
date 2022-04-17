#!/usr/bin/env python3

import PySimpleGUI as sg, random, string, pyperclip

def generate_password(total_length, upper, lower, digits, symbols, clipb):
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
    print(password)
    if clipb == '1':
        sg.popup(password+'\nPassword copied to clipboard')
        pyperclip.copy(password)
    elif clipb == '0':
        sg.popup(password)
    
def main():
    passstrength = "Weak"
    sg.theme('dark grey 5')

    layout = [[sg.Text('Uppercase letters'), sg.Push(), sg.Checkbox("", default=True, key="-UPPER-")],
                [sg.Text('Lowercase letters'), sg.Push(), sg.Checkbox("", default=True, key="-LOWER-")],
                [sg.Text('Digits'), sg.Push(), sg.Checkbox("", default=True, key="-DIGITS-")],
                [sg.Text('Symbols'), sg.Push(), sg.Checkbox("", default=True, key="-SYMBOLS-")],
                [sg.Text('Password Length'), sg.Push(), sg.Slider(range=(4, 128), orientation='h', size=(20, 8), default_value=8, k='-LENGTH-')],
                [sg.Text('Copy Password to Clipboard?'), sg.Push(), sg.Checkbox('', key="-CLIPBOARD-")],
                [sg.Text('Password Strength: '), sg.InputText(passstrength, key="-PWSTRENGTH-", readonly=False, size=(11,1), background_color="red")],
                    [sg.Button('Generate Password'), sg.Cancel(), sg.Push(), sg.Button('?')]]      

    window = sg.Window('PyPass - Password Generator', layout)    

      

    while True:
        
        event, values = window.read(timeout=10)
        if int(values['-LENGTH-']) < 8:
            window['-PWSTRENGTH-'].update("Very Weak", background_color="purple")
        if int(values['-LENGTH-']) >= 10:
            window['-PWSTRENGTH-'].update("Weak", background_color="red")
        if int(values['-LENGTH-']) >= 12:
            window['-PWSTRENGTH-'].update("Average", background_color="yellow")
        if int(values['-LENGTH-']) >= 16:
            window['-PWSTRENGTH-'].update("Strong", background_color="lime")
        if int(values['-LENGTH-']) >= 24:
            window['-PWSTRENGTH-'].update("Very Strong", background_color="green")

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
            if values["-CLIPBOARD-"] == True:
                clipb = "1"
            elif values["-CLIPBOARD-"] == False:
                clipb = "0"
            total_length = int(values['-LENGTH-'])
            print('Creating a '+str(total_length)+' character long password')
            generate_password(total_length, upper, lower, digits, symbols, clipb)
            break
        if event == sg.WINDOW_CLOSED or event == 'Quit' or event == 'Cancel':
            break
            window.close()
        if event == '?':
            sg.Popup("PyPass - A Python3 Password Generator\n\nby Colditz Colligula\n\nVersion 0.2", title='About PyPass')

if __name__ == '__main__':
    main()