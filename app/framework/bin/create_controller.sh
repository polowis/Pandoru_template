#!/usr/bin/env bash
# ------------------------------------------------------------------------------
#
# Description: script to create controller file for app.
#
# Usage: flask make:controller [options] <controller name>
#

#
#
# Example:
#  flask make:controller "example_controller"
#
#
# ------------------------------------------------------------------------------
CONTROLLER_NAME=""
FILE_NAME="${CONTROLLER_NAME}.py" 

BINPATH=$(cd `dirname $0`; pwd)
POST_PATH="${BINPATH}/app/http/controllers"

# --------------------\
# Create file content

file_content(){
    
}