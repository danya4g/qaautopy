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

        check_post = result_post.json()
        check_info_post = check_post.get("status")
        print(f'Статус код ответа: {check_info_post}')
        assert check_info_post == "OK"
        print("Статус код корректен")
        place_id = check_post.get("place_id")
        print(f'Place_id: {place_id}')
        get_resource = "/maps/api/place/get/json"

#         Base URL: https://rahulshettyacademy.com
# Resource: /maps/api/place/get/json
# Параметр для запросов: key=qaclick123, place_id
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print(f'Статус код: {result_get.status_code}')
        assert 200 == result_get.status_code
        print("Проверка создания локации прошла успешно!")

        """Тестирование PUT"""
        # https://rahulshettyacademy.com/maps/api/place/update/json?key=qaclick123
        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        print(put_url)
        new_address = "Zhukovsokogo 19"
        json_for_update_new_location = {
            "place_id": place_id,
            "address": new_address,
            "key": "qaclick123"
        }
        result_put = requests.put(put_url, json=json_for_update_new_location)
        print(result_put.text)
        assert 200 == result_put.status_code
        print("Проверка изменения локации прошла успешно!")
        check_put = result_put.json()
        check_put_info = check_put.get("msg")
        print(f'Сообщение: {check_put_info}')
        assert check_put_info == "Address successfully updated"
        print("Сообщение верно")

        """Тестирование того, что локация изменилась"""
        result_get = requests.get(get_url)
        print(result_get.json())

        check_response_get = result_get.json()
        print(f'Статус код: {result_get.status_code}')
        assert result_get.status_code == 200, 'Ошибка, статус код не совпадает'
        print("Статус код GET корректен")

        actual_address = check_response_get.get('address')
        print(actual_address)
        assert actual_address == new_address, 'Ошибка, адрес не изменился'
        print("Адрес изменен")

        """Удаление локации"""
        delete_resourсe = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resourсe + key
        print(delete_url)
        json_for_delete_new_location = {
            "place_id": place_id
        }
        result_delete = requests.delete(delete_url, json=json_for_delete_new_location)
        print(result_delete.text)
        print("Статус код: " + str(result_delete.status_code))
        assert 200 == result_delete.status_code
        check_status = result_delete.json()
        check_status_info = check_status.get("status")
        print("Сообщение: " + check_status_info)
        assert check_status_info == "OK"
        print("Сообщение верно")
        
        """Проверка удаления новой локации"""
        result_get = requests.get(get_url)
        print(result_get.json())

        check_response_get = result_get.json()
        print(f'Статус код: {result_get.status_code}')
        assert result_get.status_code == 404, 'Ошибка, статус код не совпадает'
        print("Статус код GET корректен")

        check_msg = result_get.json()
        check_msg_info = check_msg.get("msg")
        print("Сообщение: " + check_msg_info)
        assert check_msg_info == "Get operation failed, looks like place_id  doesn't exists"
        print("Сообщение верно")
        print("Тестирование Test_New_Location завершено успешно")
        
new_place = Test_New_Location()
new_place.test_create_new_location()
