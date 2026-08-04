# Configuration file for the Sphinx documentation builder.

project = "WebGIS"
copyright = "2026, ENIE"
author = "ENIE"
release = "2026"

extensions = ["sphinx.ext.todo"]
todo_include_todos = True

templates_path = ["_templates"]
language = "en"
exclude_patterns = []

html_theme = "piccolo_theme"
html_static_path = ["_static"]

html_js_files = ["js/eni.js"]
html_css_files = ["css/eni.css"]

# Short title shown in the top navigation bar (matches the tile on the docs landing page)
html_short_title = "WebGIS for Admins"

# Used by _templates/layout.html to build the home link and the DE/EN language switch
html_context = {"doc_root_folder": "webgis"}