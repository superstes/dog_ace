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
html_logo = '_static/img/2023-04_portrait.png'
# html_favicon = 'img/icon.png'

import os
if not os.path.exists('./git-lfs'):
    os.system('wget https://github.com/git-lfs/git-lfs/releases/download/v2.7.1/git-lfs-linux-amd64-v2.7.1.tar.gz')
    os.system('tar xvfz git-lfs-linux-amd64-v2.7.1.tar.gz')
    os.system('./git-lfs install')
    os.system('./git-lfs fetch')
    os.system('./git-lfs checkout')
