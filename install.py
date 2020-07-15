import os
os.system("pkg install dos2unix")
os.system("pip install requests")
os.system("cp ~/spamer/spamer.py /data/data/com.termux/files/usr/bin/spamer")
os.system("dos2unix /data/data/com.termux/files/usr/bin/spamer")
os.system("chmod 777 /data/data/com.termux/files/usr/bin/spamer")
os.system("spamer")
