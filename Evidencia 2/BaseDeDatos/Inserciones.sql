
-- Inserciones de la tabla empleados.
use sistema_de_gestion_kiosko;

INSERT INTO empleados(nombre_empleado, apellido_empleado, DNI, telefono, cargo, salario, ingreso, salida)
VALUES ("Mia Morena", "Hernandez", 3555596, "+54 15 2497 6788", 3, 648844, "2020-08-18 21:26:32", "2020-08-19 05:26:32"),
("Maximo", "Gomez", 3541149, "+54 9 3181 7367", 4, 320367, "2021-05-15 00:11:51", "2021-05-15 08:11:51"),
("Santino Benjamin", "Gutierrez", 3900279, "+54 9 3436 2878", 4, 991775, "2023-06-12 05:14:42", "2023-06-12 13:14:42"),
("Benjamin Ezequiel", "Ponce", 3165185, "+54 15 2252 1906", 1, 596068, "2021-03-27 16:37:41", "2021-03-28 00:37:41"),
("Sara", "Garcia", 3834451, "+54 15 2232 6698", 1, 53820, "2020-11-05 02:56:15", "2020-11-05 10:56:15"),
("Malena", "Romero", 3695201, "+54 9 3594 6626", 2, 969742, "2023-10-20 07:29:08", "2023-10-20 15:29:08"),
("Juan Bautista", "Martinez", 3684961, "+54 15 2644 2143", 1, 573607, "2021-11-11 07:19:30", "2021-11-11 15:19:30"),
("Ciro Benjamin", "Ramirez", 3891843, "+54 9 3395 2217", 2, 215626, "2023-01-22 07:59:33", "2023-01-22 15:59:33"),
("Thiago Benjamin", "Rodriguez", 3880399, "+54 9 3975 6507", 4, 35366, "2023-09-04 18:36:36", "2023-09-05 02:36:36"),
("Santino Benjamin", "Vazquez", 3657395, "+54 9 3612 2858", 1, 438308, "2021-11-21 02:39:25", "2021-11-21 10:39:25"),
("Tomàs", "Martinez", 3878599, "+54 15 2412 0672", 2, 900622, "2021-07-11 02:42:17", "2021-07-11 10:42:17"),
("Juana", "Duarte", 3212847, "+54 9 3198 5398", 4, 141961, "2020-02-25 03:54:15", "2020-02-25 11:54:15"),
("Angel Gabriel", "Carrizo", 3653076, "+54 15 2278 8322", 3, 413992, "2020-05-19 09:55:41", "2020-05-19 17:55:41"),
("Lautaro Nicolas", "Lopez", 3808054, "+54 9 3773 7769", 2, 532468, "2023-08-06 12:00:08", "2023-08-06 20:00:08"),
("Juan Ignacio", "Garcia", 3079458, "+54 9 3764 7980", 3, 968543, "2020-09-19 00:15:14", "2020-09-19 08:15:14");

INSERT INTO sucursal(direccion, nombre, telefono, email, encargado)
VALUES("Blv. 6 N° 45", "Mitre", "+54 9 3814 8500", "Mitre@gmail.com", 4),
("Diag. Santa Fe N° 110", "Belgrano", "+54 15 2154 6370", "Belgrano@gmail.com", 10),
("Boulevard Santa Cruz N° 369", "J.J. Castelli", "+54 9 3389 8284", "J.J. Castelli@gmail.com", 5),
("Av. Formosa N° 286", "San Martin", "+54 15 2161 4799", "San Martin@gmail.com", 10),
("Diagonal Merlo N° 146", "J.M. de Rosas", "+54 9 3598 3130", "J.M. de Rosas@gmail.com", 4);


INSERT INTO empleados_por_sucursal(id_sucursal, id_empleados)
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

INSERT INTO proveedores(nombre_proveedor, apellido_proveedor, telefono_proveedor, email_proveedor, direccion)
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

INSERT INTO productos(nombre_producto, tipo_producto, unidades, precio_venta, vencimiento, id_proveedores)
VALUES ('Coca-Cola', 1, 1000, 2000, "2026-09-19 08:15:14" , 2),
('Pritty', 1, 1000, 1000, "2026-01-01 09:13:14" , 3),
('Galletas Trio', 2, 1000, 1500, "2025-09-19 08:15:14" , 4),
('Malboro', 3, 1000, 300, "2027-11-19 08:15:14" , 8),
('Caramelos masticables', 5, 2000, 50, "2026-09-19 08:15:14" , 5),
('Lavandina', 4, 50, 1500, "2026-09-19 08:15:14" , 2),
('Detergente', 4, 30, 1550, "2026-09-19 08:15:14" , 2);
