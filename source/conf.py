from datetime import datetime

# pylint: disable=W0622

project = 'Dog ACE - Health Protocol'
copyright = f'{datetime.now().year}, Rath'
author = 'Rath Pascal'
extensions = ['piccolo_theme']
templates_path = ['_templates']
exclude_patterns = []
html_theme = 'piccolo_theme'
html_theme_options = {}
html_static_path = ['_static']
html_css_files = ['css/wiki.css']
master_doc = 'index'
display_version = True
sticky_navigation = True
# html_logo = '_static/img/icon.png'
# html_favicon = 'img/icon.png'
