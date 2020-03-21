PYTHON_REF=$(source ./bin/python.sh) # change path if necessary
if [[ "$PYTHON_REF" == "NoPython" ]]; then
    echo "Python3.6+ is not installed."
    exit 1
fi

source ./bin/node.sh
source ./bin/brew.sh
source ./bin/nvm.sh

RED='\033[0;31m'
WHITE='\033[00m'
WARNING='\033[93m'
SUCCESS='\033[92m'

if  ! isNodeInstalled ; then
    echo -e "${RED}Node is not install ${WHITE}"
    exit 1
fi

# This is your app
# PYTHON_REF is python or python3
$PYTHON_REF -c "print('Python requirement satisfied >=3.6+')";
if [  ! -f package.json ] || [ ! -f requirements.txt ]; then
    echo "Make sure to run this command from the root directory of the repo."
    
fi
# for linux installisation
if [[ "$OSTYPE" == "linux"* ]]; then
echo "Detecting OS: $OSTYPE";

# activate python virtual environment
python3 -m venv venv
source venv/bin/activate

# install packages from requirements.txt
pip install -r requirements.txt

# set the main entry point for flask app
export FLASK_APP=main.py

# install node packages
npm install

#compile js assets
npm run dev
fi

# install for OSX
if [[ "$OSTYPE" == "darwin"* ]]; then
echo "Detecting OS: $OSTYPE";

# activate python virtual environment
python3 -m venv venv
source venv/bin/activate

# install packages from requirements.txt
pip install -r requirements.txt

# set the main entry point for flask app
export FLASK_APP=main.py

# migrate the database, assuming the database is setup correctly
flask db:migrate 
    
# install npm dependencies
npm install

#compile js assets
npm run dev


# Install for window

elif [[ "$OSTYPE" == "msys"* ]]; then
echo "Detecting OS: $OSTYPE";
# activate python virtual environment
py -m venv venv
venv\Scripts\activate

# install packages from requirements.txt
pip install -r requirements.txt

# set the main entry point for flask app
set FLASK_APP=main.py

# migrate the database, assuming the database is correctly setup
flask db:migrate

# install nodejs dependencies
npm install

#compile js assets
npm run dev
fi