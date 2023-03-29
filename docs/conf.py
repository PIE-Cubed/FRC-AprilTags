# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os, sys
# sys.path.insert(0, os.path.abspath("."))
import frc_apriltags


# -- Project information -----------------------------------------------------

project   = "FRC-AprilTags"
copyright = "2022 - 2023, Alex Pereira, the Robo-Lions, and PIE3"
author    = "Alex Pereira, the Robo-Lions, and PIE3"
version   = frc_apriltags.__version__


# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx_tabs.tabs",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.duration",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
]

intersphinx_mapping = {
    "rtd": ("https://docs.readthedocs.io/en/stable/", None),
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

html_theme_options = {
    #'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
    'analytics_anonymize_ip': True,
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'vcs_pageview_mode': '',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
}

# The master toctree document.
master_doc = "index"

# The suffix of source filenames.
source_suffix = ".rst"

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title     = "FRC-AprilTags"
epub_author    = "Alex Pereira"
epub_publisher = "PIE3"
epub_copyright = "2022-2023, Alex Pereira, the Robo-Lions, and PIE3"

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
