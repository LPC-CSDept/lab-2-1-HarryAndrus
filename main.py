def main():
    original_price = int(input('What is the regular price? '))
    rate = int(input('What is the percentage discount of the item? ')) / 100
    discount_amount = rate * original_price
    final_amount = original_price - discount_amount
    print('Regular Price: ','$', original_price)
    print('Discount Amount: ','$', int(discount_amount))
    print('The Final Price: ','$', int(final_amount))

if __name__ == '__main__':
    main()



 
