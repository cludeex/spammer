#!/bin/bash
clear
pkg install python
pkg install python3
pkg install python3-pip
pkg install dos2unix
pip3 install requests
pip3 install colorama
cp ~/Spammer/spammer.py /data/data/com.termux/files/usr/bin/spammer
dos2unix /data/data/com.termux/files/usr/bin/spammer
chmod 777 /data/data/com.termux/files/usr/bin/spammer
spammer