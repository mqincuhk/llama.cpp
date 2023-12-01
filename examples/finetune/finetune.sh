#!/bin/bash
cd `dirname $0`
cd ../..

EXE="./finetune"

if [[ ! $LLAMA_MODEL_DIR ]]; then LLAMA_MODEL_DIR="./models"; fi
if [[ ! $LLAMA_TRAINING_DIR ]]; then LLAMA_TRAINING_DIR="."; fi

# MODEL="$LLAMA_MODEL_DIR/openllama-3b-v2-q8_0.gguf" # This is the model the readme uses.
MODEL="$LLAMA_MODEL_DIR/openllama-3b-v2.gguf" # An f16 model. Note in this case with "-g", you get an f32-format .BIN file that isn't yet supported if you use it with "main --lora" with GPU inferencing.

while getopts "dg" opt; do
  case $opt in
    d)
      DEBUGGER="gdb --args"
      ;;
    g)
      EXE="./build/bin/Release/finetune"
      GPUARG="--gpu-layers 25"
      ;;
  esac
done


### Begin to finetune using LORA adapters
./finetune \
    --model-base ./models/7B/ggml-model-q4_0.gguf \
    --checkpoint-in  chk-lora-open-llama-7b-reason-LATEST.gguf \
    --checkpoint-out chk-lora-open-llama-7b-reason-ITERATION.gguf \
    --lora-out lora-open-llama-7b-reason-ITERATION.bin \
    --train-data reasoning_problems.json  \
    --save-every 15 \
    --threads 6 --adam-iter 30 --batch 4 --ctx 64 \
    --use-checkpointing
