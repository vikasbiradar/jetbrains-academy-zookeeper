deposit = int(input())
interest = 7.1 / 100
year = 0
while deposit < 700000:
    year += 1
    deposit = deposit + (deposit * interest)
print(year)
