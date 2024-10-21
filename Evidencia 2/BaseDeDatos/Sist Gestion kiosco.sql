-- Base de datos de Sistema de Gestion de Kiosco
create database if not exists Sistema_de_gestion_kiosco;

use Sistema_de_gestion_kiosco;

create table proveedor (
id_proveedor int auto_increment,
nombre_proveedor varchar (45) not null,
apellido_proveedor varchar (45) not null,
telefono_proveedor varchar (45) not null,
email_proveedor varchar (45),
direccion varchar (45),

primary key (id_proveedor) -- Clave primaria de tabla proveedores 
);

create table producto (
id_producto int auto_increment,
nombre_producto varchar (45) not null,
tipo_producto enum ('bebidas', 'alimentos', 'cigarrillos', 'limpieza', 'golosinas'),
unidades int,
precio_venta decimal (10,2),
vencimiento date not null,
id_proveedor int,

-- Claves primarias y secundarias de la tabla productos
primary key (id_producto),
foreign key (id_proveedor) references proveedor (id_proveedor) on delete cascade
);


create table empleado (
id_empleado int auto_increment,
nombre_empleado varchar (45) not null,
apellido_empleado varchar (45) not null,
DNI int not null unique,
telefono varchar(30),
cargo enum ('Gerente', 'Cajero', 'Repositor', 'Administracion') not null,
salario decimal (10,2) not null,
ingreso datetime not null,
salida datetime,
contraseña varchar(256) , 


primary key (id_empleado)
);

create table sucursal (
id_sucursal int auto_increment,
direccion varchar (45) not null,
nombre varchar (45) not null,
telefono varchar (30) not null,
email varchar (45) not null,
encargado int,

primary key (id_sucursal),
foreign key (encargado) references empleado(id_empleado) on delete set null
);

create table empleados_por_sucursal (
id_sucursal int,
id_empleado int,

primary key (id_sucursal, id_empleado),
foreign key (id_sucursal) references sucursal (id_sucursal) on delete cascade,
foreign key (id_empleado) references empleado (id_empleado) on delete cascade
);

create table venta (
id_venta int not null auto_increment,
fecha_venta datetime not null,
modo_de_pago enum ('Efectivo', 'Tarjeta de debito','Tarjeta de credito', 'transferencia') not null,
id_empleado int,
id_sucursal int not null,

primary key (id_venta),
foreign key (id_empleado) references empleado (id_empleado) on delete no action ,
foreign key (id_sucursal) references sucursal (id_sucursal) on delete no action
);

create table detalle_venta (
id_venta int ,
id_producto int,
cantidad int not null,
total float not null,

primary key (id_venta, id_producto), -- Clave primaria de tabla detalle de ventra
foreign key (id_producto) references producto (id_producto) on delete no action, -- Clave secundaria de la tabla detalle de venta
foreign key (id_venta) references venta (id_venta) -- Clave secundaria de la tabla detalle de venta

);


-- Trigger para actualizar el stock de un producto.

delimiter //
create trigger update_stock after insert on detalle_venta
for each row 
BEGIN
IF NEW.cantidad <= (SELECT unidades from producto where id_producto = NEW.id_producto) THEN
		UPDATE producto
		set unidades = unidades - NEW.cantidad
		where id_producto = NEW.id_producto;
ELSE 
	signal sqlstate'45000' SET message_text = 'Cantidad de productos insuficiente';
END IF;
END //
delimiter ;

