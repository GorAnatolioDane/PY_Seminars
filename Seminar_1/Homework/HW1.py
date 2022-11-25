def InputNumbers(inputText):
    is_OK = false
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            it_OK = True
        except ValueError:
            print("Это не число!")
        return number
