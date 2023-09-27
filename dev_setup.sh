cd ..
git clone git@github.com:565353780/colmap-manage.git
git clone https://github.com/graphdeco-inria/gaussian-splatting --recursive gs

sudo apt install -y libglew-dev libassimp-dev libboost-all-dev libgtk-3-dev libopencv-dev \
	libglfw3-dev libavdevice-dev libavcodec-dev libeigen3-dev libxxf86vm-dev libembree-dev
sudo apt install imagemagick

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install tqdm plyfile

cd colmap-manage
./dev_setup.sh

cd gs/SIBR_viewers
rm -rf build
cmake -Bbuild . -DCMAKE_BUILD_TYPE=Release -G Ninja
cmake --build build -j --target install

cd ../submodules/diff-gaussian-rasterization
pip install -e .

cd ../simple-knn
pip install -e .
