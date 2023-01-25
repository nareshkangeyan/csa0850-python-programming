loaves = int(input("enter number of loaves of day old bread:"))
regular_price = loaves * 185
discount = regular_price * 0.6
total_price = regular_price-discount
print("regular price:{:.2f} rupees".format(regular_price))
print("discount:{:.2f} rupees".format(discount))
print("total price:{:.2f} rupees".format(total_price))
