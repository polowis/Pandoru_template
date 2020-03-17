# Pandoru_template
 
## Requirement

1. Python >= 3.6+
2. Selenium driver (browser testing, driver used: Chrome)
3. Database setup (sqlite, mysql, postgresql, etc.)
4. NodeJS >= 10

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
5. Run the `install.sh` bin script
    ```bash
    ./bin/install.sh
    ```
    In case you encounter errors such as `command not found` or `permission denied` you may need to follow these steps to make the file executable in order to solve your problem:
    ```bash
    sudo chmod +x ./bin/install.sh
    ./bin/install.sh
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

