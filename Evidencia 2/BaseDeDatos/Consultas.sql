-- Cantidad de unidades vendidas por producto.

select p.nombre_producto as Producto, sum(d.cantidad) as 'Unidades vendiadas' from detalle_venta d
inner join producto p on p.id_productos = d.id_producto 
group by p.nombre_producto
order by sum(d.cantidad) desc;

-- Cantidad de productos vendidos por mes.

select monthname(v.fecha_venta) as MES , 
p.nombre_producto as Producto , 
sum(d.cantidad) as 'Unidades Vendidas',
rank() over(partition by monthname(v.fecha_venta) order by sum(d.cantidad) desc) as Ranking  
from detalle_venta d
inner join producto p on p.id_producto = d.id_producto
inner join venta v on v.id_venta = d.id_venta
group by monthname(v.fecha_venta) , p.nombre_producto; 

-- Cantidad de ventas por empleado.

select e.nombre_empleado AS 'Empleado', count(*) as 'Ventas' from empleado e
inner join venta d on d.id_empleado = e.id_empleado
group by e.nombre_empleado
order by count(*) desc;

-- Cantidad de venta por mes.

select monthname(fecha_venta) as MES, count(*) as Cantidad from venta
group by monthname(fecha_venta);

-- CRUD

SELECT nombre_producto FROM producto;

INSERT INTO producto(nombre_producto, tipo_producto, unidades, precio_venta, vencimiento, id_proveedor)
VALUES ('BonOBon', 1, 1000, 500, "2026-09-19 10:15:14" , 2);

UPDATE producto SET precio_venta = 750 where nombre_producto = 'BonOBon';

DELETE FROM producto WHERE nombre_producto = 'BonOBon';

