# IDS 706 Individual Project 1

This repository is for IDS706 individual project 1. 



## Purpose 
    This repository uses panads to describe statistics and generate visualization for dataset Auto.csv. 
    It is set up based on the template's environment. This repository incorporates "pandas" to develop 
    statistical functions. Specifically, the author uses pd.dataframe() to set up a dataset. Then it 
    is tested on the count, mean, max, and min. 
    Moreover, the author loads the dataset gss.csv which includes variables displaying information on 
    age, income, and marital status etc. Summary of the dataset and a histogram is developed to 
    visualize the density of the "age" variable in the dataset.

## Important Things included are:
- ``.devcontainer`` includes a Dockerfile and devcontainer.json.
                The 'Dockerfile' within this folder specifies how the container should be built

- ``workflows`` includes CI.yml, which contain configuration files for setting up automated build, test, and deployment pipelines

- ``.gitignore`` is used to specify which files or directories should be excluded from version control when using Git.

- ``Makefile`` is a configuration file used in Unix-based systems for automating tasks and building software. It contains instructions and dependencies for compiling code, running tests, and other development tasks.

- ``README.md`` is the instruction file for the readers.

- ``main.py`` is a Python file. This specific main.py includes features of importing the pandas package and utilizing pandas to visualize data. 

- ``requirements.txt`` is to specify the dependencies (libraries and packages) required to run the project.

- ``test_main.py`` is a test file for main.py

- ``make format.png`` ``make lint.png`` ``Make Test.png``saves the running results for the building process. These are displayed in the section below
  
- ``gss.csv`` is the dataset used in this project. It contains variables such as age, marital status, income, region, and happiness level etc.
  
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

`CI.yml`
[![CI](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/actions/workflows/CI.yml/badge.svg)](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/actions/workflows/CI.yml)

## The Building Process

`make install`

The building process starts with installing the packages. 
**Make install** calls the command pip install --upgrade pip &&\pip install -r requirements.txt

`make link`

**Make lint** calls the command pylint --disable=R,C --ignore-patterns=test_.*?py *.py
<img width="457" alt="make lint" src="https://github.com/Kelly0604/miniproject2/assets/142815940/39a19764-a6cc-4eaa-977f-7433b8915dad">

`make test`

**Make test** calls the command python -m pytest -vv --cov=main test_*.py
<img width="609" alt="Make Test" src="https://github.com/nogibjj/KellyTong_miniproject2/assets/142815940/1d5eb1de-c0f7-4459-97bb-cae51ea621aa">


`make format`

**Make format** calls the command black *.py


<img width="299" alt="make format" src="https://github.com/Kelly0604/miniproject2/assets/142815940/41df08ca-d8f7-4b62-b88b-1f39f1a7d858">

## Visualization
### A Density Graph on Age
<img width="614" alt="截屏2023-09-13 16 21 26" src="https://github.com/nogibjj/KellyTong_miniproject2/assets/142815940/bf314b8b-19ec-461a-9faa-f532fb254102">

## Conclusion
The dataset includes mostly age group from 25 to 35. The mean age is approximately 46. 
(Please find more detailed steps in the output.pdf)
