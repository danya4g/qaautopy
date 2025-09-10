import requests

class Test_new_joke():
    def __init__(self):
        pass

    def test_create_new_random_joke(self):
        
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

random_joke = Test_new_joke()
random_joke.test_create_new_random_joke()