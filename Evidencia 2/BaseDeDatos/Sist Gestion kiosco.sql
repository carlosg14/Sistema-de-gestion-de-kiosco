-- Base de datos de Sistema de Gestion de Kiosco
create database if not exists Sistema_de_gestion_kiosco;

use Sistema_de_gestion_kiosco;

create table proveedores (
id_proveedores int auto_increment,
nombre_proveedor varchar (45) not null,
apellido_proveedor varchar (45) not null,
telefono_proveedor varchar (45) not null,
email_proveedor varchar (45),
direccion varchar (45),

primary key (id_proveedores) -- Clave primaria de tabla proveedores 
);

create table productos (
id_productos int auto_increment,
nombre_producto varchar (45) not null,
tipo_producto enum ('bebidas', 'alimentos', 'cigarrillos', 'limpieza', 'golosinas'),
unidades int,
precio_venta decimal (10,2),
vencimiento datetime not null,
id_proveedores int,

-- Claves primarias y secundarias de la tabla productos
primary key (id_productos),
foreign key (id_proveedores) references proveedores (id_proveedores)
);


create table empleados (
id_empleados int auto_increment,
nombre_empleado varchar (45) not null,
apellido_empleado varchar (45) not null,
DNI int not null,
telefono varchar(30),
cargo enum ('Gerente', 'Cajero', 'Repositor', 'Administracion') not null,
salario decimal (10,2) not null,
ingreso datetime not null,
salida datetime,
contraseña varchar(45), 


primary key (id_empleados)
);

create table sucursal (
id_sucursal int auto_increment,
direccion varchar (45) not null,
nombre varchar (45) not null,
telefono varchar (30) not null,
email varchar (45) not null,
encargado int,

primary key (id_sucursal),
foreign key (encargado) references empleados(id_empleados)
);

create table empleados_por_sucursal (
id_sucursal int,
id_empleados int,

primary key (id_sucursal, id_empleados),
foreign key (id_sucursal) references sucursal (id_sucursal),
foreign key (id_empleados) references empleados (id_empleados)
);

create table ventas (
id_ventas int not null auto_increment,
fecha_venta datetime not null,
modo_de_pago enum ('Efectivo', 'Tarjeta de debito','Tarjeta de credito', 'transferencia') not null,
id_empleados int,
id_sucursal int not null,

primary key (id_ventas),
foreign key (id_empleados) references empleados (id_empleados),
foreign key (id_sucursal) references sucursal (id_sucursal)
);

create table detalle_venta (
id_venta int ,
id_productos int,
cantidad int not null,
total float not null,

primary key (id_venta, id_productos), -- Clave primaria de tabla detalle de ventra
foreign key (id_productos) references productos (id_productos), -- Clave secundaria de la tabla detalle de venta
foreign key (id_venta) references ventas (id_ventas) -- Clave secundaria de la tabla detalle de venta

);


-- Trigger para actualizar el stock de un producto.

delimiter //
create trigger update_stock after insert on detalle_venta
for each row 
BEGIN
	UPDATE productos 
    set unidades = unidades - NEW.cantidad
    where id_productos = NEW.id_productos;
END //
delimiter ;

