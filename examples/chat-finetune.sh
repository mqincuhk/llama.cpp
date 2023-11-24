#!/bin/bash

#
# Temporary script - will be removed in the future
#

cd `dirname $0`
cd ..

# Important: # with the finetuned LORA adapter
#
#   "--keep 48" is based on the contents of prompts/chat-with-bob.txt
#

./main -m ./models/7B/ggml-model-q4_0.gguf -c 512 -b 1024 -n 256 --keep 48 \
    --lora lora-open-llama-7b-v2-q4_0-LATEST.bin \
    --repeat_penalty 1.0 --color -i \
    -r "User:" -f prompts/chat-finetune.txt 
