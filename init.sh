# Setup espnet
sudo apt-get update
sudo apt-get install -y sox bc

cd espnet
pip install --upgrade pip
pip install -q -e .

# install kaldi
cd tools
make kaldi

# make dummy activate
cd ..
touch tools/activate_python.sh

# Move dataset
mv /input/dump /home/vessl/espnet/egs2/ljspeech/tts1/dump
mv /input/data /home/vessl/espnet/egs2/ljspeech/tts1/data
mv /input/data /home/vessl/espnet/egs2/ljspeech/tts1/downloads
