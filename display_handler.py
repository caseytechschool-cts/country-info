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

    window['-capital-'].unhide_row()
    window['-area-'].unhide_row()
    window['-population-'].unhide_row()
    window['-car-driven-'].unhide_row()
    window['-week-'].unhide_row()
    window['-clear-'].unhide_row()
    window['-exit-'].unhide_row()


def clear_display(window):
    window['-capital-'].hide_row()
    window['-area-'].hide_row()
    window['-population-'].hide_row()
    window['-car-driven-'].hide_row()
    window['-week-'].hide_row()
    window['-clear-'].hide_row()
    window['-exit-'].hide_row()
    # window['-capital-'].update(visible=False)
    # window['-area-'].update(visible=False)
    # window['-population-'].update(visible=False)
    # window['-car-driven-'].update(visible=False)
    # window['-week-'].update(visible=False)

    # window['-clear-'].update(visible=False)
    # window['-exit-'].update(visible=False)