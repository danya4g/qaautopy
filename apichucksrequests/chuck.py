import requests

class Test_new_joke():
    def __init__(self):
        pass

    def test_create_new_random_joke(self):
        #Тестирование API random.get
        url = "https://api.chucknorris.io/jokes/random"
        print(url)
        result = requests.get(url)
        print(f'Статус код :{result.status_code}')
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Успех. Мы получили новую шутку")
        else:
            print("Провал")
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_info = check.get("categories")
        print(check_info)
        assert check_info == []
        print("Категория верна")
        check_info_value = check.get("value")
        print(check_info_value)
        name = "Chuck"
        if name in check_info_value:
            print("Имя Чак присутствует в ответе")
        else:
            print("Имя отсутствует")

    def test_create_new_random_categories_joke(self):
        #Тестирование API random by categories get
        url = "https://api.chucknorris.io/jokes/random?category=sport"
        print(url)
        result = requests.get(url)
        print(f'Статус код :{result.status_code}')
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Успех. Мы получили шутку из категории")
        else:
            print("Провал")
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_info = check.get("categories")
        print(check_info)
        assert check_info == ["sport"]
        print("Категория верна")
        check_info_value = check.get("value")
        print(check_info_value)
        name = "Chuck"
        if name in check_info_value:
            print("Имя Чак присутствует в ответе")
        else:
            print("Имя отсутствует")

    def test_create_new_random_categories_joke_404(self):
        #Негативное тестирование API random by categories get- проверка статус кода
        category = "sport"
        url = "https://api.chucknorris.io/jokes/random?category=spor"
        print(url)
        result = requests.get(url)
        print(f'Статус код :{result.status_code}')
        assert 404 == result.status_code
        if result.status_code == 404:
            print("Успех. 404 на несуществующей категории")
        else:
            print("Провал")

class CreateRandomJokeTest():
    url = "https://api.chucknorris.io/jokes/random"
    def test_some_positive_scenaries(self, category, expected_status_code):
        path_random_joke_category = f"?category={category}"
        url_random_joke_category = self.url + path_random_joke_category
        print(url_random_joke_category)

        result = requests.get(url_random_joke_category)
        print(result.json())

        print(f'Статус код: {result.status_code}')
        assert result.status_code == expected_status_code, 'Ошибка, статус код не совпадает.'
        print("Статус код корректный.")

        check_joke = result.json()
        joke_value = check_joke.get("value")
        print(joke_value)

        joke_category = check_joke.get("categories")
        print(joke_category)
        assert joke_category[0] == category, 'Ошибка, статус код не совпадает.'
        print("Категория корректна.")

        print("Успешный тест.")

    def test_negative_scenaries(self, category, expected_status_code):
        path_random_joke_category = f"?category={category}"
        url_random_joke_category = self.url + path_random_joke_category
        print(url_random_joke_category)

        result = requests.get(url_random_joke_category)
        print(result.json())

        print(f'Статус-код: {result.status_code}')
        assert result.status_code == expected_status_code, 'ОШИБКА, Статус-код не совпадают'
        print('Статус-код корректен')

        check_joke = result.json()
        print(check_joke)

        error = check_joke.get("error")
        print(error)
        assert error == 'Not Found', 'Ошибка, поле Error некорректно'
        print('Поле error корректно')


random_joke = Test_new_joke()
random_joke.test_create_new_random_joke()
categories_joke = Test_new_joke()
categories_joke.test_create_new_random_categories_joke()
failure_joke = Test_new_joke()
failure_joke.test_create_new_random_categories_joke_404()
start_test = CreateRandomJokeTest()
start_test.test_some_positive_scenaries('animal', 200)
start_test.test_negative_scenaries('an', 404)
start_test.test_negative_scenaries('pe', 404)
start_test.test_negative_scenaries('', 404)