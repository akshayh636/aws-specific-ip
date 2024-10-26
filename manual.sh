sudo apt update

sudo apt install -y python3-pip

sudo apt install -y build-essential libssl-dev libffi-dev python3-dev python3-venv

sudo mkdir -p ~/akshay

python3 -m venv ~/akshay

sudo chmod -R 775 ~/akshay

source ~/akshay/bin/activate
