#!/usr/bin/env bash
clear
if [ -e  /usr/lib/sudo ]
then
    if [ -e /usr/bin/apt-get ]
    then
        sudo apt-get install python3 python3-pip
        sudo cp spammer.py /usr/bin/spammer
        chmod +x /usr/bin/spammer
    fi
else
    if [ -d /usr/bin ]
    then
        if [ -e /usr/bin/apt-get ]
        then
            apt-get install python3 python3-pip
            cp spammer.py /usr/bin/spammer
            chmod +x /usr/bin/spammer
        fi
    fi
fi
if [ -d /data/data/com.termux/files/usr/bin ]
then
    pkg install python
    cp spammer.py $PREFIX/bin/spammer
    chmod +x $PREFIX/bin/spammer
fi
if [ -e  /usr/lib/sudo ]
then
    if [ -e /usr/bin/yum ]
    then
        sudo yum install python3 python3-pip
        sudo cp spammer.py /usr/bin/spammer
        chmod +x /usr/bin/spammer
    fi
else
    if [ -d /usr/bin ]
    then
        if [ -e /usr/bin/yum ]
        then
            yum install python3 python3-pip
            cp spammer.py /usr/bin/spammer
            chmod +x /usr/bin/spammer
        fi
    fi
fi
if [ -e  /usr/local/bin/brew ]
then
    brew install python3 python3-pip
    cp spammer.py /usr/local/bin/spammer
    chmod +x /usr/local/bin/spammer
fi
if [ -e  /usr/bin/apk ]
then
    apk install python3
    cp spammer.py /usr/bin/spammer
    chmod +x /usr/bin/spammer
fi
pip3 install -r requirements.txt
spammer
