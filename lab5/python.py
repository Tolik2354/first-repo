def calculate_overdue_days(return_day, deadline):
    """
    >>> calculate_overdue_days(10, 7)
    3
    >>> calculate_overdue_days(5, 7)
    0
    """
    if return_day > deadline:
        return return_day - deadline
    else:
        return 0

def calculate_fine(overdue_days, fine_per_day):
    """
    >>> calculate_fine(3, 2.0)
    6.0
    >>> calculate_fine(0, 5.0)
    0.0
    """
    return overdue_days * fine_per_day

def main():
    deadline = int(input("Введіть дедлайн повернення книги: "))
    return_day = int(input("Введіть день повернення книги: "))
    fine_per_day = float(input("Введіть штраф за один прострочений день : "))

    overdue_days = calculate_overdue_days(return_day, deadline)
    fine = calculate_fine(overdue_days, fine_per_day)

    print("Прострочені дні:", overdue_days)
    print("Сума штрафу:", fine)

if __name__ == "__main__":
 main()