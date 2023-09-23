cd ../gs

NERF_PATH=/home/chli/chLi/Dataset/NeRF/3vjia_simple

rm -rf $NERF_PATH/distorted
rm -rf $NERF_PATH/images
rm -rf $NERF_PATH/sparse
rm -rf $NERF_PATH/stereo
rm $NERF_PATH/run-colmap-*

python convert.py \
	--source_path $NERF_PATH/ \
	--camera PINHOLE
