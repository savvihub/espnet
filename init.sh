# Setup espnet
sudo apt-get update
sudo apt-get install -y sox bc

pip install --upgrade pip
pip install -q -e .

# download pre-compiled warp-ctc and kaldi tools
pip install gdown
espnet/utils/download_from_google_drive.sh \
    "https://drive.google.com/open?id=13Y4tSygc8WtqzvAVGK_vRV9GlV7TRC0w" espnet/tools tar.gz > /dev/null
espnet/tools/installers/install_sph2pipe.sh

# make dummy activate
touch espnet/tools/activate_python.sh