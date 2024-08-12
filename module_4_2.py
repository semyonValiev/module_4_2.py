def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


# Вызываем функцию test_function
test_function()

# Попробуем вызвать inner_function вне функции test_function
# Необходимо поместить эту строку в блок try-except, чтобы программа не останавливалась из-за ошибки
try:
    inner_function()
except NameError:
    print("Функция inner_function не определена вне области видимости test_function")
