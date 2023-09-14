cd ../gs

python render.py \
	--model_path ./output/test0/ \
	--images images \
	--resolution 8 \
	--data_device cuda
