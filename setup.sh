cd ..
git clone https://github.com/565353780/camera-manage.git
git clone https://github.com/565353780/colmap-manage.git
git clone https://github.com/565353780/sibr-core.git

cd camera-manage
./setup.sh

cd ../colmap-manage
./setup.sh

cd ../sibr-core
./setup.sh

sudo apt install libceres2 imagemagick -y

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install tqdm plyfile tensorboard

cd ../gaussian-splatting/gaussian_splatting/Lib/diff-gaussian-rasterization
pip install -e .

cd ../simple-knn
pip install -e .
