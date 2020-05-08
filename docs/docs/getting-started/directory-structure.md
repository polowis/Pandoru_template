---
layout: default
title: Directory Structure
parent: Getting Started
nav_order: 2
---

# Directory Structure

The ```app``` directory is the main directory of the application.

In the ```app``` directory, there are

1. ```command``` directory
2. ```configuration``` directory
3. ```framework``` directory
4. ```http``` directory
5. ```kernel``` directory
6. ```model``` directory
7. ```resources``` directory
8. ```static``` directory
9. ```templates``` directory

In the ```framework``` directory, there are
1. ```auth``` directory
2. ```bin``` directory
3. ```config``` directory
4. ```console``` directory
5. ```controller``` directory
6. ```database``` directory
7. ```encryption``` directory
8. ```requests``` directory
9. ```routes``` directory
10. ```tests``` directory
11. ```utility``` directory

## Overview
The default application structure is intended to provide a great starting point. But you are free to organize your application however you like. As long as you keep the base directory the same so the main core of the project which is ```framework``` directory is able to load the files.

### The app directory

The ```app``` directory contains the core code of the application. Almost everything in your application should be done inside this directory

### The command directory

This directory provides custom commands for the application. They are registered automatically.

### The configuration directory

The configuration directory contains all of your application's configuration files. You should go through these files so you can familiarize with all the options available in your application. 

### The framework directory

This directory contains the core code of the application. You should never have to access this directory. The directory provides all the core functionality to help the application run as it is expected.

### The http directory

All your requests are handled in this directory. 
