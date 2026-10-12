def get_day_name(day: int) -> str:
    match day:
        case 1:
            return "Понедельник"
        case 2:
            return "Вторник"
        case 3:
            return "Среда"
        case 4:
            return "Четверг"
        case 5:
            return "Пятница"
        case 6:
            return "Суббота"
        case 7:
            return "Воскресенье"
        case _:
            return "none"


if __name__ == "__main__":
    tests = [1, 2, 3, 4, 5, 6, 7, 8, -1]
    for t in tests:
        print(t, "->", get_day_name(t))
