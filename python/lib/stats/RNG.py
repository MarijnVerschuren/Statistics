from collections.abc import generator
from random import uniform
from functools import partial
from math import sqrt, log, cos, sin, tan, pi

# unit uniform
uu_fn = partial(uniform, 0, 1)



__all__ = [
	"uu_fn",
	"RNG_unit_uniform",
	"RNG_unit_normal",
	"RNG_normal",
	"RNG_bernoulli",
	"RNG_geometric",
	"RNG_exponential",
	"RNG_unit_cauchy",
	"RNG_cauchy",
	"RNG_pareto",
	"RNG_reyleigh"
]



class RNG_unit_uniform:
	""" uurng_src: a function that generates a uniform random number between 0 and 1 """
	def __init__(self, uu_fn: callable):
		super().__init__()
		self.src = uu_fn
		
	def inv_cdf(self, x: float) -> float:	return x
	def __iter__(self) -> iter:				return self
	def next(self) -> float:				return self.inv_cdf(self.src())
	def __next__(self) -> float:			return self.next()
	
	def __call__(self, count: int) -> generator:
		return (self.next() for _ in range(count))



class RNG_unit_normal(RNG_unit_uniform):
	""" uurng_src: a function that generates a uniform random number between 0 and 1 """
	def __init__(self, uu_fn: callable):
		super().__init__(uu_fn)
		self.gen = iter(self)
		
	def inv_cdf(self, x: float) -> float:	return 0	# TODO there is no analytical
	def __iter__(self):
		def gen():
			while True:
				u1 = self.src(); u2 = self.src() * 2 * pi
				yield sqrt(-2 * log(u1)) * cos(u2)
				yield sqrt(-2 * log(u1)) * sin(u2)
		return gen()
	def next(self):	return next(self.gen)


class RNG_normal(RNG_unit_normal):
	""" uurng_src: a function that generates a uniform random number between 0 and 1 """
	def __init__(self, mean: float, sd: float, uu_fn: callable):
		super().__init__(uu_fn)
		self.gen = iter(self)
		self.mean = mean
		self.sd = sd

	def next(self):	return self.mean + self.sd * next(self.gen)



class RNG_bernoulli(RNG_unit_uniform):
	def __init__(self, p: float, uu_fn: callable):
		super().__init__(uu_fn)
		self.p = p
	
	def inv_cdf(self, x: float) -> float:	return 1 if self.src() > self.p else 0



class RNG_geometric(RNG_unit_uniform):
	def __init__(self, p: float, uu_fn: callable):
		super().__init__(uu_fn)
		self.p = p

	def inv_cdf(self, x: float) -> float:	return log(1-x) / log(1-self.p)



class RNG_exponential(RNG_unit_uniform):
	def __init__(self, p: float, uu_fn: callable):
		super().__init__(uu_fn)
		self.p = p # lambda
		
	def inv_cdf(self, x: float) -> float:	return log(1 - x) / (-self.p)



class RNG_unit_cauchy(RNG_unit_uniform):
	def __init__(self, uu_fn: callable):
		super().__init__(uu_fn)
		
	def inv_cdf(self, x: float) -> float:	return tan(pi * (x-0.5))


class RNG_cauchy(RNG_unit_cauchy):
	def __init__(self, loc: float, scale: float, uu_fn: callable):
		super().__init__(uu_fn)
		self.scale = scale
		self.loc = loc

	def next(self):	return self.loc + self.scale * super().next()


class RNG_pareto(RNG_unit_uniform):
	def __init__(self, alpha: float, xm: float, uu_fn: callable):
		super().__init__(uu_fn)
		self.alpha = alpha
		self.xm = xm
		
	def inv_cdf(self, x: float) -> float:	return self.xm / pow(1-x, 1/self.alpha)



class RNG_reyleigh(RNG_unit_uniform):
	def __init__(self, sig: float, uu_fn: callable):
		super().__init__(uu_fn)
		self.sig = sig

	def inv_cdf(self, x: float) -> float:	return sqrt(-2 * self.sig**2 * log(1-x))



