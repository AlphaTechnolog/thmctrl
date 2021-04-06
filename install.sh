#!/bin/bash

if [ -d /opt/thmctrl ]; then
    echo 'Deleting old source code'
    sudo rm -rf /opt/thmctrl
fi

if [ -f /usr/bin/thmctrl ]; then
    echo 'Deleting old symlink'
    sudo rm /usr/bin/thmctrl
fi

cd $(dirname $0)
echo 'Copying the code to /opt'
sudo mkdir /opt/thmctrl
sudo cp -r ./* /opt/thmctrl
sudo chmod -R 777 /opt/thmctrl /opt/thmctrl/*
echo 'Code copied successfully'

if [[ $1 != "--no-install-requirements" ]]; then
    echo 'Installing requirements'
    python3 -m pip install -r /opt/thmctrl/requirements.txt > /dev/null 2>&1
    echo 'Installed the requirements'
fi

echo 'Creating symlink'
sudo ln -s /opt/thmctrl/src/main.py /usr/bin/thmctrl
sudo chmod -R 777 /usr/bin/thmctrl
echo 'Symlink created successfully, use thmctrl -h to start'