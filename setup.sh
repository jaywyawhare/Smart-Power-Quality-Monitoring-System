read -p "Enter the sudo password: " -s password
echo $password | sudo -S apt-get install build-essential python3-dev python3-smbus git
echo "Required packages installed"
pip install -r requirements.txt
echo "Required python packages installed"