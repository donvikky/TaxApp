# TaxApp
A generic tax application

## Prerequisites
This project uses Python and NodeJS. To develop it you must have both Python and Node interpreters installed on your computer. For instructions on installing them check [here](https://www.python.org) for Python and [here](https://nodejs.org/) for NodeJS.  
The [yarn](https://yarnpkg.com) package manager is used. If you prefer [NPM](https://www.npmjs.com/get-npm) however, be sure to replace `yarn dev` with either `npm run dev` or `npx dev` in `package.json`.

## Installation
```
$ git clone git@github.com:abrahamy/TaxApp.git
$ cd TaxApp
$ pip install -r requirements.txt
$ yarn
$ yarn start
```
Note: The django-audit-log version on pypi (v0.7.0 at the time of writing this) is not compatible with Django 2.x, I forked the repository and patched it to make it work. Hence, the requirement is specified using git+https in the requirements.txt file.

## Running The Project
To run the application run `yarn start` in the project root directory. This is equivalent to running `yarn dev && python manage.py collectstatic -c --no-input && python manage.py runserver`. If using NPM refer to the explanation in **Prerequisites** above.

## Contributors
Victor Okroboda (@donvikky)  
Abraham Yusuf (@abrahamy)
