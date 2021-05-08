/opt/thmctrl: src
	sudo mkdir -p /opt/thmctrl
	sudo cp -r ./src/* /opt/thmctrl
	sudo chmod -R 777 /opt/thmctrl

/usr/bin/thmctrl: /opt/thmctrl
	sudo ln -s /opt/thmctrl/main.py /usr/bin/thmctrl
	sudo chmod -R 777 /usr/bin/thmctrl

uninstall: /opt/thmctrl /usr/bin/thmctrl
	sudo rm -rf /opt/thmctrl
	sudo rm /usr/bin/thmctrl

install: /opt/thmctrl /usr/bin/thmctrl
	@echo "***Installed thmctrl on /usr/bin/thmctrl***"
