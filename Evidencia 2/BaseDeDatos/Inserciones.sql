
use sistema_de_gestion_kiosco;

-- Inserciones de la tabla empleados.

INSERT INTO empleado(nombre_empleado, apellido_empleado, DNI, telefono, cargo, salario, ingreso, salida, contraseña)
VALUES ("Mia Morena", "Hernandez", 3555596, "+54 15 2497 6788", 3, 648844, "2020-08-18 21:26:32", "2020-08-19 05:26:32", sha2('1234', 256)),
("Maximo", "Gomez", 3541149, "+54 9 3181 7367", 4, 320367, "2021-05-15 00:11:51", "2021-05-15 08:11:51", sha2('1234', 256)),
("Santino Benjamin", "Gutierrez", 3900279, "+54 9 3436 2878", 4, 991775, "2023-06-12 05:14:42", "2023-06-12 13:14:42", sha2('1234', 256)),
("Benjamin Ezequiel", "Ponce", 3165185, "+54 15 2252 1906", 1, 596068, "2021-03-27 16:37:41", "2021-03-28 00:37:41", sha2('1234', 256)),
("Sara", "Garcia", 3834451, "+54 15 2232 6698", 1, 53820, "2020-11-05 02:56:15", "2020-11-05 10:56:15", sha2('1234', 256)),
("Malena", "Romero", 3695201, "+54 9 3594 6626", 2, 969742, "2023-10-20 07:29:08", "2023-10-20 15:29:08", sha2('1234', 256)),
("Juan Bautista", "Martinez", 3684961, "+54 15 2644 2143", 1, 573607, "2021-11-11 07:19:30", "2021-11-11 15:19:30", sha2('1234', 256)),
("Ciro Benjamin", "Ramirez", 3891843, "+54 9 3395 2217", 2, 215626, "2023-01-22 07:59:33", "2023-01-22 15:59:33", sha2('1234', 256)),
("Thiago Benjamin", "Rodriguez", 3880399, "+54 9 3975 6507", 4, 35366, "2023-09-04 18:36:36", "2023-09-05 02:36:36", sha2('1234', 256)),
("Santino Benjamin", "Vazquez", 3657395, "+54 9 3612 2858", 1, 438308, "2021-11-21 02:39:25", "2021-11-21 10:39:25", sha2('1234', 256)),
("Tomàs", "Martinez", 3878599, "+54 15 2412 0672", 2, 900622, "2021-07-11 02:42:17", "2021-07-11 10:42:17", sha2('1234', 256)),
("Juana", "Duarte", 3212847, "+54 9 3198 5398", 4, 141961, "2020-02-25 03:54:15", "2020-02-25 11:54:15", sha2('1234', 256)),
("Angel Gabriel", "Carrizo", 3653076, "+54 15 2278 8322", 3, 413992, "2020-05-19 09:55:41", "2020-05-19 17:55:41", sha2('1234', 256)),
("Lautaro Nicolas", "Lopez", 3808054, "+54 9 3773 7769", 2, 532468, "2023-08-06 12:00:08", "2023-08-06 20:00:08", sha2('1234', 256)),
("Juan Ignacio", "Garcia", 3079458, "+54 9 3764 7980", 3, 968543, "2020-09-19 00:15:14", "2020-09-19 08:15:14", sha2(1234, 256));

-- Inserciones de la tabla sucursal.

INSERT INTO sucursal(direccion, nombre, telefono, email, encargado)
VALUES("Blv. 6 N° 45", "Mitre", "+54 9 3814 8500", "Mitre@gmail.com", 4),
("Diag. Santa Fe N° 110", "Belgrano", "+54 15 2154 6370", "Belgrano@gmail.com", 10),
("Boulevard Santa Cruz N° 369", "J.J. Castelli", "+54 9 3389 8284", "J.J. Castelli@gmail.com", 5),
("Av. Formosa N° 286", "San Martin", "+54 15 2161 4799", "San Martin@gmail.com", 10),
("Diagonal Merlo N° 146", "J.M. de Rosas", "+54 9 3598 3130", "J.M. de Rosas@gmail.com", 4);

-- Inserciones de la tabla empleados_por_sucursal.

INSERT INTO empleados_por_sucursal(id_sucursal, id_empleado)
VALUES (4, 15),
(5, 8),
(5, 12),
(2, 12),
(4, 8),
(5, 9),
(4, 14),
(2, 2),
(4, 6),
(5, 1);

-- Inserciones de la tabla proveedores.

INSERT INTO proveedor(nombre_proveedor, apellido_proveedor, telefono_proveedor, email_proveedor, direccion)
VALUES ("Romero-Leiva", "Romero-Leiva", "+54 15 2685 6526", "biancapereyra@martinez.net.ar", "Diag. Alvear N° 533"),
("Flores, Carrizo and Rodriguez", "Flores, Carrizo and Rodriguez", "+54 9 3508 7049", "mpaez@rodriguez.org", "Av. Alem N° 6311"),
("Mendoza-Perez", "Mendoza-Perez", "+54 9 3864 5514", "sotosalvador@peralta-blanco.ar", "Calle San Martin N° 495"),
("Gomez-Rodriguez", "Gomez-Rodriguez", "+54 15 2410 7239", "esanchez@gutierrez.net", "Av. 4 N° 3115"),
("Rodriguez, Ayala and Silva", "Rodriguez, Ayala and Silva", "+54 9 3627 7428", "guadalupegarcia@leiva-romero.com.ar", "Diagonal 167 B N° 6464"),
("Gimenez-Vega", "Gimenez-Vega", "+54 9 3215 9770", "oquiroga@alvarez.com", "Camino Mitre N° 3452"),
("Barrios Inc", "Barrios Inc", "+54 15 2230 8402", "leon17@chavez.net.ar", "Camino Santa Fe N° 719"),
("Martinez, Ferreyra and Silva", "Martinez, Ferreyra and Silva", "+54 9 3202 4534", "constantino21@pereyra-figueroa.com", "Diagonal J.B. Alberdi N° 104"),
("Ruiz Ltd", "Ruiz Ltd", "+54 15 2590 1901", "santino-gabrieltorres@peralta.ar", "Avenida Resistencia N° 1130"),
("Garcia Ltd", "Garcia Ltd", "+54 15 2482 4987", "renata28@silva.ar", "Av. Buenos Aires N° 35");

-- Inserciones de la tabla productos.

INSERT INTO producto(nombre_producto, tipo_producto, unidades, precio_venta, vencimiento, id_proveedor)
VALUES ('Coca-Cola', 1, 1000, 2000, "2026-09-19 " , 2),
('Pritty', 1, 1000, 1000, "2026-01-01 " , 3),
('Galletas Trio', 2, 1000, 1500, "2025-09-19" , 4),
('Malboro', 3, 1000, 300, "2027-11-19 " , 8),
('Caramelos masticables', 5, 2000, 50, "2026-09-19 " , 5),
('Lavandina', 4, 50, 1500, "2026-09-19 " , 2),
('Detergente', 4, 30, 1550, "2026-09-19 " , 2);

-- Inserciones de la tabla ventas.

INSERT INTO venta(fecha_venta, modo_de_pago, id_empleado, id_sucursal)
VALUES ("2020-06-27 11:20:20", "4", "15", "4"),
("2021-02-15 10:04:07", "3", "14", "4"),
("2021-09-08 14:14:48", "2", "15", "4"),
("2021-01-16 02:34:23", "3", "12", "5"),
("2022-11-02 14:50:35", "4", "15", "4"),
("2022-03-02 03:41:50", "4", "1", "5"),
("2022-09-13 19:47:18", "3", "1", "5"),
("2021-10-04 02:17:44", "2", "9", "5"),
("2021-10-18 09:55:28", "4", "9", "5"),
("2022-10-12 16:22:51", "3", "2", "2");


-- Inserciones de la tabla detalle_venta.

INSERT INTO detalle_venta(id_venta, id_producto, cantidad, total)
VALUES ("4", "6", "6", "9000"),
("10", "1", "9", "18000"),
("2", "2", "5", "5000"),
("8", "5", "5", "250"),
("9", "3", "9", "13500"),
("9", "7", "1", "1550"),
("2", "6", "7", "10500"),
("10", "6", "6", "9000"),
("2", "3", "6", "9000"),
("1", "1", "6", "12000"),
("7", "6", "5", "7500"),
("7", "5", "2", "100"),
("3", "1", "8", "16000"),
("8", "4", "8", "2400"),
("2", "4", "9", "2700"),
("3", "6", "9", "13500"),
("6", "7", "7", "10850"),
("1", "5", "9", "450"),
("1", "2", "7", "7000"),
("5", "6", "2", "3000");
