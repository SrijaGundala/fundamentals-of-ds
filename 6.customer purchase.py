item_prices = [2.99, 1.49, 4.99, 3.99]
item_quantities = [3, 2, 1, 4]

discount_rate = 10  
tax_rate = 8

subtotals = [price * quantity for price, quantity in zip(item_prices, item_quantities)]

total_cost_before_discounts_and_taxes = sum(subtotals)

discount_amount = (discount_rate / 100) * total_cost_before_discounts_and_taxes

total_cost_after_discounts = total_cost_before_discounts_and_taxes - discount_amount

tax_amount = (tax_rate / 100) * total_cost_after_discounts

final_total_cost = total_cost_after_discounts + tax_amount

print("Total cost before discounts and taxes: $", total_cost_before_discounts_and_taxes)
print("Discount amount: $", discount_amount)
print("Total cost after discounts: $", total_cost_after_discounts)
print("Tax amount: $", tax_amount)
print("Final total cost after taxes: $", final_total_cost)
