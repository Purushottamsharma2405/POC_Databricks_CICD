#! /bin/bash

#Update System Local Repositories
export RPASS="1111"
echo "RPASS" | sudo --stdin apt-get update -y
echo "RPASS" | sudo --stdin apt-get upgrade -y

# install python3 and pip 
echo "RPASS" | sudo --stdin apt install python3 -y
echo "RPASS" | sudo --stdin apt install python3-pip -y

#Installing required dependencies
pip3 install -r requirement.txt

export TOKEN="dapi8e16fd65fb3b46a4a37595587797f150"

#Running out automaiton script
python3 automationscript.py
