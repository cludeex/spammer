#!/usr/bin/env bash
clear
if [ $OSTYPE == linux-android* ]; then
    distro=termux
elif [ $OSTYPE == darwin ]; then
    distro=darwin
fi
if [ -z $distro ]; then
    distro=$(ls /etc | awk 'match($0, "(.+?)[-_](?:release|version)", groups) {if(groups[1] != "os") {print groups[1]}}')
fi
if [ -z $distro ]; then
    if [ -f /etc/os-release ]; then
        distro=$(source /etc/os-release && echo $ID)
    fi
fi
bin="/usr/bin"
python="python3"
sudo="sudo"
if [ $distro == arch ]; then
    install="pacman -S --noconfirm"
elif [ $distro == debian ]; then
    install="apt-get -y install"
elif [ $distro == ubuntu ]; then
    install="apt -y install"
elif [ $distro == termux ]; then
    install="apt -y install"
    bin="$PREFIX/bin"
    python="python"
    sudo=""
elif [ $distro == fedora ] || [ $distro == redhat ]; then
    install="yum -y install"
elif [ $distro == SuSE ] || [ $distro == sles ]; then 
    install="zypper -n install"
elif [ $distro == darwin ]; then 
    install="brew install"
    bin="/usr/local/bin"
elif [ $distro == alpine ]; then 
    install="apk add"
    sudo=""
fi
$sudo $install $python $python-pip git
git clone https://github.com/cludeex/spammer
$python -m pip install -r spammer/requirements.txt
$sudo cp spammer/spammer.py $bin/spammer
$sudo chmod +x $bin/spammer
$sudo rm -rf spammer
spammer

