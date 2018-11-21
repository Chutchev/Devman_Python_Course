def calculate_max_lenght(PRODUCTS):
    max_lenght = 0
    for product in PRODUCTS:
        if len("|{} {:7d} руб.|".format(product[0], product[1])) > max_lenght:
            max_lenght = len("|{} {:7d} руб.|".format(product[0], product[1]))
    return max_lenght


def print_check(max_lenght, PRODUCTS):
    line_stroke = "_" * (max_lenght - 1)
    strokes_on_check = []
    strokes_on_check.append(f" {line_stroke}\r")
    strokes_on_check.append("|{}|\r".format(" " * (max_lenght - 1)))
    for product in PRODUCTS:
        strokes_on_check.append("|{:16} {:7d} руб.|\r".format(product[0], product[1]))
    strokes_on_check.append("|{}|\r".format(line_stroke))
    return strokes_on_check


def send_to_printer(strokes_on_check):
    for stroke in strokes_on_check:
        print(stroke)

def main():
    PRODUCTS = [
        # название, цена
        ['яблоки', 100],
        ['швейцарский сыр', 1500],
        ['красная рыба', 450],
    ]
    max_lenght = calculate_max_lenght(PRODUCTS)
    strokes_on_check = print_check(max_lenght, PRODUCTS)
    send_to_printer(strokes_on_check)

if __name__ == "__main__":
    main()
