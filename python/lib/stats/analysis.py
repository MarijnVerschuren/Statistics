from typing import Iterable
from math import sqrt



__all__ = [
	"mean",
	"median",
	"variance",
	"sd"
]




def median(data: Iterable[float]) -> float:
	data = list(data); data.sort()
	if len(data) % 2 == 0:
		return data[int(len(data)/2)]
	return (data[int(len(data)/2)] + data[int(len(data)/2)+1]) / 2

def mean(data: Iterable) -> float:
	data = list(data)
	return sum(data) / len(data)

def variance(data: Iterable) -> float:
	data = list(data); m = mean(data)
	return sum((x - m) ** 2 for x in data) / (len(data) - 1)

def sd(data: Iterable) -> float:
	return sqrt(variance(data))

