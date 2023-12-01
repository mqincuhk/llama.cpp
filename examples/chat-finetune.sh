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
    --lora-scaled lora-open-llama-7b-reason-LATEST.bin 0.7 \
    --lora-scaled lora-open-llama-7b-path-LATEST.bin 0.3 \
    --repeat_penalty 1.0 --color -i \
    -r "User:" -f prompts/chat-path.txt 











"""
./main -m ./models/7B/ggml-model-q4_0.gguf -c 512 -b 1024 -n 256 --keep 48 \
    --lora lora-open-llama-7b-reason-LATEST.bin \
    --repeat_penalty 1.0 --color -i \
    -r "User:" -f prompts/chat-reason.txt 
"""