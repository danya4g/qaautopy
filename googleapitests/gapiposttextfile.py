import requests

class Test_New_Location():
    """Создаем новую локацию"""

    def test_create_new_location(self):
        """Создание новой локации"""
        base_url = "https://rahulshettyacademy.com"  # Базовая url
        key = "?key=qaclick123"  # Обязательный параметр для всех запросов
        post_resource = "/maps/api/place/add/json"  # Ресурс метода Post

        post_url = base_url + post_resource + key
        print(post_url)

        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        result_post = requests.post(post_url, json=json_for_create_new_location)
        result_post.raise_for_status()
        print(result_post.text)
        assert 200 == result_post.status_code
        print("Успешно создана новая локация!")
        
        """Создаем и читаем текстовый файл, в который отправим значения метода POST"""
       
        filename = 'post_response_ids.txt'
        all_place_ids = [] #Сохраняем ID для дальнейших проверок id файлов
        
        with open (filename, 'w+', encoding='utf-8') as file:
            for i in range(5):
                result_post = requests.post(post_url, json=json_for_create_new_location)
                result_post.raise_for_status()
                
                post_data = result_post.json()
                place_id = post_data.get("place_id")
                file.write(f'{place_id}\n')
                all_place_ids.append(place_id)
             
            file.seek(0)  
            content = file.read() 
            print(content)
        """Проверяем POST и статус код"""
        check_post = result_post.json()
        check_info_post = check_post.get("status")
        print(f'Статус код ответа: {check_info_post}')
        assert check_info_post == "OK"
        print("Статус код корректен")
        # place_id = check_post.get("place_id")
        print(f'Place_id: {place_id}')
              
        """Получение GET локаций, но place_id берем из файла"""
        get_resource = "/maps/api/place/get/json"
        """Перебираем список из файла с первого индекса"""
        for i, place_id in enumerate(all_place_ids, 1): 
            get_url = base_url + get_resource + key + "&place_id=" + place_id
            print(f'{i}:{get_url}')
            result_get = requests.get(get_url)
            result_get.raise_for_status()
            print(result_get.text)
            print(f'Статус код: {result_get.status_code}')
            assert 200 == result_get.status_code
            print("Проверка создания локации прошла успешно!")
        
        print("Локации созданы и проверены успешно")

run_test = Test_New_Location()
run_test.test_create_new_location()