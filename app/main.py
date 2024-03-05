from nicegui import ui

from gui.knowlagde_base import knpwlegde
from gui.new_game import new_game
from gui.upload_files import upload_files

ui.add_head_html('''
<style>
.zoom {
  padding: 10px;
  background-color: green;
  transition: transform .3s;
  margin: 0 auto;
  z-index: 1;
}

.zoom:hover {
  transform: scale(1.1); /* (150% zoom - Note: if the zoom is too large, it will go outside of the viewport) */
  z-index: 2;
}

.text-subtitle {
  font-size: .675rem;
  font-weight: 500;
  line-height: 1.375rem;
  letter-spacing: .00714em;
  color: grey;
}
</style>
''', shared=True)

# from app.gui.dashboard import dashboard
# from app.gui.new_game import new_game
# from app.gui.upload_files import upload_files
from gui.war_game import war_game, dashboard


@ui.page('/vault')
def vault_page():
    dashboard()
    knpwlegde()


#
@ui.page('/new_game')
def new_game_page():
    dashboard()
    new_game()


#
#
@ui.page('/')
def wargame_page():
    dashboard()
    war_game()


#
#
@ui.page('/config')
def upload_files_page():
    dashboard()
    upload_files()


#
# state = {
#     "team": {
#         "red": 50,
#         "blue": 50
#     },
#     "number": 1
# }
#
# ui.slider(min=1, max=1000).bind_value(state["team"], 'red')
#
#
# # change the value to random number
# def random_number(args):
#     global state
#     state["team"]['red'] += 100
#     print(state["team"]['red'])
#
#
# ui.button("Send message", on_click=random_number)
#
# state = {
#     "winning": {
#         "land": 0.2,
#         "sea": 0.8
#     }
# }
# #
# #
# # def create_bar_chart(domain):
# #     ui.linear_progress(color="red", show_value=False).style('height: 20px; margin: 10px;').style(
# #         f'background-color: blue;').bind_value(state["winning"], domain)
# #
# #
# # create_bar_chart("land")
# # create_bar_chart("sea")
# #
# #
# # def modify():
# #     state["winning"]["land"] += 0.1
# #     state["winning"]["sea"] += 0.1
# #     print(state["winning"]["land"])
# #
# #
# # # ui.button("update", on_click=lambda x: state["winning"].update({"land": 0.5}))
# # # ui.button("update", on_click=modify)


# ui.add_head_html('''
# <style>
# .zoom {
#   padding: 10px;
#   background-color: green;
#   transition: transform .3s;
#   margin: 0 auto;
#   z-index: 1;
# }
#
# .zoom:hover {
#   transform: scale(1.1); /* (150% zoom - Note: if the zoom is too large, it will go outside of the viewport) */
#   z-index: 2;
# }
#
# .text-subtitle {
#   font-size: .675rem;
#   font-weight: 500;
#   line-height: 1.375rem;
#   letter-spacing: .00714em;
#   color: grey;
# }
# </style>
# ''')

ui.run()
