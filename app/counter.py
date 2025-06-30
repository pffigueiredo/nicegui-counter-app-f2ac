from nicegui import ui

def create():
    @ui.page('/')
    def page():
        with ui.column().classes('items-center justify-center min-h-screen gap-8'):
            # Counter display
            counter_label = ui.label('0').classes('text-6xl font-bold text-blue-600')
            
            # Buttons container
            with ui.row().classes('gap-4'):
                ui.button('Decrement', on_click=lambda: update_counter(-1)).classes('px-6 py-3 bg-red-500 hover:bg-red-600')
                ui.button('Reset', on_click=lambda: reset_counter()).classes('px-6 py-3 bg-gray-500 hover:bg-gray-600')
                ui.button('Increment', on_click=lambda: update_counter(1)).classes('px-6 py-3 bg-green-500 hover:bg-green-600')
        
        # Counter state
        counter_value = 0
        
        def update_counter(change: int):
            nonlocal counter_value
            counter_value += change
            counter_label.set_text(str(counter_value))
        
        def reset_counter():
            nonlocal counter_value
            counter_value = 0
            counter_label.set_text('0')