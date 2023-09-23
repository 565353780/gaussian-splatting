cd ../gs

rm -rf ./output/test0

python train.py \
	--source_path /home/chli/chLi/NeRF/3vjia_person_gs/ \
	--model_path ./output/test0/ \
	--images images \
	--resolution 1 \
	--data_device cuda \
	--iterations 30000 \
	--port 6006 \
	--percent_dense 0.01
