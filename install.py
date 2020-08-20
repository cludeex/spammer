import os

os.system("pkg install dos2unix")
os.system("pip install requests")
os.system("cp ~/spammer/spammer.py /data/data/com.termux/files/usr/bin/spammer")
os.system("dos2unix /data/data/com.termux/files/usr/bin/spammer")
os.system("chmod 777 /data/data/com.termux/files/usr/bin/spammer")
os.system("spammer")
