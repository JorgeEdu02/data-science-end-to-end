select categoria, count(*) as numero_ventas, sum(monto_total) as monto_total
from {{ ref('int_ventas_con_producto') }}
group by categoria
order by monto_total desc
