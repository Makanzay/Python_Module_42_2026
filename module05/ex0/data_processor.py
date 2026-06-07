#! /usr/bin/env python3


import typing
import abc


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self.data = []

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
                raise ValueError("Invalid data type for NumericProcessor:"
                                 " list contains non-numeric values")
        else:
            raise ValueError("Invalid data type for NumericProcessor")
        return False

    def ingest(self, data: typing.Any) -> None:
        pass


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def output(self, data: typing.Any) -> typing.Any:
        pass

    def validate(self, data: typing.Any) -> bool:
        return isinstance(data, str)

    def ingest(self, data: typing.Any) -> None:
        pass


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.data = []

    def output(self, data: typing.Any) -> typing.Any:
        pass

    def validate(self, data: typing.Any) -> bool:
        return isinstance(data, (int, float, str))

    def ingest(self, data: typing.Any) -> None:
        self.data.append(data)
