import PySimpleGUI as sg


def layout_builder():
    return [[sg.Input(key='-country_name-'), sg.Button('GO')],
            [sg.Text(key='-capital-', text='Capital:', visible=False)],
            [sg.Text(key='-area-', text='Area:', visible=False)],
            [sg.Text(key='-population-', text='Population:', visible=False)],
            [sg.Text(key='-car-driven-', text='Car driven:', visible=False)],
            [sg.Text(key='-week-', text='Start of week:', visible=False)],
            [sg.Button('Clear', visible=False, key='-clear-'), sg.Button('Exit', visible=False, key='-exit-')]]
