def get_summ(num_one, num_two):
    try:
        return int(num_one) + int(num_two)
    except ValueError:
        return "ValueError"


print(get_summ(1, '5'))