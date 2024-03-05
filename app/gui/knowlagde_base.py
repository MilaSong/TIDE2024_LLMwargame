import math
import os

from tika import parser
from nicegui import ui
from nicegui.events import UploadEventArguments

from resources.file_knowlage import ExternalFileDatabase


def read_from_with_tika(raw_file):
    """
    Read the content of a file using tika
    :param raw_file:
    :return:
    """
    parsed = parser.from_buffer(raw_file)
    return parsed['content']


async def handle_upload(e: UploadEventArguments):
    try:
        text_byte = e.content.read()
        text_raw = read_from_with_tika(text_byte)
    except Exception as e:
        raise Exception(f"Error reading file: {str(e)}")

    if not text_raw or len(text_raw) < 10:
        raise Exception("Error reading file: empty content")
    try:
        await ExternalFileDatabase.add(text_raw)
    except Exception as e:
        ui.notify(f"Error adding file: {str(e)}", type='error')


def knpwlegde():
    async def delete_selected_item() -> None:
        print("Deleting selected items")
        for file_info in await create_grid.get_selected_rows():
            hash_code = file_info['hash']
            print(f"Deleting file with hash: {hash_code}")
            ExternalFileDatabase.delete(hash_code)
            create_grid.refresh()

    with ui.expansion(f"File upload", icon='file').classes('w-full').classes("border-2 border-gray-200").style(
            "background-color: #f3f4f6;"):
        ui.label("Files to process").style("font-weight: bold;")
        ui.label("Select files to process and uadd them to knowledge base")
        ui.upload(on_upload=lambda e: handle_upload(e),
                  on_rejected=lambda: ui.notify('Rejected!'),
                  max_file_size=10_000_000).classes('max-w-full')

    ui.label("Knowledge base files").style("font-weight: bold;")

    with ui.row():
        ui.button('Delete', on_click=delete_selected_item)

    @ui.refreshable
    def create_grid():
        grid = ui.aggrid({
            'columnDefs': [
                {'name': 'hash', 'label': 'ID', 'field': 'hash', 'sortable': True, 'searchable': True, 'align': 'left'},
                {'field': 'domains', 'filter': 'agSetColumnFilter', 'floatingFilter': True, "editable": True},
                {'field': 'country', 'filter': 'agSetColumnFilter', 'floatingFilter': True, "editable": True},
                {'field': 'category', 'filter': 'agSetColumnFilter', 'floatingFilter': True, "editable": True},
                {'field': 'paragraph', 'filter': 'agTextColumnFilter', 'floatingFilter': True, "editable": True,
                 "cellEditor": 'agLargeTextCellEditor'},
                {'field': 'summary', 'filter': 'agTextColumnFilter', 'floatingFilter': True, "editable": True,
                 "cellEditor": 'agLargeTextCellEditor'}
            ],
            'rowData': ExternalFileDatabase.get_all(),
            ':getRowId': '(params) => params.data.name',
            'rowSelection': 'multiple',
            'stopEditingWhenCellsLoseFocus': True
        })

    create_grid()


