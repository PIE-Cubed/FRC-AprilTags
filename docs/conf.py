# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Imports
import frc_apriltags

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

#
import sys

if sys.version_info >= (3, 8):
    from importlib import metadata

assert metadata.version('pip') >= '1.2.0'

#

project = 'FRC-AprilTags'
copyright = '2023, Alex Pereira, Members of the Robo-Lions, and PIE3'
author = 'Alex Pereira, Members of the Robo-Lions, and PIE3'
release = frc_apriltags.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
