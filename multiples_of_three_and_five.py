# Solved 24th July 2019

running_sum = 0

for i in range(10):
    if i % 3 == 0 or i % 5 == 0:
        running_sum += i

print(running_sum)
