# Gaussian Splatting

## Requirements

```bash
gcc-12 & g++-12
cuda-11.8
```

## Source

```bash
https://github.com/graphdeco-inria/gaussian-splatting
```

## Install

```bash
conda create -n gs python=3.11
conda activate gs
./setup.sh
```

## Run

```bash
python convert.py
python demo.py
```

and see log via

```bash
tensorboard --logdir ./output --host 0.0.0.0
```

## Visualization

choose and edit the script to see the corresponding results

```bash
python render_train.py
python render_result.py
```

## Enjoy it~
