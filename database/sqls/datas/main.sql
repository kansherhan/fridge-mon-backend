INSERT INTO
	company_employees (
		first_name,
		last_name,
		email,
		password,
		icon_url
	)
VALUES
	(
		'Magnum',
		'Owner',
		'info@magnum.kz',
		'$2a$05$TyDi.JSW9ksHwpvPu43gsewjjdIeVMTyM7vZnBqWPWLhcWwwqtqNu',
		'user.jpg'
	);


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
		icon_url,
		city_id
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
		'1.jpg',
		34
	),
	(
		1,
		'Люмир',
		'г. Алматы, мкр. Астана, 1/10, ТЦ «Люмир»',
		43.215311,
		76.915598,
		'+7 (707) 852 45 17',
		'info@magnum.kz',
		'2.jpg',
		34
	),
	(
		1,
		'Айнабулак',
		'г. Алматы, Айнабулак 3 мкр., Жумабаева 98а',
		43.239327,
		76.870250,
		'+7 (776) 123 48 12',
		'info@magnum.kz',
		'3.jpg',
		34
	),
	(
		1,
		'Шелек',
		'Алматинская обл. Енбекшийказахский р-н с. Шелек Ул. Каипова №1В. 1 этаж, Литер А',
		43.254332,
		76.958198,
		'+7 (778) 212 21 54',
		'info@magnum.kz',
		'4.jpg',
		34
	),
	(
		1,
		'Мехзавот',
		'г. Алматы, пр. Сакена Сейфуллина, 171/Акан серы',
		43.249334,
		76.873299,
		'+7 (770) 787 58 12',
		'info@magnum.kz',
		'5.jpg',
		34
	),
	
	(
		1,
		'Кулагер',
		'г. Астана, ул. Сыганак, 4',
		51.132276,
		71.446072,
		'+7 (770) 787 58 12',
		'info@magnum.kz',
		'5.jpg',
		50
	),
	(
		1,
		'Аружан',
		'г. Астана, р-н Алматы, ул. Ілияс Жансүгірұлы, дом 8/1, литер Б, 1 этаж',
		51.123657,
		71.410343,
		'+7 (770) 787 58 43',
		'info@magnum.kz',
		'1.jpg',
		50
	),
	(
		1,
		'Рауан',
		'г. Астана, р-н Сарыарка, Биржан Сал 7',
		51.146368,
		71.377908,
		'+7 (772) 752 13 79',
		'info@magnum.kz',
		'3.jpg',
		50
	),
	(
		1,
		'Самал',
		'г. Астана, мкр. Самал, 11',
		51.122240,
		71.518176,
		'+7 (770) 787 58 12',
		'info@magnum.kz',
		'2.jpg',
		50
	),
	(
		1,
		'Женис',
		'г. Астана, р-н Сарыарка, Женіс 55',
		51.095511,
		71.417858,
		'+7 (774) 789 88 19',
		'info@magnum.kz',
		'4.jpg',
		50
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
	fridge_templates (
		company_id,
		name,
		temperature_upper,
		temperature_lower
	)
VALUES
	(1, 'meat', -15.00, 3.00),
	(1, 'flask', -2.00, 10.00),
	(1, 'milk', -2.00, 8.00),
	(1, 'cheese', -2.00, 2.00);


INSERT INTO
	fridges (
		company_id,
		enterprise_id,
		name,
		serial_number,
		temperature_upper,
		temperature_lower
	)
VALUES
	(1, 1, 'Холодильник в магазине', 'Lieb46570', 7.59, -40.75),
	(1, 2, 'Холодильник в магазине', 'Lieb5fdas6905', 4.84, -20.41),
	(1, 2, 'Холодильник в магазине', 'Lieb47fdasf891', 3.86, -28.45),
	(1, 3, 'Холодильник в магазине', 'Lieb614fdasf57', 3.40, -20.75),
	(1, 3, 'Холодильник в магазине', 'Lieb58464', 10.24, -32.79),
	(1, 3, 'Холодильник в магазине', 'Lieb6fadsf0770', 9.39, -52.19),
	(1, 4, 'Холодильник в магазине', 'Lieb61482', 2.34, -34.01),
	(1, 4, 'Холодильник в магазине', 'Lieb55666', 1.63, -29.11),
	(1, 4, 'Холодильник в магазине', 'Lieb6dsaf1762', 3.87, -28.14),
	(1, 5, 'Холодильник в магазине', 'Lieb48010', 0.16, -51.13),
	(1, 5, 'Холодильник в магазине', 'Lieb5dfsaf2239', 7.65, -17.47),
	(1, 4, 'Холодильник в магазине', 'Lieb59874', 5.80, -26.6),
	(1, 3, 'Холодильник в магазине', 'Lieb6faasfddsf0521', 10.79, -14.41),
	(1, 5, 'Холодильник в магазине', 'Lieb47214', 10.35, -48.76),
	(1, 5, 'Холодильник в магазине', 'Lieb52746', 6.76, -50.62),
	(1, 3, 'Холодильник в магазине', 'Lieb49860', 5.10, -21.59),
	(1, 4, 'Холодильник в магазине', 'Lieb46253', 7.20, -35.57),
	(1, 4, 'Холодильник в магазине', 'Lieb5fadsf2392', 8.55, -14.60),
	(1, 2, 'Холодильник в магазине', 'Lieb55716', 9.67, -24.55),
	(1, 3, 'Холодильник в магазине', 'Lieb55567', 7.95, -30.60),
	(1, 2, 'Холодильник в магазине', 'Lieb62wgrgf175', 4.58, -32.80),
	(1, 1, 'Холодильник в магазине', 'Lieb49gwf927', 5.26, -48.56),
	(1, 1, 'Холодильник в магазине', 'Lieb551whwgf42', 5.42, -52.69),
	(1, 4, 'Холодильник в магазине', 'Lieb6fdasf1953', 3.66, -36.46),
	(1, 5, 'Холодильник в магазине', 'Lieb517werg86', 6.02, -38.55),
	(1, 2, 'Холодильник в магазине', 'Lieb48sfdg716', 1.30, -17.61),
	(1, 2, 'Холодильник в магазине', 'Lieb516fadsf63', 9.48, -31.84),
	(1, 2, 'Холодильник в магазине', 'Lieb51gfds857', 3.63, -19.88),
	(1, 2, 'Холодильник в магазине', 'Lieb53rth568', 0.13, -32.27),
	(1, 3, 'Холодильник в магазине', 'Lieb562wrth54', 2.20, -49.31),
	(1, 4, 'Холодильник в магазине', 'rn', 11.52, -31.19),
	(1, 4, 'Холодильник в магазине', 'Lieb599wrehgh67', 4.17, -48.59),
	(1, 4, 'Холодильник в магазине', 'Lieb5gwergfn2666', 3.34, -17.71),
	(1, 2, 'Холодильник в магазине', 'Lieb49sfgn031', 4.75, -14.64),
	(1, 3, 'Холодильник в магазине', 'Lieb61fgn980', 11.35, -28.08),
	(1, 6, 'Холодильник в магазине', 'rwth', 7.59, -40.75),
	(1, 7, 'Холодильник в магазине', 'Lieb569045', 4.84, -20.41),
	(1, 6, 'Холодильник в магазине', 'ng', 3.86, -28.45),
	(1, 8, 'Холодильник в магазине', 'nwt', 3.40, -20.75),
	(1, 8, 'Холодильник в магазине', 'wrhb', 10.24, -32.79),
	(1, 9, 'Холодильник в магазине', 'wr', 9.39, -52.19),
	(1, 7, 'Холодильник в магазине', 'trhg', 2.34, -34.01),
	(1, 7, 'Холодильник в магазине', 'tjhr', 1.63, -29.11),
	(1, 9, 'Холодильник в магазине', 'ngfstr', 3.87, -28.14),
	(1, 10, 'Холодильник в магазине', 'trjetyj', 0.16, -51.13),
	(1, 10, 'Холодильник в магазине', 'dfsg', 7.65, -17.47),
	(1, 6, 'Холодильник в магазине', 'rt', 5.80, -26.6),
	(1, 7, 'Холодильник в магазине', 'gfdsg', 10.79, -14.41),
	(1, 6, 'Холодильник в магазине', 'erwt', 10.35, -48.76),
	(1, 8, 'Холодильник в магазине', 'dsfg', 6.76, -50.62),
	(1, 8, 'Холодильник в магазине', 'dfsb', 5.10, -21.59),
	(1, 7, 'Холодильник в магазине', 'Lieb46erg253', 7.20, -35.57),
	(1, 8, 'Холодильник в магазине', 'gfds', 8.55, -14.60),
	(1, 9, 'Холодильник в магазине', 'Liebertgfds55716', 9.67, -24.55),
	(1, 7, 'Холодильник в магазине', 'Liebgfsdg55567', 7.95, -30.60),
	(1, 9, 'Холодильник в магазине', 'weqr', 4.58, -32.80),
	(1, 6, 'Холодильник в магазине', 'gda', 5.26, -48.56),
	(1, 6, 'Холодильник в магазине', 'Lieb55gfdsg142', 5.42, -52.69),
	(1, 10, 'Холодильник в магазине', 'werq', 3.66, -36.46),
	(1, 10, 'Холодильник в магазине', 'Lieb51dfsa786', 6.02, -38.55),
	(1, 10, 'Холодильник в магазине', 'Lieb48vcxsv716', 1.30, -17.61),
	(1, 7, 'Холодильник в магазине', 'Lieb51qewr663', 9.48, -31.84),
	(1, 7, 'Холодильник в магазине', 'Lieb51gdf857', 3.63, -19.88),
	(1, 8, 'Холодильник в магазине', 'Lieb53rewqr568', 0.13, -32.27),
	(1, 9, 'Холодильник в магазине', 'Lieb56ewr254', 2.20, -49.31),
	(1, 10, 'Холодильник в магазине', 'Lieb4reqwr8068', 11.52, -31.19),
	(1, 6, 'Холодильник в магазине', 'Lieb59er967', 4.17, -48.59),
	(1, 7, 'Холодильник в магазине', 'Lieb5fdasf2666', 3.34, -17.71),
	(1, 8, 'Холодильник в магазине', 'Lieb49fadsf031', 4.75, -14.64),
	(1, 9, 'Холодильник в магазине', 'Lieb61fdasf980', 11.35, -28.08);


INSERT INTO
	fridge_measurements (
		fridge_id,
		temperature,
		humidity
	)
VALUES
	(1, 3.3, 15.2),
	(2, -11.2, -15.2),
	(3, -4.1, -15.2),
	(4, -23.1, -22.3),
	(5, -33.1, -32.2),
	(6, 10.2, 9.2),
	(7, 3.1, 10.2),
	(8, 4.5, 15.2),
	(9, 7.8, 14.2),
	(10, 8.4, 15.2),
	(11, -15.2, -10.2),
	(12, -10.2, 14.2),
	(13, 3.2, 4.3),
	(14, 1.2, 4.2),
	(15, 7.2, 10.2),
	(16, -4.1, -10.4),
	(17, -4.2, -7.6),
	(18, -10.5, -4.5),
	(19, -100, -75),
	(20, 100, 75),
	(21, 10.2, 7.5),
	(22, 4.2, 3.1),
	(23, -7.8, -10.2),
	(24, -6.3, -5.2),
	(25, 8.2, 10.1),
	(26, -10.3, -10.1),
	(27, 4.2, 3.2),
	(28, 7.8, 10.2),
	(29, 5.3, 4.2),
	(30, 7.8, 6.9),
	(31, 18.9, 15.2),
	(32, -16.3, -15.2),
	(33, 15.2, 15.1),
	(34, -32.1, -26.5),
	(35, -7.4, -9.5),

	(36, 3.3, 15.2),
	(37, -11.2, -15.2),
	(38, -4.1, -15.2),
	(39, -23.1, -22.3),
	(40, -33.1, -32.2),
	(41, 10.2, 9.2),
	(42, 3.1, 10.2),
	(43, 4.5, 15.2),
	(44, 7.8, 14.2),
	(45, 8.4, 15.2),
	(46, -15.2, -10.2),
	(47, -10.2, 14.2),
	(48, 3.2, 4.3),
	(49, 1.2, 4.2),
	(50, 7.2, 10.2),
	(51, -4.1, -10.4),
	(52, -4.2, -7.6),
	(53, -10.5, -4.5),
	(54, -100, -75),
	(55, 100, 75),
	(56, 10.2, 7.5),
	(57, 4.2, 3.1),
	(58, -7.8, -10.2),
	(59, -6.3, -5.2),
	(60, 8.2, 10.1),
	(61, -10.3, -10.1),
	(62, 4.2, 3.2),
	(63, 7.8, 10.2),
	(64, 5.3, 4.2),
	(65, 7.8, 6.9),
	(66, 18.9, 15.2),
	(67, -16.3, -15.2),
	(68, 15.2, 15.1),
	(69, -32.1, -26.5),
	(70, -7.4, -9.5);
