def expensive_pair(keybord_prices, usb_prices, budget_amount):
    keybord_prices.sort(reverse=True)
    usb_prices.sort(reverse=True)
    for keybord_price in keybord_prices:
        for usb_price in usb_prices:
            if budget_amount >= keybord_price+usb_price:
                most_expensive_pair_in_budget = [keybord_price, usb_price]
                return most_expensive_pair_in_budget


if __name__ == "__main__":
    keyboards_prices = [40, 50, 60,52]
    drives_prices = [5, 8, 12,9]
    budget = 60
    expensive_pair_in_budget = expensive_pair(keyboards_prices, drives_prices, budget)
    print(expensive_pair_in_budget)
