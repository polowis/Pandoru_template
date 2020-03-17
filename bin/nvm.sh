isNVMInstalled(){
    if which nvm > /dev/null
    then
        echo "nvm is installed, skipping..."
        return 0
    else
        echo "nvm is not installed"
        return 1
    fi
}
RED='\033[0;31m'
WHITE='\033[00m'
WARNING='\033[93m'
SUCCESS='\033[92m'

installNVM(){
     brew install nvm
    source $(brew --prefix nvm)/nvm.sh
    echo "source $(brew --prefix nvm)/nvm.sh" >> ~/.profile
    if isNVMInstalled ; then
        source ./bin/node.sh
        installNodeWithNVM
    else 
        echo -e "${RED}Failed to install nvm ${WHITE}"
    fi
}