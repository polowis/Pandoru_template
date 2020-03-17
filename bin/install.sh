PYTHON_REF=$(source ./bin/python.sh) # change path if necessary
if [[ "$PYTHON_REF" == "NoPython" ]]; then
    echo "Python3.6+ is not installed."
    exit
fi

source ./bin/node.sh

RED='\033[0;31m'
WHITE='\033[00m'

if  ! isNodeInstalled ; then
    echo -e "${RED}Node is not install ${WHITE}"
    exit 
fi

# This is your app
# PYTHON_REF is python or python3
$PYTHON_REF -c "print('Python requirement satisfied >=3.6+')";

if [[ "$OSTYPE" == "darwin"* ]] || [[ "$OSTYPE" == "linux"* ]]; then
echo "Detecting OS: $OSTYPE";
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=main.py
flask db:migrate
npm install

elif [[ "$OSTYPE" == "msys"* ]]; then
echo "Detecting OS: $OSTYPE";
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
set FLASK_APP=main.py
flask db:migrate
npm install
fi