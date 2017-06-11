#!/bin/sh
echo "Do you want to install the clock script for Diplay-O-Tron HAT?"
echo "You will be running all commands as sudo."
echo "Please run 'cat install.sh' if you want to inspect this script. \n"
echo "Type INSTALL to install or upgrade, type REMOVE to uninstall."
echo -n "[INSTALL or REMOVE]> "
read yesno

if [ -z $yesno ]; then exit 0
elif [ $yesno = "INSTALL" ]; then
	echo "Installing clock\n"
	echo "Installing dependency: screen (using apt-get)"
	sudo apt-get -qq install screen
	if [ $? -ne 0 ]; then echo "Error installing screen."; exit 1; fi;
	echo "Copying latest binaries to /usr/local"
	echo "Copying clock.py to /usr/local/share/clock-dothat"
	sudo mkdir -p "/usr/local/share/clock-dothat"
	if [ $? -ne 0 ]; then echo "Error creating directory /usr/local/share/clock-dothat"; exit 1; fi;
	sudo cp "clock.py" "/usr/local/share/clock-dothat"
	if [ $? -ne 0 ]; then echo "Error copying to directory /usr/local/share/clock-dothat"; exit 1; fi;
	echo "Copying start script to /usr/local/bin as clock"
	sudo cp "start_clock" "/usr/local/bin/clock"
	if [ $? -ne 0 ]; then echo "Error copying to directory /usr/local/bin"; exit 1; fi;
	echo "Setting permissions (root:root 755)"
	sudo chown -R root:root "/usr/local/bin/clock" "/usr/local/share/clock-dothat"
	if [ $? -ne 0 ]; then echo "Error setting permissions to root:root"; exit 1; fi;
	sudo chmod 755 "/usr/local/bin/clock" "/usr/local/share/clock-dothat"
	if [ $? -ne 0 ]; then echo "Error setting permissions to 755"; exit 1; fi;
	echo "All done, if you want 'clock' to run on start up, please run 'crontab -u pi -e' and copy this line into it:"
	echo "@reboot /usr/local/bin/clock"
	echo "\nAlso, run 'clock' to start the clock now!"
elif [ $yesno = "REMOVE" ]; then
	echo "Removing clock\n"
	sudo rm -r "/usr/local/bin/clock" "/usr/local/share/clock-dothat"
	if [ $? -ne 0 ]; then echo "Removal failed."; exit 1; fi;
	echo "Done! If you set up the crontab, please run 'crontab -u pi -e' and remove the following line:"
	echo "@reboot /usr/local/bin/clock"
	echo "\n"
fi;
