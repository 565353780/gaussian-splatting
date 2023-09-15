# Gaussian Splatting

## Source

```bash
https://github.com/graphdeco-inria/gaussian-splatting
```

## Install COLMAP

```bash
cd ..
git clone https://github.com/colmap/colmap
```

and edit

```bash
if(CUDA_ENABLED AND CUDA_FOUND)
```

to

```bash
set(CMAKE_CUDA_ARCHITECTURES "86")
if(CUDA_ENABLED AND CUDA_FOUND)
```

which is located near

```bash
colmap/cmake/FindDependencies.cmake:Line123
```

## Install

```bash
conda create -n gs python=3.7
conda activate gs
./setup.sh
```

## Run

```bash
./run.sh
```

## Enjoy it~
