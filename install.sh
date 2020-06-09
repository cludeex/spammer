#!/bin/bash
pkg install python
pkg install dos2unix
pip install requests
cp ~/Spammer/spammer.py /data/data/com.termux/files/usr/bin/spammer
dos2unix /data/data/com.termux/files/usr/bin/spammer
chmod -R 777 ~/spammer
chmod 777 /data/data/com.termux/files/usr/bin/spammer
spammer
