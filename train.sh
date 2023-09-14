cd ../gs

python train.py \
	--source_path /home/chli/chLi/NeRF/ustc_niu_black_bg/ \
	--model_path ./output/test0/ \
	--images images \
	--resolution 1 \
	--data_device cuda \
	--iterations 30000 \
	--port 6006 \
	--percent_dense 0.01
