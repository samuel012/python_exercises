""" Mang Toto's ForEx Challenge
Author:
Description: Aling Nena's Sari-sari store just had a new neighbor! It's Mang Toto's ForEx!
Help Mang Toto to convert `USD, JPY, SGD` to `PHP` by:
* Asking the customer for their currency.
>> Welcome to Mang Toto's ForEx! What is your currency? We accept (usd, jpy, sgd):
* If they are not exchanging the currrency, notify the customer.
>> Welcome to Mang Toto's ForEx! What is your currency? We accept (usd, jpy, sgd):
>> aud
>> Sorry! We do not exchange aud!
* If they are in their currency list, ask for the amount and inform the original and equivalent PHP amount.
>> Welcome to Mang Toto's ForEx! What is your currency? We accept (usd, jpy, sgd):
>> usd
>> Your 100.50 usd is equivalent to 5069.22 PHP
"""

PHP_EXCHANGE_RATE = {
  'usd': 50.44,
  'jpy': 0.45,
  'sgd': 36.25
}
exchange_rate_keys = ', '.join(str(e) for e in list(PHP_EXCHANGE_RATE.keys()))


def converter(currency, amount):
  return PHP_EXCHANGE_RATE[currency.lower()] * float(amount)

curr = input('Welcome to Mang Toto\'s ForEx! What is your currency? We accept ({}): '.format(exchange_rate_keys))
if curr.lower() in PHP_EXCHANGE_RATE:
  amt = input('Please enter the amount you want to exchange: ')
  converted_amount = converter(curr, amt)
  print('Your {} usd is equivalent to {} PHP'.format(amt, converted_amount))
else:
  print('Sorry! We do not exchange \'{}\'!'.format(curr))

