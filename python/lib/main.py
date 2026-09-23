from typing import Optional, Iterable

from uniplot import histogram
import matplotlib.pyplot as plt
from scipy import stats

from stats import *
from excersise import *



def stats_hw_w2_ex1() -> None:
	data = [
		84, 49, 61, 40, 83, 67, 45, 66, 70, 69,
		80, 58, 68, 60, 67, 72, 73, 70, 57, 63,
		70, 78, 52, 67, 53, 67, 75, 61, 70, 81,
		76, 79, 75, 76, 58, 31
	]
	
	with Exercise("EX1", (1, 0)) as ex:
		with ex.subquestion("A") as a:
			a.print(f"data: {data}")
			a.print(
				f"mean: {mean(data)},\n"
				f"variance: {variance(data)},\n"
				f"sd: {sd(data)},\n"
				f"median: {median(data)}"
			)
	
			fig, ax = plt.subplots()
			ax.hist(data, bins=13)
			ax.set_title("data histogram")
			fig.show()
	
		with ex.subquestion("B") as b:
			b.print(f"boxplot shows a significant outlier")
			fig, ax = plt.subplots()
			ax.boxplot(data)
			ax.set_title("data boxplot")
			fig.show()
	
		with ex.subquestion("C") as c:
			outlier = min(data)
			data.remove(outlier)
	
			c.print(f"data without outlier: {outlier}")
			c.print(
				f"mean: {mean(data)},\n"
				f"variance: {variance(data)},\n"
				f"sd: {sd(data)},\n"
				f"median: {median(data)}"
			)
	
		with ex.subquestion("D") as d:
			d.print(
				"The data is approximately linear on the "
				"QQ-plot, so it is approximately normal."
			)
	
			fig, ax = plt.subplots()
			stats.probplot(data, dist="norm", plot=ax)
			ax.set_title("data QQ plot")
			fig.show()
	
			ex1 = RNG_normal(mean(data), sd(data), uu_fn)
	
			fig, ax = plt.subplots()
			ax.hist(list(ex1(10000)), bins=range(30, 80))
			ax.set_title("normal distribution of estimators")
			fig.show()
	
		with ex.subquestion("E") as e:
			m_before, v_before = mean(data), variance(data)
	
			data = [(5 / 9) * (x - 32) for x in data]
	
			e.print(f"data: {data}")
			e.print(
				f"mean: {mean(data)},\n"
				f"variance: {variance(data)},\n"
				f"sd: {sd(data)},\n"
				f"median: {median(data)}"
			)
	
			e.print(
				"when calculating directly via original values\n"
				f"mean: {(5/9) * m_before - (160/9)},\n"
				f"variance: {(25/81) * v_before}"
			)
	
			fig, ax = plt.subplots()
			ax.hist(data, bins=9)
			ax.set_title("data histogram")
			fig.show()




def stats_hw_w2_ex2() -> None:
	pass


def main() -> None:
	stats_hw_w2_ex1()



# TODO: seaborn
if __name__ == "__main__":
	main()

	
	
	

	


# TODO: quickselect


# def distribution_test(
# 		rng: RNG_unit_uniform,
# 		plot_min: Optional[float] = None,
# 		plot_max: Optional[float] = None
# ) -> None:
# 	fig1a, ax1a = plt.subplots()
# 	for i, a in enumerate(rng(8*8)):
# 		if i % 8 == 0: print()
# 		print(a, end="\t")
# 	else: print("\n")
#
# 	n = 100000
# 	data = list(rng(n))
# 	print(f"n samples: {n}\nmin: {min(data)}, max: {max(data)}, mean: {mean(data)}, sd: {sd(data)}")
# 	histogram(data, bins=100, bins_min=plot_min, bins_max=plot_max)
#
#
# def tests() -> None:
# 	fig1a, ax1a = plt.subplots()
# 	distribution_test(RNG_unit_uniform(uu_fn))
# 	distribution_test(RNG_unit_normal(uu_fn))
# 	distribution_test(RNG_normal(4, 2, uu_fn))
# 	distribution_test(RNG_exponential(0.5, uu_fn))
# 	distribution_test(RNG_cauchy(4, .8, uu_fn),					-2, 8)
# 	#distribution_test(RNG_pareto(20, 1, uu_fn))
# 	distribution_test(RNG_bernoulli(0.4, uu_fn))
# 	#distribution_test(RNG_geometric(0.04, uu_fn))
# 	distribution_test(RNG_reyleigh(2.5, uu_fn))



