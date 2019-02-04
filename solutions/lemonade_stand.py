# Write a script that asks your how many lemonades you sold over how many hours.
# It should print how much profit you made, as well as your average hourly income.

# Assume that:
# - It takes 4 lemons to make a lemonade
# - Each lemon costs 50 cents
# - Cost of the lemonades is your only expense
# - When prompted, the user will input valid integer values

num_lemonades = int(input("How many lemonades did you sell? "))
num_hours = int(input("Over how many hours? "))

lemons_per_lemonade = 4
price = 5
lemon_cost = 0.5

revenues = num_lemonades * price
expenses = lemon_cost * num_lemonades * lemons_per_lemonade

profit = revenues - expenses

print("You made ${}, or ${} per hour.".format(profit, profit / num_hours))
