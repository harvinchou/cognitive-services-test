import sys
from jiwer import wer

#ground_truth = "In most toothpastes and many water supplies,we use tiny amounts of fluoride"
ground_truth = sys.argv[1]
#hypothesis = "In most toothpaste and many water supplies, we use tiny amounts of fluoride."
hypothesis = sys.argv[2]

error = wer(ground_truth, hypothesis)
#error = wer(ground_truth, hypothesis, standardize=True, words_to_filter="")

print(error)