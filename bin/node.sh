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