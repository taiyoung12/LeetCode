# Write your MySQL query statement below
select V.customer_id, count(V.visit_id) as count_no_trans
from Visits as V
left join Transactions as T on T.visit_id = V.visit_id 
where T.transaction_id is null
GROUP BY v.customer_id
ORDER BY v.customer_id;