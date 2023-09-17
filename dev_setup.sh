cd ..
git clone https://github.com/graphdeco-inria/gaussian-splatting --recursive gs
git clone https://github.com/colmap/colmap

sudo apt install -y libglew-dev libassimp-dev libboost-all-dev libgtk-3-dev libopencv-dev \
	libglfw3-dev libavdevice-dev libavcodec-dev libeigen3-dev libxxf86vm-dev libembree-dev

sudo apt install imagemagick

sudo apt-get install git cmake ninja-build build-essential libboost-program-options-dev \
	libboost-filesystem-dev libboost-graph-dev libboost-system-dev libeigen3-dev libflann-dev \
	libfreeimage-dev libmetis-dev libgoogle-glog-dev libgtest-dev libsqlite3-dev libglew-dev \
	qtbase5-dev libqt5opengl5-dev libcgal-dev libceres-dev

if [! -d "/usr/local/bin/colmap"]; then
	cd colmap
	rm -rf build
	mkdir build
	cd build
	cmake .. -G Ninja
	ninja
	sudo ninja install
	cd ../..
fi

cd gs/SIBR_viewers
rm -rf build
cmake -Bbuild . -DCMAKE_BUILD_TYPE=Release -G Ninja
cmake --build build -j --target install

cd ../submodules/diff-gaussian-rasterization
pip install -e .

cd ../simple-knn
pip install -e .

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
pip install tqdm
