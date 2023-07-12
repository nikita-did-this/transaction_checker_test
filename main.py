from base64 import b64decode
import json
import requests

block_number = str(input("Введите номер блока: "))
print()  # Вывод с разделением мне кажется более читабельным


def transactions(block_num="11260637"):

    """Возвращает данные о транзакциях из указанного пользователем блока"""

    api_resp = requests.get(f"https://akash-mainnet-rpc.cosmonautstakes.com/block?height={block_num}")  # Обращаемся к API за информацией о блоке по его номеру
    try:  # Проверяем что блок в принципе существует
        api_resp_json = json.loads(api_resp.content)
        transactions_list = api_resp_json['result']['block']['data']['txs']  # Получаем список транзакций
        if transactions_list:  # Проверяем, были ли транзакции
            for transaction in transactions_list:
                data = b64decode(transaction, altchars=None, validate=True)  # Декодируем данные о транзакции
                print(data, "\n")  # Выводим декодированные данные о транзакции
        else:
            print("В этом блоке не было совершено транзакций")
    except KeyError:
        print("Этого блока не существует, попробуйте другой")


if __name__ == '__main__':  # На всякий случай обозначаю точку входа (адрес в оперативной памяти, по которому хранится первая команда программы, спасибо википедия)))
    transactions(block_number)
