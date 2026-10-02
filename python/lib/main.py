from typing import Optional, Iterable

from uniplot import histogram
import matplotlib.pyplot as plt
from functools import partial

from stats import *







def main() -> None:
	pass







def plotting_test() -> None:
	rng = RNG_cauchy(0, .8, uu_fn)
	ds = dataset(rng(100000))
	lout, uout = ds.outliers
	print(ds, lout, uout, sep="\n\n")
	
	fig_ds, ax_ds = plt.subplots(2, figsize=(10,10))
	ds.hist(ax_ds[0], "dataset hist", bins=100, range=ds.iqrr(1.5))
	ds.box( ax_ds[1], "dataset box")
	fig_ds.show()
	
	fig_out, ax_out = plt.subplots(2, figsize=(10,10))
	lout.hist(ax_out[0], "lower outliers",		bins=100, log=True, range=(-2500, 0))
	uout.hist(ax_out[1], "higher outliers",	bins=100, log=True, range=(0,  2500))
	fig_out.show()


if __name__ == "__main__":
	plotting_test()
	main()



# TODO: seaborn
# TODO: quickselect



# def distribution_test(
# 		rng: RNG_unit_uniform,
# 		title: str,
# 		plot_fn: callable,
# 		plot_range: Optional[tuple[float, float]] = None,
# ) -> None:
# 	for i, a in enumerate(rng(8*8)):
# 		if i % 8 == 0: print()
# 		print(a, end="\t")
# 	else: print("\n")
#
# 	n = 100000
# 	data = list(rng(n))
# 	print(f"n samples: {n}\nmin: {min(data)}, max: {max(data)}, mean: {mean(data)}, sd: {sd(data)}")
# 	plot_fn(title, data, 100, plot_range)
#
# def tests() -> None:
# 	matplot = lambda ax, title, data, bins, range:	(ax.hist(data, bins=bins, range=range), ax.set_title(title))
# 	terminal = lambda title, data, bins, range:		(print(title), histogram(data, bins=bins, bins_min=range[0], bins_max=range[1]))
#
# 	fig_smpl, ax_smpl = plt.subplots(nrows=2, figsize=(10, 10))
# 	distribution_test(RNG_unit_uniform(uu_fn),				"unit uniform",		partial(matplot, ax_smpl[0]))
# 	distribution_test(RNG_bernoulli(0.4, uu_fn), 		"bernoulli(0.4)",		partial(matplot, ax_smpl[1]))
# 	fig_smpl.show()
#
# 	fig_bell, ax_bell = plt.subplots(nrows=3, figsize=(10, 10))
# 	distribution_test(RNG_unit_normal(uu_fn),				"unit normal",			partial(matplot, ax_bell[0]))
# 	#distribution_test(RNG_normal(4, 2, uu_fn),	"normal(4, sd=2)")
# 	distribution_test(RNG_reyleigh(2.5, uu_fn),			"reyleigh(2.5)",		partial(matplot, ax_bell[1]))
# 	distribution_test(RNG_cauchy(4, .8, uu_fn),	"cauchy(4, 0.8)",		partial(matplot, ax_bell[2]), (-2, 8))
# 	fig_bell.show()
#
# 	fig_exp, ax_exp = plt.subplots(nrows=3, figsize=(10, 10))
# 	distribution_test(RNG_exponential(0.5, uu_fn),		"exponential(0.5)",	partial(matplot, ax_exp[0]))
# 	distribution_test(RNG_geometric(0.04, uu_fn),		"geometric(0.04)",		partial(matplot, ax_exp[1]))
# 	distribution_test(RNG_pareto(20, 1, uu_fn),	"pareto(20, 1)",		partial(matplot, ax_exp[2]))
# 	fig_exp.show()
#
