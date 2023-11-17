class CheapestOperatorUtil:

    @staticmethod
    def find_cheapest_operator(operators, telephone_number):
        cheapest_operator = None
        lowest_price = float('inf')

        for operator_name, operator in operators.items():
            price = operator.search_for_cheapest_telephone_operator(telephone_number)
            if price is not None and price < lowest_price:
                lowest_price = price
                cheapest_operator = operator_name

        if cheapest_operator:
            print(f"The cheapest operator for given number {telephone_number} is {cheapest_operator} with price {lowest_price}")
        else:
            print(f"There are no operators available for number {telephone_number}")