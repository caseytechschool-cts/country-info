import PySimpleGUI as sg
from layout import layout_builder
from core_logic import core
from display_handler import update_display, clear_display


def country_info():
    layout = layout_builder()
    window = sg.Window('Country info finder', layout, element_justification='c')
    while True:
        event, values = window.read()
        print(event)
        if event == sg.WIN_CLOSED or event == '-exit-':
            break
        if event == 'GO':
            data = core(values['-country_name-'])
            if data.status_code == 200:
                update_display(data, window)

        if event == '-clear-':
            clear_display(window)

    window.close()


if __name__ == '__main__':
    country_info()

