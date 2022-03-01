#!/usr/bin/bash
clear

if [[ "$(id -u)" -ne 0 ]];
then
   echo "Please run as root."
   exit 1
fi


os=$(cat /etc/os-release | grep "ID" | head -1 | cut -d "=" -f 2 | tr '[a-z]' '[A-Z]')

echo "Installing package on ${os}"
echo ---------------------------------------

# install apt package

apt install python3 -y
apt install python3-pip -y
apt install adb -y
apt install scrcpy -y

# install pip package

pip3 install colorama

clear
echo ------------------------------------------
echo "Successfuly installed."
echo ------------------------------------------
sleep 5
python3 Black-Android.py