from gaussian_splatting.Demo.train import demo as demo_train
from gaussian_splatting.Demo.controller import demo as demo_control
from gaussian_splatting.Demo.render import (
    demo_train as demo_render_train
    demo_result as demo_render_result
)

if __name__ == "__main__":
    demo_train()
    demo_control()
    # demo_render_train()
    demo_render_result()
