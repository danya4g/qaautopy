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

        result_post = requests.post(
            post_url, json=json_for_create_new_location)
        print(result_post.text)
        assert 200 == result_post.status_code
        print("Успешно создана новая локация!")

        """Создаем и читаем текстовый файл, в который отправим значения метода POST"""

        filename = 'post_response_ids.txt'
        with open(filename, 'w+', encoding='utf-8') as file:
            for i in range(5):
                result_post = requests.post(
                    post_url, json=json_for_create_new_location)
                result_post.raise_for_status()

                post_data = result_post.json()
                place_id = post_data.get("place_id")
                file.write(f'{place_id}\n')

            file.seek(0)
            content = file.read()
            print(content)

        """Проверяем POST и статус код"""
        check_post = result_post.json()
        check_info_post = check_post.get("status")
        print(f'Статус код ответа: {check_info_post}')
        assert check_info_post == "OK"
        print("Статус код корректен")

        """Удаляем 2й и 4й place_id из файла"""
        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key
        with open(filename, 'r', encoding='utf-8') as file:
            # [выражение for элемент in коллекция if условие]
            place_ids_in_file = [line.strip() for line in file if line.strip()]
            # Удаляем place_id из файла с индексом 1, 3
            lines_to_delete = [1, 3]
            for index in lines_to_delete:
                if index < len(place_ids_in_file):
                    place_id = place_ids_in_file[index]
                    json_for_delete_place_id = {
                        "place_id": place_id
                    }
                    result_delete = requests.delete(
                        delete_url, json=json_for_delete_place_id)
                    print(
                        f'Удаление локации {index + 1}: Id: {place_id}{result_delete.status_code}')
                    assert 200 == result_delete.status_code
                    check_status = result_delete.json()
                    check_status_info = check_status.get("status")
                    print(f'Локация {index + 1}:{place_id} удалена из API')
                    assert check_status_info == "OK"
                    print("Сообщение верно")

        """Получение GET локаций, но place_id берем из файла"""
        get_resource = "/maps/api/place/get/json"
        """Перебираем список из файла с первого индекса"""
        with open(filename, 'r+', encoding='utf-8') as file:
             for i, line in enumerate(file, 1):
                 place_id = line.strip()
                 if place_id:
                    get_url = base_url + get_resource + key + "&place_id=" + place_id
                    result_get = requests.get(get_url)
                    assert result_get.status_code in [
                        200, 404], f'Неожиданный статус код {result_get.status_code}'
                    if result_get.status_code == 200:
                        print(f'Локация {i}:{place_id} успешно создана')
                    else:
                        result_get.status_code == 404
                        print(f'Локация {i}:{place_id} удалена')
        """Создаем файл 2, записываем в него существующие локации"""
        file_with_existing_place_ids = 'filewithwexistlocations.txt'
        with open(filename, 'r', encoding='utf-8') as file_with_locations,\
            open(file_with_existing_place_ids, 'w+', encoding='utf-8') as file_to_write_eloc:

            for i, line in enumerate(file_with_locations):
                place_id = line.strip()
                if place_id:
                    get_url = base_url + get_resource + key + "&place_id=" + place_id
                    result_get = requests.get(get_url)
                    assert result_get.status_code in [200, 404], f'Неожиданный статус код {result_get.status_code}'
                    if result_get.status_code == 200:
                        file_to_write_eloc.write(f'{place_id}\n')
                        print((f'Существующая локация {i}:{place_id} записана в файл '))
                    else:
                        result_get.status_code == 404
                        print(f'Локация {i}:{place_id} не записана в файл')
                    
        print("Локации созданы и проверены успешно") 
        
run_test = Test_New_Location()
run_test.test_create_new_location()