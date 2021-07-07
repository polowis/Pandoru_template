---
layout: default
title: Configuration
parent: Getting Started
nav_order: 2
---
# Configuration

## Introduction

All of the configuration files for the Pandoru are stored in the ```app/config``` directory. The app's configuration (usually this is ```.env``` file) is placed inside ```app``` directory. 

## Enviroment configuration

It is helpful to have different configuration values based on the environment where the application is running. For example, you may wish to use a different database locally than you do on your production server.

The environment main app's configuration file (```config.py```) should never be directly commited to the source control. If you decide to store sensitive configuration, this would be a security risk as someone might gains access to your source control and then any sensitive information would get exposed.

If you're developing in a team, you may wish to include the example configuration file so other developers can see which configuration variables are needed to run the application.

## Environment variables

Please don't remove any environment variables that already exist this may cause errors as the main core of the project is heavily depended on it.

You are free to customize the database configuration, if you look at ```config.py``` file, you can see what variables are needed in order to configure the database. 

Please note that if you're using ```sqlite```, you will need to provide the full url path in ```DB_URI``` variable.