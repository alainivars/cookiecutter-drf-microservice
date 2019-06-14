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
project = u'{{cookiecutter.github_repository_name}}'
copyright = u'2017-2019'
version = 'latest'
release = 'latest'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
htmlhelp_basename = '{{cookiecutter.github_repository_name}}'
file_insertion_enabled = False
latex_documents = [
    ('index', '{{cookiecutter.github_repository_name}}.tex', u'{{cookiecutter.github_repository_name}} Documentation',
     u'', 'manual'),
]
