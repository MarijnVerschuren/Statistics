import matplotlib.pyplot as plt
from scipy import stats
from math import sqrt

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

def stats_hw_w2_ex3() -> None:
	n = 200
	a_ex, b_ex = -5, 3
	rng = RNG_uniform(a_ex, b_ex, uu_fn)
	def sim() -> tuple[float, float, float, float]:
		data = list(rng(n))
		A = mean(data)
		B = mean([x**2 for x in data])
		a_mm = A - sqrt(3 * (B - A**2))
		b_mm = A + sqrt(3 * (B - A**2))
		a_ml = min(data); b_ml = max(data)
		return a_mm, b_mm, a_ml, b_ml
		
	
	with Exercise("EX3", (1, 0)) as ex:
		with ex.subquestion("D") as d:
			a_mm_mse = []; b_mm_mse = []
			a_ml_mse = []; b_ml_mse = []
			for _ in range(10000):
				a_mm, b_mm, a_ml, b_ml = sim()
				a_mm_mse.append((a_mm - a_ex) ** 2)
				b_mm_mse.append((b_mm - b_ex) ** 2)
				a_ml_mse.append((a_ml - a_ex) ** 2)
				b_ml_mse.append((b_ml - b_ex) ** 2)
			
			d.print(
				"method of moments:\n"
				f" - min mse a: {min(a_mm_mse)}, b: {min(b_mm_mse)}\n"
				f" - max mse a: {max(a_mm_mse)}, b: {max(b_mm_mse)}\n"
				f" - avg mse a: {mean(a_mm_mse)}, b: {mean(b_mm_mse)}\n"
			)
			
			d.print(
				"maximum likelihood:\n"
				f" - min mse a: {min(a_ml_mse)}, b: {min(b_ml_mse)}\n"
				f" - max mse a: {max(a_ml_mse)}, b: {max(b_ml_mse)}\n"
				f" - avg mse a: {mean(a_ml_mse)}, b: {mean(b_ml_mse)}\n"
			)
			
			bsize = 0.05
			bmax = 2.5
			bins = [bsize*x for x in range(0, int(bmax/bsize))]
			log = True
			
			fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))
			ax[0][0].hist(a_mm_mse, bins=bins, log=log)
			ax[0][0].set_title("MSE of MM estimator for 'a'")
			ax[0][1].hist(b_mm_mse, bins=bins, log=log)
			ax[0][1].set_title("MSE of MM estimator for 'b'")
			ax[1][0].hist(a_ml_mse, bins=bins, log=log)
			ax[1][0].set_title("MSE of MLE estimator for 'a'")
			ax[1][1].hist(b_ml_mse, bins=bins, log=log)
			ax[1][1].set_title("MSE of MLE estimator for 'a'")
			
			fig.show()
		
	
def stats_hw_w3_ex1() -> None:
	pass


			


def main() -> None:
	#stats_hw_w2_ex1()
	#stats_hw_w2_ex3()
	stats_hw_w3_ex1()

