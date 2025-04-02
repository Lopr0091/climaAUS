# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Clima'
copyright = '2025, Yo'
author = 'Yo'
release = 'dev'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

import os
import sys


sys.path.insert(0, os.path.abspath("../../src/clima"))
print("PYTHONPATH:", sys.path)


project = "climaAUS"
author = "Tu Nombre"
release = "0.1"

extensions = [
    "sphinx.ext.autodoc",   
    "sphinx.ext.napoleon",  # estilo Google/Numpy
    "sphinx.ext.viewcode",  # enlaces al código fuente
]

html_theme = "sphinx_rtd_theme"
