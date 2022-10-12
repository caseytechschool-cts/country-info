import PySimpleGUI as sg
import requests

# step 1: creating the layout

layout = [[sg.Input(key='-country_name-'), sg.Button('GO')],
          [sg.Text(key='-capital-', text='Capital:', visible=False)],
          [sg.Text(key='-area-', text='Area:', visible=False)],
          [sg.Text(key='-population-', text='Population:', visible=False)],
          [sg.Text(key='-car-driven-', text='Car driven:', visible=False)],
          [sg.Text(key='-week-', text='Start of week:', visible=False)],
          [sg.Button('Clear', visible=False, key='-clear-'), sg.Button('Exit',visible=False, key='-exit-')]]

window = sg.Window('Country info finder', layout, element_justification='c')

while True:
    event, values = window.read()
    print(event)
    if event == sg.WIN_CLOSED or event == '-exit-':
        break
    if event == 'GO':
        url = f"https://restcountries.com/v3.1/name/{values['-country_name-']}?fullText=true"
        data = requests.get(url)
        if data.status_code == 200:
            formatted_data = data.json()
            capital = formatted_data[0]['capital'][0]
            area = formatted_data[0]['area']
            car_driven = formatted_data[0]['car']['side']
            population = formatted_data[0]['population']
            week = formatted_data[0]['startOfWeek']

            window['-capital-'].update(value=f'Capital:{capital}', visible=True)
            window['-area-'].update(value=f'Area:{area}', visible=True)
            window['-population-'].update(value=f'Population:{population}', visible=True)
            window['-car-driven-'].update(value=f'Car driven:{car_driven}', visible=True)
            window['-week-'].update(value=f'Start of week:{week}', visible=True)

            window['-clear-'].update(visible=True)
            window['-exit-'].update(visible=True)

window.close()

