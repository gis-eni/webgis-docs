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