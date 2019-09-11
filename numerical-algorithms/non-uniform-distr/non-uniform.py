# Write an algorthm that picks between 3 colors pick, green and yellow randomly but the distribution is 0.25 pink 0.30 green and 0.45 yello
from random import random

colors = ["pink", "green", "yellow", "purple"]
probabilities = [0.4, 0.1, 0.3, 0.2]
trials = 1000000


def non_uniform_random_picker(array, probabilities):
    rand_value = random()
    for i in range(len(array)):
        rand_value -= probabilities[i]
        if rand_value <= 0:
            return array[i]


results = dict()

for i in range(trials):
    value = non_uniform_random_picker(colors, probabilities)

    if results.get(value) == None:
        results[value] = 1
    else:
        results[value] += 1


for key in results:
    percentage = round(((results[key]/trials) * 100), 2)
    print(f"{key}:{percentage}% ")
