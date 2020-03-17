isNodeInstalled(){
    if which node > /dev/null
    then
        echo "node is installed, skipping..."
        return 0
    else
        echo "node is not installed"
        return 1
    fi
}

RED='\033[0;31m'
WHITE='\033[00m'
WARNING='\033[93m'
SUCCESS='\033[92m'

installNodeWithNVM()
{
    echo -e "${WARNING}Installing NodeJS... ${WHITE}"
    nvm install v12.16.1
    if ! isNodeInstalled; then
        echo -e "${SUCCESS} NodeJS is installed ${WHITE}"
    else
        echo -e "${RED} Failed to install NodeJS ${WHITE}"
        exit 
    fi
}