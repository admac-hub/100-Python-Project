"""
    The Official Python GUI Programming with PySimpleGUI Course

"""
# 1 - Import

import PySimpleGUI as sg

# 2 - Layout
# this is what define the interior of the window 

sg.set_options(font='Default 18', keep_on_top=True)

layout = [
            [sg.Text('Hello, World!')],
            [sg.Text('Hello, World!')],
            [sg.Button('Ok')],
         ]

# 3 - Window

window = sg.Window('Title', layout)

# 4 - Event loop / handling

event, values = window.read()

# 5 - Close
window.close()



'''
In a gui are this things called row and on a row we have this things called widgets.

if we talking for element that i`m refering to GUI, if we talk for widgets then i know it`s tkinter or Qt , ot some underlying framework
'''


