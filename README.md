# docx_templates
A set of docx templates to be used with python

# Introduction
This project has been initiated to simplify paperasse

It uses input/companies.yml as input variables and templates/<operation>/*.docx as templates file

# Usage
Generate docs from templates/<operation>/*.docx

```bash
python gen_docs.py <operation>
# Exemple for liquidation :
python gen_docs.py liquidation
```
# Requirements
Python 3.7 + Python PIP

```bash
pip install -r requirements.txt
```
# Configuration
Set variables in input/companies.yml

# Limitations
See templates/\<operation\>/README.md for limitations
  
# Disclaimer
None of the contributors can be held responsible for any usage made from this project
