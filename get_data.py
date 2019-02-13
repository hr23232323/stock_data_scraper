import stock_scraper as ss
import pandas as pd

def createList():
	df = pd.read_csv("sp500-constituents.csv")
	stock_list = df['Symbol'].values
	return stock_list

def main():
	stock_list = createList()
	interested = ['Market Cap (intraday)', 'Return on Equity', 'Revenue', 'Quarterly Revenue Growth', 
	'Operating Cash Flow', 'Total Cash', 'Total Debt', 'Current Ratio', '52-Week Change',
	'Avg Vol (3 month)', 'Avg Vol (10 day)', '% Held by Insiders']
	technicals = {}
	df = pd.DataFrame(columns=interested)
	for each_stock in stock_list:
		tech = ss.scrape_yahoo(each_stock)
		for ind in interested:	
			try:
				df.at[each_stock, ind] = tech[ind]
			except Exception as e:
				print('Failed, exception: ', str(e))
		print("DONE- " + each_stock)
	#Correct column name
	df.rename(index=str, columns={df.columns[0]: "Symbol"}, inplace=True)
	
	# Merge symbols with data df to get name of company and industry
	df = df.join(df_symbols.set_index('Symbol'), on="Symbol")

	# Drop rows with excessive NaN values
	df.dropna(thresh=10, inplace=True)

	# Save as CSV
	df.to_csv("data.csv")


if __name__ == "__main__":
	main()