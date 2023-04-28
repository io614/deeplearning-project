#!/bin/bash

base_models=("gpt2" "gpt2-medium" "EleutherAI/gpt-neo-125m")
mask_model=t5-base
datasets=("xsum")
n_perturbation_list=50 
n_samples=200
batch_size=50
# n_samples must >= batch_size

for dataset in "${datasets[@]}"
do
    for base_model in "${base_models[@]}"
    do
        for scoring_model in "${base_models[@]}"
        do
            python run.py --output_name cross --base_model_name "$base_model" --scoring_model_name "$scoring_model" --mask_filling_model_name "$mask_model" --n_perturbation_list "$n_perturbation_list" --n_samples "$n_samples" --batch_size "$batch_size" --pct_words_masked 0.3 --span_length 2 --skip_baselines 
        done
    done
done