[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![anisf.docx_templates.simple_run](https://github.com/anisf/docx_templates/actions/workflows/simple_run.yml/badge.svg)](https://github.com/anisf/docx_templates/actions/workflows/simple_run.yml)
# docx_templates
A set of docx templates to be used with python

# Introduction
This project has been initiated to simplify paperasse

It uses input/companies.yml as input variables and templates/\<operation\>/*.docx as templates file

# Usage
Generate docs from templates/\<operation\>/*.docx

```bash
python gen_docs.py <operation>
# Exemple for liquidation :
python gen_docs.py liquidation
```

Convert generated docs to pdf from output/\*\*/*.docx (NEEDS MICROSOFT WORD INSTALLED)

```bash
python convert2pdf.py
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
