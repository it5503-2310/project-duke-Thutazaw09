from typing import Any


class DB:
    __storage: list[Any]
    __count: int

    def __init__(self) -> None:
        self.__storage = []
        self.__count = 0

    def addItem(self, item: Any) -> None:
        self.__storage.append(item)
        self.__count += 1

    def getItem(self, position: int) -> Any:
        return self.__storage[position]

    def getCount(self) -> int:
        return self.__count

    def remmoveItem(self, position: int) -> Any:
        if self.__count >= 1:

            if 0 <= position < self.__count:  # Check if 'position' is within bounds
                self.__count -= 1
                return self.__storage.pop(position)
            else:
                raise IndexError("Invalid position")
        else:
            raise IndexError("No items to remove")

    def getStorage(self) -> list[Any]:
        return self.__storage

    def clearStorage(self) -> None:
        self.__storage[:] = []
