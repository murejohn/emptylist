ef calculate_discount(price, discount_percent):
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        # Calculate discount amount and subtract from original price
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price

# Prompt user for input
original_price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

# Calculate final price using the function
result = calculate_discount(original_price, discount)

# Print the result with 2 decimal places
print(f"The final price is: ${result:.2f}")