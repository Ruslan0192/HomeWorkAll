from multiprocessing import Process

class WarehouseManager():
    def __init__(self, *args, **kwargs):
         self.data = {}
    def process_request(self, request):
    #     реализует запрос (действие с товаром), принимая request - кортеж.
    #     Есть 2 действия: receipt - получение, shipment - отгрузка.
    # а) В случае получения данные должны поступить в data (добавить пару, если её не было и изменить значение ключа, если позиция уже была в словаре)
    # б) В случае отгрузки данные товара должны уменьшаться (если товар есть в data и если товара больше чем 0).
        if request[0]  in self.data:
            if request[1] == 'receipt':
                self.data[request[0]] += request[2]
            else:
                if self.data[request[0]] < request[2]:
                    self.data[request[0]] = 0
                else:
                    self.data[request[0]] -= request[2]
        else:
            if request[1] == 'receipt':
                self.data[request[0]] = request[2]
            else:
                self.data[request[0]] = 0

    def run(self,requests):
    #  принимает запросы и создаёт для каждого свой параллельный процесс, запускает его(start) и замораживает(join).
        for request in requests:
            process = Process(target=self.process_request(request))
            process.start()
            process.join()


if __name__ == '__main__':
    manager = WarehouseManager()
    # Множество запросов на изменение данных о складских запасах
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    manager.run(requests)
    print(manager.data)
