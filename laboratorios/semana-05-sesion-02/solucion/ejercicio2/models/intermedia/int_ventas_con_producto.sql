select v.id_venta, v.fecha, v.id_producto, v.unidades,
       p.nombre, p.categoria, p.precio,
       v.unidades * p.precio as monto_total
from {{ ref('stg_ventas') }} v
join {{ ref('stg_productos') }} p using (id_producto)
