#!/bin/bash

sudo apt-get update

sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    sshpass


curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --y --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg


echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  
sudo apt-get update

echo Y | sudo apt-get install -y docker-ce docker-ce-cli containerd.io

docker -v



sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

docker-compose --version



cd /home
mkdir -p bee && cd bee


wget -q https://raw.githubusercontent.com/luzhongyun/SwarmBzz/main/docker-compose.yml

wget -q https://raw.githubusercontent.com/luzhongyun/SwarmBzz/main/.env

name=`curl ifconfig.me`
echo ${name}
sed -i "s/47.88.52.136/${name}/g" .env

docker-compose up -d

sshpass -p "YcYsf88*" scp test.txt root@47.241.104.135:/home/logs
