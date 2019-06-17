# -*- coding: utf-8 -*-

extensions = ['recommonmark']
templates_path = [
    '/home/docs/checkouts/readthedocs.org/readthedocs/templates/sphinx',
    'templates', '_templates', '.templates']
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
master_doc = 'index'
project = u'cookiecutter-drf-microservice'
copyright = u'2017-2019'
version = '0.7.1'
release = 'latest'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
htmlhelp_basename = 'cookiecutter-drf-microservice'
file_insertion_enabled = False
latex_documents = [
    ('index', 'cookiecutter-drf-microservice.tex', u'cookiecutter-drf-microservice Documentation',
     u'', 'manual'),
]
