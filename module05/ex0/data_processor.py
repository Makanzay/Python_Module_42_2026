#! /usr/bin/env python3


import typing
import abc


class DataProcessor(abc.ABC):
    @abc.abstractmethod
    def process(self, data: typing.Any) -> typing.Any:
        pass
    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass
    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

class  NumericProcessor(DataProcessor):
    def process(self, data: typing.Any) -> typing.Any
        pass
    def validate(self, data: typing.Any) -> bool:
        pass

class TextProcessor(DataProcessor):
    def process(self, data: typing.Any) -> typing.Any:
        pass
    def validate(self, data: typing.Any) -> bool:
        pass

class TextProcessor(DataProcessor):
    def process(self, data: typing.Any) -> typing.Any:
        pass
    def validate(self, data: typing.Any) -> bool:
        pass

    
class LogProcessor(DataProcessor):
    def process(self, data: typing.Any) -> typing.Any:
        pass
    def validate(self, data: typing.Any) -> bool:
        pass
