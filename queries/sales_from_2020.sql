SELECT contract_id, client_id, c.name AS client_name
FROM sales s
JOIN clients c ON s.client_id = c.id
WHERE sale_date >= '2020-01-01';