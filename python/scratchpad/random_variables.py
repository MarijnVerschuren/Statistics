from numpy.random import Generator, PCG64
import altair as alt
import pandas as pd






def main() -> None:
	rng = Generator(PCG64())
	n = 10000
	
	m = 10
	s = 5
	
	data = [rng.normal(m, s) for _ in range(n)]
	print(data)
	print(min(data), max(data))
	
	df = pd.DataFrame({"value": data})
	chart = alt.Chart(df).mark_bar().encode(
		x=alt.X("value:Q", bin=alt.Bin(step=1)),
		y="count()"
	)
	
	chart.save("random_variables.png")

	
	
	
	
	
	
	

if __name__ == "__main__":
	main()