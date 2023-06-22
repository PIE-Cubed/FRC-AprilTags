anchor_1 = 530
anchor_2 = 500
h_dist   = 30

y = round(((anchor_1**2) - ((((anchor_1**2) - (anchor_2**2) + (h_dist**2)) / (2 * h_dist))**2))**0.5)
x = round(((anchor_1**2) - (anchor_2**2) + (h_dist**2)) / (2 * h_dist))

x = x - h_dist//2

print(x,y)