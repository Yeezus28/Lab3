import price_info

def test_total_cost_shopping():
    expected_total = (
        price_info.price_list['watermelon'] * price_info.quantity_list['watermelon'] + 
        price_info.price_list['apple'] * price_info.quantity_list['apple'] +
        price_info.price_list['orange'] * price_info.quantity_list['orange'] +
        price_info.price_list['pineapple'] * price_info.quantity_list['pineapple'] +
        price_info.price_list['pear'] * price_info.quantity_list['pear'] +
        price_info.price_list['papaya'] * price_info.quantity_list['papaya'] +
        price_info.price_list['pomegranate'] * price_info.quantity_list['pomegranate']
    )
    result = price_info.total_cost_shopping()
    assert result == expected_total

def test_cost_of_fruit():
    fruit = "watermelon"
    quantity = 3
    expected_cost = price_info.price_list[fruit] * quantity
    result = price_info.cost_of_fruits(fruit, quantity)
    assert result == expected_cost