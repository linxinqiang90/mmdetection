import asyncio
import os
from argparse import ArgumentParser

from mmdet.apis import (async_inference_detector, inference_detector,
                        init_detector, show_result_pyplot)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--img', help='Image file')
    parser.add_argument('--config', help='Config file')
    parser.add_argument('--checkpoint', help='Checkpoint file')
    parser.add_argument(
        '--device', default='cuda:0', help='Device used for inference')
    parser.add_argument(
        '--score-thr', type=float, default=0.3, help='bbox score threshold')
    parser.add_argument(
        '--async-test',
        action='store_true',
        help='whether to set async options for async inference.')
    args = parser.parse_args()
    return args


def main(args):
    # build the model from a config file and a checkpoint file
    model = init_detector(args.config, args.checkpoint, device=args.device)
    input = args.img
    if not os.path.exists("demo/test_result"):
        os.makedirs("demo/test_result")
    files = os.listdir(input)
    print(f"文件:{len(files)}")
    counter = 1
    for i in files:
        print(i+f"[{counter}/{len(files)}]")
        input_file = input+"/"+i
        output_file = input+"_result/"+i
        # test a single image
        result = inference_detector(model, input_file)
        # show the results
        show_result_pyplot(model, input_file, result, score_thr=args.score_thr,out_file=output_file)
        counter +=1

if __name__ == '__main__':
    args = parse_args()
    main(args)
