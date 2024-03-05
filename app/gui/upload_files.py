import json
import math
import os
import shutil
from nicegui import ui, events

from resources import Dictionary
from resources.map_data import MapDatabaseDatabase


def upload_files():
    with ui.tabs().classes('w-full') as tabs:
        two = ui.tab('Units')
        three = ui.tab('Types')
        four = ui.tab('Map data')
    with ui.tab_panels(tabs, value=two).classes('w-full'):
        with ui.tab_panel(two):
            ui.aggrid({
                'columnDefs': [
                    {'field': 'domain', 'filter': 'agTextColumnFilter', 'floatingFilter': True},
                    {'field': 'name', 'filter': 'agTextColumnFilter', 'floatingFilter': True},
                    {'field': 'description', 'filter': 'agTextColumnFilter', 'floatingFilter': True},

                ],
                'rowData': Dictionary.get_json_units(),
                ':getRowId': '(params) => params.data.name',

            })

        with ui.tab_panel(three):

            json_obj = Dictionary.get_json_types()
            json_list = [{'type': key, 'description': value} for key, value in json_obj.items()]
            ui.aggrid({
                'columnDefs': [
                    {'field': 'type', 'filter': 'agTextColumnFilter', 'floatingFilter': True},
                    {'field': 'description', 'filter': 'agTextColumnFilter', 'floatingFilter': True},

                ],
                'rowData': json_list,
                ':getRowId': '(params) => params.data.name',
            })
        with ui.tab_panel(four):
            edit1 = ui.json_editor({'content': {'json': MapDatabaseDatabase.get_all()}})
            edit1.style('height: 100%').style('width: 100%')
            edit1.run_editor_method('updateProps', {'readOnly': True})
            edit1.run_editor_method(':expand', 'path => true')

# def upload_files():
#     def bytes_to_kilobytes(bytes_size):
#         return f"{math.ceil(bytes_size / 1024)} kB"
#
#     async def show_file_editor():
#         file_name = await grid.get_selected_rows()
#         file_path = f"../uploads/{file_name[0]['Name']}"
#         try:
#             with open(file_path, 'r') as file:
#                 file_contents = file.read()
#                 # print(file_contents)
#                 update_file['visible'] = True
#                 file_content.value = file_contents
#         except Exception as e:
#             ui.notify(f"Error reading file '{file_path}': {str(e)}")
#
#     # def copy_file(source_file):
#     #     try:
#     #         shutil.copy(source_file, "../uploads")
#     #         ui.notify(f"File {source_file} loaded")
#     #     except Exception as e:
#     #         ui.notify(f"An error occurred while copying the file: {e}")
#
#     async def delete_selected_item() -> None:
#         directory = '../uploads'
#         for file_info in await grid.get_selected_rows():
#             filename = file_info['Name']
#             filepath = os.path.join(directory, filename)
#             if os.path.exists(filepath):
#                 os.remove(filepath)
#                 ui.notify(f"File '{filename}' deleted successfully.")
#                 # update_grid()
#                 grid.remove(filename)
#                 grid.update()
#                 ui.update(grid)
#             else:
#                 print(f"File '{filename}' does not exist.")
#
#     def get_files_data():
#         folder_path = "../uploads"
#         files_data = []
#         for filename in os.listdir(folder_path):
#             file_path = os.path.join(folder_path, filename)
#             # Check if the path is a file (not a directory)
#             if os.path.isfile(file_path):
#                 file_size = os.path.getsize(file_path)
#                 files_data.append({'Name': filename, 'Size': bytes_to_kilobytes(file_size)})
#         return files_data
#
#     def update_grid():
#         grid.options['rowData'] = get_files_data()
#         grid.update()
#         ui.update(grid)

# async def upload_file():
#     result = await local_file_picker('/', multiple=True)
#     copy_file(result[0])
#     update_grid()

# ui.button("Upload file", on_click=upload_file)
# def handle_upload(e: events.UploadEventArguments):
#     text = e.content.read().decode('utf-8')
#     content.set_content(text)
#     dialog.open()
#
# ui.upload(on_upload=handle_upload)
# with ui.dialog().props('full-width') as dialog:
#     with ui.card():
#         content = ui.markdown()

# def handle_upload(e: events.UploadEventArguments):
#     filepath = f"../uploads/{e.name}"
#     text = e.content.read().decode('utf-8')
#     print(e)
#     content.set_content(text)
#     dialog.open()
# with open(filepath, 'w', encoding='utf-8') as f:
#     Write the content of the 'text' variable to the file
# f.write(text)
# update_grid()

# def parse_resource_data(filepath):
#     data = [] #get_resource_data(filepath)
#     data_list = []
#     for id, text in data.items():
#         data_list.append({'type': id, 'description': text})
#     return data_list


# with ui.tab_panel(one):
# with ui.tab_panels(tabs, value=one).classes('w-full'):
# with ui.tab_panel(one):
#     ui.upload(on_upload=handle_upload).classes('max-w-full')
#     ui.label("Uploaded files").style("font-weight: bold;")
# grid = ui.aggrid({
#     'columnDefs': [
#         {'field': 'Name', 'checkboxSelection': True, 'filter': 'agTextColumnFilter',
#          'floatingFilter': True},
#         {'field': 'Size', 'filter': 'agNumberColumnFilter', 'floatingFilter': True},
#     ],
#     'rowData': get_files_data(),
#     ':getRowId': '(params) => params.data.name',
#     'rowSelection': 'multiple',
#
# })
# ui.button('Delete',
#           on_click=delete_selected_item)
# update_file = {'visible': False}
# ui.button('Show content',
#           on_click=show_file_editor)
# file_content = ui.editor(value='').bind_visibility(update_file)

# with ui.tab_panel(five):
#     edit2 = ui.json_editor({'content': {'json': get_resource_data("/app/resources/external.json")}})
#     edit2.run_editor_method('updateProps', {'readOnly': True})
#     edit2.run_editor_method(':expand', 'path => true')
