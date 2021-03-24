# -*- coding: utf-8 -*-
'''
Created : 24/03/2021
@author: Anis FATHALLAH
'''

from docxtpl import DocxTemplate
from yaml import safe_load
from pathlib import PurePath, Path
from argparse import ArgumentParser
from sys import exit

template_base_dir = Path('templates')
operations = [child.name for child in template_base_dir.iterdir()]

parser = ArgumentParser(description='Supported operations are : {}'.format(', '.join(operations)))
parser.add_argument('operation', type=str, help='templates folder to use from templates dir')
args = parser.parse_args()

if args.operation not in operations:
  parser.print_help()
  exit(1)

input_dir = PurePath('input')
templates_dir = Path(template_base_dir, args.operation)

templates = sorted(templates_dir.glob('*.docx'))

with open(PurePath(input_dir, 'companies.yml'), 'r') as file:
  parsed_yaml = safe_load(file)

  for company in parsed_yaml["companies"]:
    output_dir = Path('output', company['company_name'], args.operation)

    if not output_dir.exists():
      Path.mkdir(output_dir, parents=True)

    for template in templates:
      print('{0}: {1}...'.format(company['company_name'], template.name ))

      tpl = DocxTemplate(template)
      tpl.render(company)

      tpl.save(PurePath(output_dir, template.name ))

      print('... Done !')