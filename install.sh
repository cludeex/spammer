#!/bin/bash
pkg install python
pkg install python3
pkg install python3-pip
pkg install dos2unix
pip3 install requests
pip3 install colorama
cp /data/data/com.termux/files/home/Spammer/spammer.py /data/data/com.termux/files/usr/bin/spammer
dos2unix /data/data/com.termux/files/usr/bin/spammer
chmod 777 /data/data/com.termux/files/usr/bin/spammer
spammer