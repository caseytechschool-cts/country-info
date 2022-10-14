import PySimpleGUI as sg


def layout_builder():
    return [[sg.Input(key='-country_name-'), sg.Button('GO', bind_return_key=True)],
            [sg.pin(sg.Text(key='-capital-', text='Capital:', visible=False))],
            [sg.pin(sg.Text(key='-area-', text='Area:', visible=False))],
            [sg.pin(sg.Text(key='-population-', text='Population:', visible=False))],
            [sg.pin(sg.Text(key='-car-driven-', text='Car driven:', visible=False))],
            [sg.pin(sg.Text(key='-week-', text='Start of week:', visible=False))],
            [sg.pin(sg.Button('Clear', visible=False, key='-clear-')), sg.pin(sg.Button('Exit', visible=False, key='-exit-'))]]
