apt-get update
apt-get upgrade

apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor --y -o /usr/share/keyrings/docker-archive-keyring.gpg


echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

echo Y | apt-get install docker-ce docker-ce-cli containerd.io

docker -v

curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

chmod +x /usr/local/bin/docker-compose

docker-compose --version


wget -q https://raw.githubusercontent.com/luzhongyun/SwarmBzz/main/docker-compose.yml

wget -q https://raw.githubusercontent.com/luzhongyun/SwarmBzz/main/.env

docker-compose up -d

docker-compose logs --tail=10
