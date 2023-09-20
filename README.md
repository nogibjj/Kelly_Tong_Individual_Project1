# IDS 706 Individual Project 1

This repository is for IDS706 individual project 1. 



## Purpose 
    This repository uses panads to describe statistics and generate visualization for dataset Auto.csv. 
    The dataset Auto.csv includes variables such as mpg, weight, year, origin and acceleration etc.
    General statistics are described in the describe_dataset() function. This includes statistics on
    mean, count, and standard deviation etc.
    Furthermore, through the visualizatons created, one is able to analyze the correlation between weight and mpg or
    weight and acceleration with respect to origin or year. Both the scattered plots and fitted plots, 
    which include line of best fit, are included to provide closer insight.

## Important Things included are:
- ``.devcontainer`` includes a Dockerfile and devcontainer.json.
                The 'Dockerfile' within this folder specifies how the container should be built

- ``workflows`` includes install.yml, test.yml, format.yml, lint.yml, deploy.yml, and generate_and_push.yml. These are the configuration files for setting up automated build, test, and deployment pipelines

- ``.gitignore`` is used to specify which files or directories should be excluded from version control when using Git.

- ``Makefile`` is a configuration file used in Unix-based systems for automating tasks and building software. It contains instructions and dependencies for compiling code, running tests, and other development tasks.

- ``README.md`` is the instruction file for the readers.

- ``requirements.txt`` is to specify the dependencies (libraries and packages) required to run the project.
  
- ``project1`` folder includes the main files for this project. It includes a ``desc_stats.ipynb`` jupyter notebook and 4 python files:                                                      ``main.py``,``lib.py``,``test_main.py``,``test_lib.py``. It also includes the investigated dataset ``Auto.csv``.
        - ``desc_stats.ipynb`` is a jupyter notebook that includes the scratch notes for creating the functions. It also displays the plots created. 
        - ``main.py`` is a Python file. This specific main.py includes features of importing the pandas package and utilizing pandas to visualize the dataset Auto.csv.
        - ``test_main.py`` is a test file for main.py.
        - ``lib.py`` includes all the written functions for describing statistics and visualizing data in Auto.csv
        - ``test_lib.py`` is a test file for lib.py.
        - ``Auto.csv`` is the dataset used in this project. It contains variables such as mpg, acceleration, weight, origin, and year etc. 

- ``scatter_mpg.png`` ``fitted_mpg.png`` ``scatter_acc.png`` ``fitted_acc.png`` are the automatically saved plots generated by the functions. They are saved in png format.
  
- ``output.pdf`` displays the detailed output from running main.py

## Github Actions
Status badges for each makefile commands are displayed below. CI.yml includes all commands. 

`install.yml`
[![Install](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/actions/workflows/install.yml)

`test.yml`
[![Test](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/actions/workflows/test.yml)

`format.yml`
[![Format](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/actions/workflows/format.yml)

`lint.yml`
[![Lint](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/actions/workflows/lint.yml)

`deploy.yml`
[![Deploy](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/actions/workflows/deploy.yml/badge.svg)](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/actions/workflows/deploy.yml)

`generate_and_push.yml`
[![Generate_and_Push](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/actions/workflows/generate_and_push.yml/badge.svg)](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/actions/workflows/generate_and_push.yml)

## The Building Process

`make install`

The building process starts with installing the packages. 
**Make install** calls the command pip install --upgrade pip &&\pip install -r requirements.txt
<img width="1217" alt="install" src="https://github.com/nogibjj/Kelly_Tong_Individual_Project1/assets/142815940/df16531a-98ec-4459-9584-87995963d22c">

`make test`

**Make test** for jupyter notebook, calls the command py.test --nbval project1/*.ipynb
<img width="801" alt="test jupyter notebook" src="https://github.com/nogibjj/Kelly_Tong_Individual_Project1/assets/142815940/07a6728b-c465-4321-be24-b4760d9f6c89">

**Make test** for python files, calls the command python -m pytest -vv --cov=main test_*.py
<img width="637" alt="test python file" src="https://github.com/nogibjj/Kelly_Tong_Individual_Project1/assets/142815940/59dfdb11-cbc3-40ee-9a25-684f317f3fe1">

`make format`

**Make format** calls the command black *.py
<img width="453" alt="make format" src="https://github.com/nogibjj/Kelly_Tong_Individual_Project1/assets/142815940/4176a55d-853a-4d61-9213-ac0d05a88217">

`make lint`

**Make lint** calls the command pylint --disable=R,C --ignore-patterns=test_.*?py *.py
<img width="243" alt="make lint" src="https://github.com/nogibjj/Kelly_Tong_Individual_Project1/assets/142815940/385e863e-6203-45ca-8a03-8b211fda209c">

`make deploy`

no implementation of deployment is required in this repository
<img width="180" alt="make deploy" src="https://github.com/nogibjj/Kelly_Tong_Individual_Project1/assets/142815940/bdc9c2a2-a49f-4690-b9f2-920d11e0a815">

`generate_and_push`

**generate_and push** automatically saves the plots and markdown file via github actions. 
<img width="468" alt="generate_and_push" src="https://github.com/nogibjj/Kelly_Tong_Individual_Project1/assets/142815940/f969cbc2-016c-4a3b-bc07-d684ab18bcf4">


## Visualizations
#### Correlation between weight and mpg with respect to origins
![plot1](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/blob/b3d1e3cc85eea862430cc145ced16f1e8228a3cc/scatter_mpg.png)

#### Fitted correlation between weight and mpg with respect to origins
![plot2](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/blob/643860451ba0a15403f7845adc7617d11b55d10f/fitted_mpg.png)

#### Correlation between weight and acceleraton with respect to year
![plot3](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/blob/a67b037d951f518ddc11b91881e9557fb7335b59/scatter_acc.png)

#### Fitted correlation between weight and acceleraton with respect to year
![plot4](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/blob/be5babf412f4ad45f062f033c9f1178ca83e7896/fitted_acc.png)

## Conclusion
Please view results in desc_stats.md, which is automatically generated by github action generate_and_push. 
