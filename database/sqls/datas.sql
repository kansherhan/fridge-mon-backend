INSERT INTO
	companies (name, inn, phone, email, icon_url)
VALUES
	(
		'Magnum',
		'75345678901',
		'+7 766 147 78 85',
		'info@magnum.kz',
		'magnum.jpg'
	);

INSERT INTO
	company_enterprises (
		company_id,
		name,
		address,
		latitude,
		longitude,
		phone,
		email,
		icon_url
	)
VALUES
	(
		1,
		'Коктем',
		'г. Алматы, ул. Тимирязева, 37 ТЦ Коктем',
		43.192287,
		76.835896,
		'+7 (778) 147 48 12',
		'info@magnum.kz',
		'1.jpg'
	),
	(
		1,
		'Люмир',
		'г. Алматы, мкр. Астана, 1/10, ТЦ «Люмир»',
		43.215311,
		76.915598,
		'+7 (707) 852 45 17',
		'info@magnum.kz',
		'2.jpg'
	),
	(
		1,
		'Айнабулак',
		'г. Алматы, Айнабулак 3 мкр., Жумабаева 98а',
		43.239327,
		76.870250,
		'+7 (776) 123 48 12',
		'info@magnum.kz',
		'3.jpg'
	),
	(
		1,
		'Шелек',
		'Алматинская обл. Енбекшийказахский р-н с. Шелек Ул. Каипова №1В. 1 этаж, Литер А',
		43.254332,
		76.958198,
		'+7 (778) 212 21 54',
		'info@magnum.kz',
		'4.jpg'
	),
	(
		1,
		'Мехзавот',
		'г. Алматы, пр. Сакена Сейфуллина, 171/Акан серы',
		43.249334,
		76.873299,
		'+7 (770) 787 58 12',
		'info@magnum.kz',
		'5.jpg'
	);

INSERT INTO
	company_employees (first_name, last_name, email, password, icon_url)
VALUES
	(
		'Magnum',
		'Owner',
		'info@magnum.kz',
		'$2a$05$TyDi.JSW9ksHwpvPu43gsewjjdIeVMTyM7vZnBqWPWLhcWwwqtqNu',
		'user.jpg'
	);

INSERT INTO
	company_employee_roles (employee_id, company_id, role)
VALUES
	(1, 1, 'owner');

INSERT INTO
	company_employee_tokens (employee_id, token)
VALUES
	(1, 'e067ae719ba19ef09741a9e6c88e93ef');

INSERT INTO
	fridge_categories (name)
VALUES
	('Холодильные шкафы'),
	('Холодильные витрины'),
	('Пристенные витрины'),
	('Боннеты'),
	('Морозильные лари'),
	('Кондитерские витрины'),
	('Настольные витрины'),
	('Холодильные столы'),
	('Холодильные камеры'),
	('Холодильные агрегаты');

INSERT INTO
	fridge_manufacturers (name)
VALUES
	('Liebherr'),
	('Bosch'),
	('Siemens'),
	('Indesit'),
	('Hotpoint'),
	('LG'),
	('Samsung'),
	('Mitsubishi'),
	('Electric'),
	('Hitachi'),
	('Sharp'),
	('Атлант'),
	('POZIS'),
	('Бирюс'),
	('Don'),
	('BEK'),
	('Vestfrost'),
	('Haier'),
	('Midea'),
	('Hisense');

INSERT INTO
	fridges (
		company_id,
		enterprise_id,
		serial_number,
		category_id,
		manufacturer_id,
		temperature_upper,
		temperature_lower
	)
VALUES
	(1, 1, 'Lieb46570', 8, 17, 7.59, -40.75),
	(1, 2, 'Lieb56905', 7, 14, 4.84, -20.41),
	(1, 2, 'Lieb47891', 3, 1, 3.86, -28.44),
	(1, 3, 'Lieb61457', 4, 15, 3.40, -20.75),
	(1, 3, 'Lieb58464', 4, 14, 10.24, -32.79),
	(1, 3, 'Lieb60770', 7, 12, 9.39, -52.19),
	(1, 4, 'Lieb61482', 2, 12, 2.34, -34.01),
	(1, 4, 'Lieb55666', 7, 11, 1.63, -29.11),
	(1, 4, 'Lieb61762', 1, 10, 3.87, -28.18),
	(1, 5, 'Lieb48010', 8, 12, 0.16, -51.13),
	(1, 5, 'Lieb52239', 3, 9, 7.65, -17.47),
	(1, 4, 'Lieb59874', 4, 18, 5.80, -26.67),
	(1, 3, 'Lieb60521', 2, 6, 10.79, -14.41),
	(1, 5, 'Lieb47214', 2, 5, 10.35, -48.76),
	(1, 5, 'Lieb52746', 2, 11, 6.76, -50.62),
	(1, 3, 'Lieb49860', 5, 4, 5.10, -21.59),
	(1, 4, 'Lieb46253', 8, 6, 7.20, -35.57),
	(1, 4, 'Lieb52392', 9, 8, 8.55, -14.60),
	(1, 2, 'Lieb55716', 4, 7, 9.67, -24.55),
	(1, 3, 'Lieb55567', 2, 15, 7.95, -30.60),
	(1, 2, 'Lieb62175', 4, 10, 4.58, -32.80),
	(1, 1, 'Lieb49927', 7, 13, 5.26, -48.56),
	(1, 1, 'Lieb55142', 2, 10, 5.42, -52.69),
	(1, 4, 'Lieb61953', 6, 11, 3.66, -36.46),
	(1, 5, 'Lieb51786', 1, 19, 6.02, -38.55),
	(1, 2, 'Lieb48716', 4, 17, 1.30, -17.61),
	(1, 2, 'Lieb51663', 5, 5, 9.48, -31.86),
	(1, 2, 'Lieb51857', 2, 11, 3.63, -19.88),
	(1, 2, 'Lieb53568', 4, 17, 0.13, -32.27),
	(1, 3, 'Lieb56254', 6, 10, 2.20, -49.31),
	(1, 4, 'Lieb48068', 7, 16, 11.52, -31.19),
	(1, 4, 'Lieb59967', 3, 1, 4.17, -48.59),
	(1, 4, 'Lieb52666', 2, 19, 3.34, -17.71),
	(1, 2, 'Lieb49031', 2, 5, 4.75, -14.64),
	(1, 3, 'Lieb61980', 10, 6, 11.35, -28.08);

INSERT INTO
	fridge_sensors (
		name,
		fridge_id,
		ip_address,
		exchange_protocol,
		start_register,
		register_count
	)
VALUES
	('sensor57626', 1, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor58396', 2, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor46781', 3, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor52133', 4, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor46802', 5, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor46850', 6, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor48270', 7, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor61373', 8, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor59809', 9, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor54491', 10, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor52116', 11, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor62040', 12, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor57277', 13, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor52418', 14, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor46105', 15, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor45946', 16, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor53281', 17, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor49360', 18, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor54983', 19, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor56505', 20, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor57006', 21, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor58281', 22, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor50991', 23, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor58063', 24, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor56415', 25, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor46418', 26, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor47308', 27, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor59281', 28, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor52213', 29, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor46271', 30, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor61622', 31, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor55397', 32, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor52394', 33, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor52865', 34, '127.0.0.1', 'modbus tcp', 1, 30),
	('sensor56425', 35, '127.0.0.1', 'modbus tcp', 1, 30);

INSERT INTO
	fridge_sensor_measurements (
		sensor_id,
		temperature,
		humidity,
		connection_status
	)
VALUES
	(1, 3.3, 15.2, 'connected'),
	(2, -11.2, -15.2, 'connected'),
	(3, -4.1, -15.2, 'connected'),
	(4, -23.1, -22.3, 'connected'),
	(5, -33.1, -32.2, 'connected'),
	(6, 10.2, 9.2, 'connected'),
	(7, 3.1, 10.2, 'connected'),
	(8, 4.5, 15.2, 'connected'),
	(9, 7.8, 14.2, 'connected'),
	(10, 8.4, 15.2, 'connected'),
	(11, -15.2, -10.2, 'connected'),
	(12, -10.2, 14.2, 'connected'),
	(13, 3.2, 4.3, 'connected'),
	(14, 1.2, 4.2, 'connected'),
	(15, 7.2, 10.2, 'connected'),
	(16, -4.1, -10.4, 'connected'),
	(17, -4.2, -7.6, 'connected'),
	(18, -10.5, -4.5, 'connected'),
	(19, -100, -75, 'connected'),
	(20, 100, 75, 'connected'),
	(21, 10.2, 7.5, 'connected'),
	(22, 4.2, 3.1, 'connected'),
	(23, -7.8, -10.2, 'connected'),
	(24, -6.3, -5.2, 'connected'),
	(25, 8.2, 10.1, 'connected'),
	(26, -10.3, -10.1, 'connected'),
	(27, 4.2, 3.2, 'connected'),
	(28, 7.8, 10.2, 'connected'),
	(29, 5.3, 4.2, 'connected'),
	(30, 7.8, 6.9, 'connected'),
	(31, 18.9, 15.2, 'connected'),
	(32, -16.3, -15.2, 'connected'),
	(33, 15.2, 15.1, 'connected'),
	(34, -32.1, -26.5, 'connected'),
	(35, -7.4, -9.5, 'connected');
