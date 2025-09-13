import requests

class CreateRandomJokeTest():
    """Класс получения всех шуток по Чаку Норрису"""
    def __init__(self):
        self.categories = self.get_categories_api()
        self.url = "https://api.chucknorris.io/jokes/random"

    def get_categories_api(self):
        """Получение всех категорий API Categories. В случае добавления категорий тест будет проверять новые категории и не завязываться на старые."""
        categories_url = "https://api.chucknorris.io/jokes/categories"
        print("Получены категории из API categories GET")

        try:
            response = requests.get(categories_url)
            response.raise_for_status()

            categories = response.json()
            print(f'Получены категории: {categories}')
            return categories #Возврат всех категорий

        except requests.exceptions.RequestException as e:
            print("Ошибка при получении категорий: {e}") # Обработка ошибок на отсутствие категорий

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

        print(f"Протестировано {len(self.categories)}")
        
        if not self.categories:
            print("Нет категорий для тестирования")
            return

        for category in self.categories:
            print(f'Тестовая категория: {category}')
            self.test_single_positive_category(category, 200)

random_category_joke = CreateRandomJokeTest()
random_category_joke.test_all_categories()
