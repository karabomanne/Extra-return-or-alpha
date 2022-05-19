#Extra return or alpha
b = 0.8 #Beta on investment
i = 0.05 #Risk-free interest 
m = 0.07 #Return on the market
Rp = 0.09 #Actual expected return

alpha = Rp - i - b * (m - i)
print ("The manager's alpha is{:0.2f}%".format (alpha))
