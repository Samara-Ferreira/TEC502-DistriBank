'''
Descrição: Arquivo referente a importação de módulos do projeto.
'''

import os
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir)
