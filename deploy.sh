sudo apt-get -y update

sudo apt-get -y install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor --y -o /usr/share/keyrings/docker-archive-keyring.gpg


echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

echo Y | sudo apt-get install docker-ce docker-ce-cli containerd.io

docker -v

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

docker-compose --version



cd /home
mkdir -p bee && cd bee


wget -q docker-compose.yml

wget -q https://raw.githubusercontent.com/luzhongyun/SwarmBzz/main/.env

docker-compose up -d


curl cip.cc
cd /home/bee
docker-compose logs --tail="10"

docker-compose logs -f bee-1
