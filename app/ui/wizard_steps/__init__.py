# This file makes app/ui/wizard_steps a Python package
# It can also be used for package-level imports if needed later.

# For now, ensure wizard_data and its sub-dictionaries are initialized early if not present
# This could be done in main_page or here if these modules are imported early.
# It's generally better to initialize in main_page before the UI elements that bind to it are created.
# from nicegui import app
#
# def init_wizard_storage():
#     if 'wizard_data' not in app.storage.user:
#         app.storage.user['wizard_data'] = {}
#     if 'additional_features' not in app.storage.user['wizard_data']:
#         app.storage.user['wizard_data']['additional_features'] = {}
#
# # init_wizard_storage() # Call it if this __init__ is guaranteed to run before UI bindings.
# # Safer to do in main_page.
