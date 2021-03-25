# -*- coding: utf-8 -*-
'''
Created : 24/03/2021
@author: Anis FATHALLAH
'''

from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
from yaml import safe_load
from pathlib import PurePath, Path
from argparse import ArgumentParser
from sys import exit

def add_signatures(tpl, company):
  for i, sh in enumerate(company['shareholders']):
    company['shareholders'][i]['sign'] = InlineImage(tpl, sh['signature'], height=Mm(20))
  return company

def get_operations(template_base_dir):
  return [child.name for child in template_base_dir.iterdir()]

def get_args(operations):
  
  parser = ArgumentParser(description='Supported operations are : {}'.format(', '.join(operations)))
  parser.add_argument('operation', type=str, help='templates folder to use from templates dir')
  args = parser.parse_args()

  if args.operation not in operations:
    parser.print_help()
    exit(1)
  
  return args

def get_templates(templates_dir):
  return sorted(templates_dir.glob('*.docx'))

def load_yaml(path):
  with open(path, 'r') as file:
    return safe_load(file)

def main(yaml, templates, operation):
  for company in yaml["companies"]:
    output_dir = Path('output', company['company_name'], operation)

    if not output_dir.exists():
      Path.mkdir(output_dir, parents=True)

    for template in templates:
      print('{0}: {1}...'.format(company['company_name'], template.name ))

      tpl = DocxTemplate(template)

      tpl_context = add_signatures(tpl, company)
      tpl.render(tpl_context)

      tpl.save(PurePath(output_dir, template.name ))

      print('... Done !')

if __name__ == '__main__':
  possible_operations = get_operations(Path('templates'))
  args = get_args(possible_operations)
  templates = get_templates(PurePath('templates', args.operation))
  yaml = load_yaml(PurePath('input', 'companies.yml'))
  main(yaml, templates, args.operation)
