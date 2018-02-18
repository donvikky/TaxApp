# TaxApp
A generic tax application

## Installation
```
$ git clone git@github.com:abrahamy/TaxApp.git
$ cd TaxApp
$ pip install -r requirements.txt
$ yarn
$ yarn start
```
Note: The django-audit-log version on pypi (v0.7.0 at the time of writing this) is not compatible with Django 2.x, I forked the repository and patched it to make it work. Hence, the requirement is specified using git+https in the requirements.txt file.

## Contributors
Victor Okroboda (@donvikky)
Abraham Yusuf (@abrahamy)
