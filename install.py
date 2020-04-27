import os
os.system('pip3 install requests')
os.system('pip3 install colorama')
os.system('cp /data/data/com.termux/files/home/Spammer/spammer.py /data/data/com.termux/files/usr/bin/spammer')
os.system('dos2unix /data/data/com.termux/files/usr/bin/spammer')
os.system('chmod 777 /data/data/com.termux/files/usr/bin/spammer')
os.system('spammer')