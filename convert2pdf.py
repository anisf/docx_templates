# -*- coding: utf-8 -*-
'''
Created : 24/03/2021
@author: Anis FATHALLAH
'''

from pathlib import Path
from docx2pdf import convert

output_dir = Path('output')
dirs_only = [x.parent for x in output_dir.glob('**/*.docx')]

for dir in set(dirs_only):
  pdf_dir = Path(dir, 'pdf')

  if not pdf_dir.exists():
    Path.mkdir(pdf_dir)

  print('Converting {}...'.format(dir))
  convert(dir, pdf_dir)
  print('...Done')