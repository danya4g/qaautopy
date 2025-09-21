import requests
"""Класс получения всех шуток по Чаку c проверкой статус кода"""
class UserInputCategories():
    def __init__(self):
        self.categories = self.get_categories_api(200)
        self.url = "https://api.chucknorris.io/jokes/random"

    def get_categories_api(self, expected_status_code):
        """Получение всех категорий API Categories. В случае добавления категорий тест будет проверять новые категории и не завязываться на старые."""
        categories_url = "https://api.chucknorris.io/jokes/categories"
        print("Получены категории из API categories GET")
        #Запрос для проверки статус кода
        try:
            result = requests.get(categories_url)
            print(f'Статус код: {result.status_code}')
            assert result.status_code == expected_status_code, f'Ожидался {expected_status_code}, получен: {result.status_code}'
            print("Статус код корректный.")
        #Запрос для проверки категорий
            response = requests.get(categories_url)
            response.raise_for_status()

            categories = response.json()
            print(f'Получены категории: {categories}')
            return categories # Возврат всех категорий

        except requests.exceptions.RequestException as e:
            print("Ошибка при получении категроий: {e}")
            return[]
        except AssertionError:
            print("Ошибка. Ожидался статус код {expected_status_code}, получен {result.status_code}")
            return []
   
# Тестирование категорий, введенных пользователем.
    def user_input_category(self):
        user_category = str(input().strip())
        print(f"Пользователь ввел категорию: {user_category}")

        if user_category in self.categories:
            print(f"Категория {user_category} найдена в списке.")
            return user_category
        
        else:  
            print(f"Категория {user_category} не найдена в списке.")
            print(f"Доступные категории: {self.categories}")
            return None

    def test_user_category(self, user_category, expected_status_code=200):
        """Тестирование категории шутки"""

        if not user_category:
            print("Категория {user_category} отсутствует в списке категорий. ")
            return
        
        print(f'Шутка из категории пользователя: {user_category}')
        url = f'{self.url}?category={user_category}'
        print(f'URL запроса: {url}')

        try:
            response = requests.get(url)
            response.raise_for_status()
            assert response.status_code == expected_status_code, f'Ожидался: {expected_status_code}, получен: {response.status_code}'
            print("Статус код корректный.")

            joke_data = response.json()
            print(f'Шутка: {joke_data['value']}')
        except requests.exceptions.RequestException as e:
            print(f'Ошибка при получении шутки: {e}')
        except AssertionError as e:
            print(f'Ошибка {e}')
# Тестирование категории, введенной пользователем.        
    def test_user(self):
        print("Введите категорию для шутки. Доступные категории:", self.categories)
        while True:
            selected_category = self.user_input_category()
            if selected_category:
                self.test_user_category(selected_category, 200)
                break
            else:
                print('Попробуйте еще раз.')

user_input_joke = UserInputCategories()
user_input_joke.test_user()