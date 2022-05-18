#Extra return or alpha
b = 0.8
i = 0.05
m = 0.07
Rp = 0.09

alpha = Rp - i - b * (m - i)
print ("The manager's alpha is{:0.2f}%".format (alpha))
