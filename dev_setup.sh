cd ..
git clone https://github.com/graphdeco-inria/gaussian-splatting --recursive gs

cd gs/submodules/diff-gaussian-rasterization
pip install -e .
cd ../simple-knn
pip install -e .

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
pip install tqdm
