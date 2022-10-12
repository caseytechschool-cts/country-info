def update_display(data, window):
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


def clear_display(window):
    window['-capital-'].update(visible=False)
    window['-area-'].update(visible=False)
    window['-population-'].update(visible=False)
    window['-car-driven-'].update(visible=False)
    window['-week-'].update(visible=False)

    window['-clear-'].update(visible=False)
    window['-exit-'].update(visible=False)