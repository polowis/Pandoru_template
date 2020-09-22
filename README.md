<img src="docs/beymax.png">

This repo also contains the example todolist app.

This template contains many built in feature such as moment (to deal with datetime, localization, built in functions that allow you to retrieve user's IP details and many more.). You can also build your frontend code using single command (currently only supported for vue). Highly customizable.

Note: The root of this project is placed at https://github.com/Strefio/Beymax (currently not open sourced)

## Requirement

1. Python >= 3.6+
2. Database setup (sqlite, mysql, postgresql, etc.)
3. NodeJS >= 11
4. Redis 

## Optional Dependencies
1. ```webdriver``` - required if you want to run ```flask test``` command

## Installation

In order to work on this project on your machine, you can follow the instructions below

1. Fork this repository 
2. Open your terminal and `cd` to your `~/your_folder` folder
3. Clone your fork into the `~/your_folder` folder, by running the following command *replace your username into {your_username} slot*:
    ```bash
    git clone git@github.com:{your_username}/Pandoru_template
    ```
4. CD into the new directory you just created:
    ```bash
    cd Pandoru_template
    ```

5. Run the `install.sh` bin script <br>
    **If your machine has satisfied with all the requirements listed above, skip this step**
    ```bash
    ./bin/install.sh
    ```
    In case you encounter errors such as `command not found` or `permission denied` you may need to follow these steps to make the file executable in order to solve your problem:
    ```bash
    sudo chmod +x ./bin/install.sh
    ./bin/install.sh
    ```

6. Run ```setup.sh``` bin script <br>
    **If you already run the ```install.sh``` script, skip this step**
    ```bash
    ./bin/setup.sh
    ```
    In case you encounter errors such as `command not found` or `permission denied` you may need to follow these steps to make the file executable in order to solve your problem:
    ```bash
    sudo chmod +x ./bin/setup.sh
    ```

## Configuration

You may change the configuration of the project in ./app/config.py. 

## Testing

To run all the tests, you might use the following command:
```
$ flask test
```

## Refresh database
This command will drop all tables and rerun the database

```
$ flask db:fresh
```
## Test database connection
```
$ flask db:connection
```
## Available commands

```
$ flask db:migrate 
$ flask db:fresh
$ flask db:connection
$ flask node
$ flask test
$ flask serve
$ flask key:generate
$ flask config:mail
$ flask config:localization
```
