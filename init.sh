# Setup espnet
sudo apt-get update
sudo apt-get install -y sox bc

cd espnet
pip install --upgrade pip
pip install -q -e .

# download pre-compiled warp-ctc and kaldi tools
pip install gdown
utils/download_from_google_drive.sh \
    "https://drive.google.com/open?id=13Y4tSygc8WtqzvAVGK_vRV9GlV7TRC0w" espnet/tools tar.gz > /dev/null
tools/installers/install_sph2pipe.sh

# make dummy activate
touch tools/activate_python.sh

# Move dataset
mv /input/dump /home/vessl/espnet/egs/an4/tts1/dump
mv /input/data /home/vessl/espnet/egs/an4/tts1/data
mv /input/fbank /home/vessl/espnet/egs/an4/tts1/fbank