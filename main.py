from impl.cheapest_operator_util import CheapestOperatorUtil
from impl.telephone_operator import TelephoneOperator


OPERATOR_A = "Operator A"
OPERATOR_B = "Operator B"
OPERATOR_C = "Operator C"
OPERATOR_D = "Operator D"

operators = {
    OPERATOR_A: TelephoneOperator(),
    OPERATOR_B: TelephoneOperator(),
    OPERATOR_C: TelephoneOperator(),
    OPERATOR_D: TelephoneOperator()
}

operators[OPERATOR_A].add_telephone_operator_offer('1', 0.9)
operators[OPERATOR_A].add_telephone_operator_offer('268', 5.1)
operators[OPERATOR_A].add_telephone_operator_offer('46', 0.17)
operators[OPERATOR_A].add_telephone_operator_offer('4620', 0.0)
operators[OPERATOR_A].add_telephone_operator_offer('468', 0.15)
operators[OPERATOR_A].add_telephone_operator_offer('4631', 0.15)
operators[OPERATOR_A].add_telephone_operator_offer('4673', 0.9)
operators[OPERATOR_A].add_telephone_operator_offer('46732', 1.1)

operators[OPERATOR_B].add_telephone_operator_offer('1', 0.92)
operators[OPERATOR_B].add_telephone_operator_offer('44', 0.5)
operators[OPERATOR_B].add_telephone_operator_offer('46', 0.2)
operators[OPERATOR_B].add_telephone_operator_offer('467', 1.0)
operators[OPERATOR_B].add_telephone_operator_offer('48', 1.2)

operators[OPERATOR_C].add_telephone_operator_offer('3', 0.92)
operators[OPERATOR_C].add_telephone_operator_offer('38', 0.5)
operators[OPERATOR_C].add_telephone_operator_offer('387', 0.2)
operators[OPERATOR_C].add_telephone_operator_offer('3876', 1.0)
operators[OPERATOR_C].add_telephone_operator_offer('38761', 1.1)

operators[OPERATOR_D].add_telephone_operator_offer('3', 1.0)
operators[OPERATOR_D].add_telephone_operator_offer('38', 1.1)
operators[OPERATOR_D].add_telephone_operator_offer('387', 1.2)
operators[OPERATOR_D].add_telephone_operator_offer('3876', 1.3)
operators[OPERATOR_D].add_telephone_operator_offer('38761', 1.2)

telephone_number_one = "4673212345"
CheapestOperatorUtil.find_cheapest_operator(operators, telephone_number_one)

telephone_number_two = "38761225883"
CheapestOperatorUtil.find_cheapest_operator(operators, telephone_number_two)

telephone_number_three = "000000000"
CheapestOperatorUtil.find_cheapest_operator(operators, telephone_number_three)