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
sed -i "s/47.88.85.249/${name}/g" docker-compose.yml
sed -i "s/47.88.85.249/${name}/g" .env

docker-compose up -d bee-1 bee-2 bee-3 bee-4 bee-5 bee-6
sleep 3m
docker-compose up -d bee-7 bee-8 bee-9 bee-10 bee-11 bee-12
sleep 3m
docker-compose up -d bee-13 bee-14 bee-15 bee-16 
sleep 3m
curl -sLf https://raw.githubusercontent.com/luzhongyun/SwarmBzz/main/watch.sh | bash

