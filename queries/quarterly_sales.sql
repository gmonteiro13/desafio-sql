SELECT SUM(sales_values) AS sales_values, year, quarter, (year || '-' || quarter) AS year_quarter
FROM (
	SELECT s.value AS sales_values, 
		   strftime('%Y', s.sale_date) AS year,
		   (CAST(strftime('%m', s.sale_date) AS INTEGER) + 2) / 3 AS quarter
	FROM sales s
)
GROUP BY year, quarter, year_quarter;