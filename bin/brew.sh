isBrewInstalled(){
    if which brew > /dev/null
    then
        echo "brew is installed, skipping..."
        return 0
    else
        echo "brew is not installed"
        return 1
    fi
}
RED='\033[0;31m'
WHITE='\033[00m'
WARNING='\033[93m'
SUCCESS='\033[92m'

installBrew() {
    echo -e "${RED}Brew is not installed ${WHITE}"
    echo -e "${WARNING} Installing brew... ${WHITE}"

    # Install homebrew
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
    if ! isBrewInstalled; then
        echo -e "${RED}Failed to install Brew ${WHITE}"
        exit 
    fi
    brew update
    
}