import requests

def currency_converter():
    print("\n===== CURRENCY CONVERTER =====")

    base_currency = input("Enter base currency (e.g., USD, INR, EUR): ").upper()
    target_currency = input("Enter target currency: ").upper()
    amount = float(input("Enter amount: "))

    # API endpoint
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"

    try:
        response = requests.get(url)
        data = response.json()

        if target_currency in data["rates"]:
            rate = data["rates"][target_currency]
            converted_amount = amount * rate
            print(f"\n💱 {amount} {base_currency} = {converted_amount:.2f} {target_currency}")
        else:
            print("❌ Currency not found.")

    except Exception as e:
        print("Error fetching data:", e)

# Main program loop
while True:
    currency_converter()
    again = input("\nDo you want to convert again? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye 👋")
        break
