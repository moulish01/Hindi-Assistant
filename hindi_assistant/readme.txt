Unzip the hindiassistant.zip file in home folder :
unzip hindi_assistant.zip

Install python 20.04+ and install python3.10:
sudo apt install python3.10 python3.10-venv python3.10-dev -y

cd ~/hindi_assistant

Open terminal run : 
chmod +x setup.sh
bash setup.sh

To activate the env source the file :
source hindi_env/bin/activate

To run the assistant :
python assistant.py

Sometimes the ls vosk-model will fail to install
So te check it whether it install:
ls ~/vosk-model-small-hi-0.22
You should see this files : ls ~/vosk-model-small-hi-0.22

If not install manually:
cd ~
wget https://alphacephei.com/vosk/models/vosk-model-small-hi-0.22.zip
unzip vosk-model-small-hi-0.22.zip
###########################################################################################
###########################################################################################
Easy Version (After zip package is installed)

cd ~
unzip hindi_assistant.zip
cd hindi_assistant
bash setup.sh
source hindi_env/bin/activate
python assistant.py


