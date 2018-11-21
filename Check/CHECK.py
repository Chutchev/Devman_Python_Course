def calculate_max_lenght(PRODUCTS):
    max_lenght = 0
    for product in PRODUCTS:
        if len("|{} {:7d} руб.|".format(product[0], product[1])) > max_lenght:
            max_lenght = len("|{} {:7d} руб.|".format(product[0], product[1]))
    return max_lenght


def print_check(max_lenght, PRODUCTS):
    line_stroke = "_" * (max_lenght - 1)
    print(f" {line_stroke}")
    print("|{}|".format(" " * (max_lenght - 1)))
    for product in PRODUCTS:
        print("|{:16} {:7d} руб.|".format(product[0], product[1]))
    print("|{}|".format(line_stroke))


def main():
    PRODUCTS = [
        # название, цена
        ['яблоки', 100],
        ['швейцарский сыр', 1500],
        ['красная рыба', 450],
    ]
    max_lenght = calculate_max_lenght(PRODUCTS)
    print_check(max_lenght, PRODUCTS)


if __name__ == "__main__":
    main()
