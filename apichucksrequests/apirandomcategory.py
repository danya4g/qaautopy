import requests

class CreateRandomJokeTest():
    def __init__(self):

        self.categories = [
    'animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 
    'food', 'history', 'money', 'movie', 'music', 'political', 
    'religion', 'science', 'sport', 'travel'
]

    url = "https://api.chucknorris.io/jokes/random"

    def test_single_positive_category(self, category, expected_status_code):
       #Тестирование позитивных кейсов одной категории
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

    def test_all_categories(self):
    #Тестирование позитивных кейсов всех категорий из categories 
        for category in self.categories:
            print(f'Тестовая категория: {category}')
            self.test_single_positive_category(category, 200)

    def test_single_negative_category(self, category, expected_status_code):
        #Тестирование негативных кейсов невалидной категории
        path_random_joke_category = f"?category={category}"
        url_random_joke_category = self.url + path_random_joke_category
        print(url_random_joke_category)

        result = requests.get(url_random_joke_category)

        print(f'Статус код: {result.status_code}')
        assert result.status_code == expected_status_code, f'Ошибка, ожидался {expected_status_code}, получен {result.status_code}'
        print("Статус код корректный.")

        if result.status_code == "404":
            error_data = result.json()
            print(error_data)

            error_message = error_data.get("error")
            assert error_message == "Not Found", f'Ошибка, ожидался {expected_status_code}, получен {result.status_code}'
            print("Ошибка корректна. Not Found")

            assert "categories" not in error_data or error_data.get("categories") is None
            
        else:
            joke_data = result.json()
            print(joke_data)
   
    def test_negative_scenarios(self):
    #Тестирование негативных кейсов невалидной категории
        negative_cases = [
            ('invalid_category', 404),
            ('test', 404),
            ('spor', 404),
            ('', 404)
        ]

        for category, expected_status_code in negative_cases:
            print(f'Негативный тест: {category}')
            self.test_single_negative_category(category, expected_status_code)


random_category_joke = CreateRandomJokeTest()
random_category_joke.test_all_categories()
random_category_joke.test_negative_scenarios()