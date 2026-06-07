#! /usr/bin/env python3


import typing
import abc


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self.stock = []

    def output(self, data: typing.Any) -> typing.Any:
        pass

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def output(self, data: typing.Any) -> typing.Any:
        pass

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, list):
            if all(isinstance(x, (int, float)) for x in data):
                return True
            else:
                return False
        else:
            return False

    def ingest(self, data: typing.Any) -> None:
        if self.validate(data):
            if isinstance(data, list):
                self.stock.extend(str(x) for x in data)
            else:
                self.stock.append(str(data))
        else:
            raise ValueError("Invalid data type for NumericProcessor")


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def output(self, data: typing.Any) -> typing.Any:
        pass

    def validate(self, data: typing.Any) -> bool:
        return isinstance(data, str)

    def ingest(self, data: typing.Any) -> None:
        if self.validate(data):
            self.data.append(data)
        else:
            raise ValueError("Invalid data type for TextProcessor")


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def output(self, data: typing.Any) -> typing.Any:
        pass

    def validate(self, data: typing.Any) -> bool:
        return isinstance(data, (int, float, str))

    def ingest(self, data: typing.Any) -> None:
        if self.validate(data):
            self.data.append(data)
        else:
            raise ValueError("Invalid data type for LogProcessor")
