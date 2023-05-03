# Applying Ensemble Methods to Model-Agnostic Machine-Generated Text Detection

Group name: Fly by Night

Final project for OMSCS deep learning course


## Instructions

First, install the Python dependencies using conda:

```
conda env create -f environment.yml
```

Second, run the experiments in `permute.sh`.

This is a fork of the official implementation of the experiments in the [DetectGPT paper](https://arxiv.org/abs/2301.11305v1). The original Github repository can be found [here](https://github.com/eric-mitchell/detect-gpt). An interactive demo of DetectGPT can be found [here](https://detectgpt.ericmitchell.ai).

If you'd like to run the WritingPrompts experiments, you'll need to download the WritingPrompts data from [here](https://www.kaggle.com/datasets/ratthachat/writing-prompts). Save the data into a directory `data/writingPrompts`.

**Note: Intermediate results are saved in `tmp_results/`. If your experiment completes successfully, the results will be moved into the `results/` directory.**
