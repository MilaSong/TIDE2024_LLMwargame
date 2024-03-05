from nicegui import ui

values = {
    'attacker': 'a',
    'target': 'b'
}
sel = ui.select(options=['a', 'b', 'c'], new_value_mode='add-unique', label='Select unit', with_input=True).classes(
    'w-full').bind_value_to(values,
                            'attacker')

ui.button("Print", on_click=lambda x: print(sel.value)).classes('w-full')

ui.run()
