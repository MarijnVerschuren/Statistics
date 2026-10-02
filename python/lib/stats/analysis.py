from matplotlib.axes import Axes
from typing import Iterable, Optional, Literal
from math import sqrt


__all__ = [
	"mean",
	"median",
	"variance",
	"sd",
	
	"dataset"
]




def median(data: Iterable[float]) -> float:
	data = list(data)
	if not len(data): return 0
	data.sort()
	if len(data) % 2 == 0:
		return data[int(len(data)/2)]
	return (data[int(len(data)/2)] + data[int(len(data)/2)+1]) / 2

def mean(data: Iterable) -> float:
	data = list(data)
	if not len(data): return 0
	return sum(data) / len(data)

def variance(data: Iterable) -> float:
	data = list(data)
	if not len(data): return 0
	m = mean(data)
	return sum((x - m) ** 2 for x in data) / (len(data) - 1)

def sd(data: Iterable) -> float:
	return sqrt(variance(data))



class dataset:
	def __init__(self, data: Iterable) -> None:
		self.data = list(data)
		self.data.sort()
	
	def __len__(self) -> int:		return len(self.data)
	def __iter__(self) -> Iterable:	return iter(self.data)
	
	@property
	def min(self) -> float:			return min(self.data) if self.data else None
	@property
	def q1(self) -> float:			return median(self.data[:int(len(self)/2) + 1])
	@property
	def median(self) -> float:		return median(self.data)
	@property
	def q3(self) -> float:			return median(self.data[int(len(self)/2):])
	@property
	def max(self) -> float:			return max(self.data) if self.data else None
	
	@property
	def iqr(self) -> float:			return self.q3 - self.q1
	def iqrr(self, whis: float) -> tuple[float, float]:
		return self.q1-whis*self.iqr, self.q3+whis*self.iqr
	
	@property
	def outliers(self) -> tuple["dataset", "dataset"]:
		lb = self.q1 - self.iqr * 1.5
		ub = self.q3 + self.iqr * 1.5
		return dataset([x for x in self if x < lb]), dataset([x for x in self if x > ub])
	
	@property
	def mean(self) -> float:		return mean(self.data)
	@property
	def variance(self) -> float:	return variance(self.data)
	@property
	def sd(self) -> float:			return sd(self.data)
	
	@property
	def summary(self) -> tuple[float, float, float, float, float]:
		return self.min, self.q1, self.median, self.q3, self.max
	
	def __str__(self) -> str:	return f"summary: {self.summary}\nmean: {self.mean}, sd: {self.sd}"
	def __repr__(self) -> str:	return f"ds<{self.summary}>"
	
	def hist(
		self, ax: Axes, title: str = None, bins: int = None,
		range: tuple[float, float] = None, log: bool = False
	) -> None:
		ax.hist(self.data, bins=bins, range=range, log=log)
		if title is not None: ax.set_title(title)
	
	def box(
		self, ax: Axes, title: str = None, sym: str = "",
		orient: Literal["vertical", "horizontal"] = "horizontal",
		whis: float = 1.5
	) -> None:
		ax.boxplot(self.data, sym=sym, orientation=orient, whis=whis)
		if title is not None: ax.set_title(title)
	