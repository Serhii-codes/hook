# Calculate income tax
#
# Calculate income tax for the given income by adhering to the rules below
# Taxable Income	Rate (in %)
# First $10,000	          0
# Next $10,000	         10
# The remaining	         20
#
# Expected Output:
#
# For example, suppose the income is 45000, and the income tax payable is
#
# 10000*0% + 10000*10%  + 25000*20% = $6000

# income = float(input('Please, enter your sum'))
# tax = 0.1
# tax_1 = 10000 * tax
# tax_2 = income - 20000
# total_tax = tax_1 + tax_2 *0.2
#
# if income <= 10000:
#     print('It is 0 taxes for you')
# elif income <= 20000:
#     print(f'The tax is {tax_1}')
# else:
#     print(f'The tax is {total_tax:.2f}') # варіант без функції

def rate_tax(income):
    amount = 10000                                     # варіант з функцією
    if income <= 10000:
        return 'It is 0 taxes for you'
    elif income <= 20000:
        our_tax_1 = (income - amount) * 0.1
        return our_tax_1
    else:
        our_tax_2 = amount * 0.1
        our_tax_3 = (income - 20000) * 0.2
        return our_tax_2 + our_tax_3

print(rate_tax(25000))




