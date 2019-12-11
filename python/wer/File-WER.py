import sys
from jiwer import wer

#ground_truth = "In most toothpastes and many water supplies,we use tiny amounts of fluoride"
ground_truth_file = sys.argv[1]
#hypothesis = "In most toothpaste and many water supplies, we use tiny amounts of fluoride."
hypothesis_file = sys.argv[2]

with open(ground_truth_file, 'r', encoding="utf-8") as fg:
    ground_truth = fg.read()

with open(hypothesis_file, 'r', encoding="utf-8") as fh:
    hypothesis = fh.read()

error = wer(ground_truth, hypothesis)
#error = wer(ground_truth, hypothesis, standardize=True, words_to_filter="")

print("Word Error Rate: {:.1%}".format(error))