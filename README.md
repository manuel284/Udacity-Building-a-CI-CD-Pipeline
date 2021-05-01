# Overview

[![Python application test with Github Actions](https://github.com/manuel284/Udacity-Building-a-CI-CD-Pipeline/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/manuel284/Udacity-Building-a-CI-CD-Pipeline/actions/workflows/pythonapp.yml)
[![Build Status](https://dev.azure.com/DemoTospa01/Udacity-Devops/_apis/build/status/manuel284.Udacity-Building-a-CI-CD-Pipeline?branchName=main)](https://dev.azure.com/DemoTospa01/Udacity-Devops/_build/latest?definitionId=3&branchName=main)

<TODO: complete this with an overview of your project>

## Project Plan
<TODO: Project Plan

* [Trello Board](https://trello.com/b/7E52uJeg/udacity-building-a-ci-cd-pipeline)
* [Project Plan](https://docs.google.com/spreadsheets/d/1upfoYk2llhbB5BGs1W-Y3U2vmln8hDHQUxTRWsh1REw/edit?usp=sharing)

## Instructions

<TODO:  
* Architectural Diagram (Shows how key parts of the system work)>

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service

* Project cloned into Azure Cloud Shell
  - Generate ssh key:<br/>
    `ssh-keygen -t rsa`<br/>
    `cat /home/manuel/.ssh/id_rsa.pub`<br/>
    ![ssh-keys](screenshots/1-ssh-keys.png)
  - git clone git@github.com:manuel284/Udacity-Building-a-CI-CD-Pipeline.git<br/>
    ![repo in cloud shell](screenshots/2-cloud-shell-repo.png)

* Passing tests that are displayed after running the `make all` command from the `Makefile`

    ![make all 1](screenshots/3-make-all1.png)<br/>
    ![make all 2](screenshots/4-make-all2.png)
* Output of a test run

    ![github actions](screenshots/5-github-actions.png)
* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>


