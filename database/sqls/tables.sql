CREATE TYPE "sensor_connection_status" AS ENUM (
  'connected',
  'disconnected'
);

CREATE TYPE "company_roles" AS ENUM (
  'owner',
  'administrator',
  'moderator',
  'viewer'
);

CREATE TYPE "fridge_status" AS ENUM (
  'inactive',
  'active',
  'broken'
);

CREATE TABLE "companies" (
  "id" INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "name" varchar NOT NULL,
  "inn" varchar(20) NOT NULL,
  "phone" varchar(20),
  "email" varchar(50),
  "icon_url" varchar,
  "created_at" timestamp NOT NULL DEFAULT (now()),
  "updated_at" timestamp NOT NULL DEFAULT (now())
);

CREATE TABLE "company_enterprises" (
  "id" INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "name" varchar NOT NULL,
  "address" varchar NOT NULL,
  "company_id" integer NOT NULL,
  "latitude" numeric(3, 10) NOT NULL,
  "longitude" numeric(3, 10) NOT NULL,
  "phone" varchar(20),
  "email" varchar(50),
  "icon_url" varchar,
  "created_at" timestamp NOT NULL DEFAULT (now()),
  "updated_at" timestamp NOT NULL DEFAULT (now())
);

CREATE TABLE "company_employees" (
  "id" INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "first_name" varchar NOT NULL,
  "last_name" varchar NOT NULL,
  "email" varchar(50) UNIQUE NOT NULL,
  "password" varchar NOT NULL,
  "icon_url" varchar NOT NULL,
  "created_at" timestamp NOT NULL DEFAULT (now()),
  "updated_at" timestamp NOT NULL DEFAULT (now())
);

CREATE TABLE "company_employee_roles" (
  "id" INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "employee_id" integer NOT NULL,
  "company_id" integer NOT NULL,
  "enterprise_id" integer,
  "role" company_roles NOT NULL
);

CREATE TABLE "company_employee_tokens" (
  "id" INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "employee_id" integer NOT NULL,
  "token" varchar NOT NULL,
  "created_at" timestamp NOT NULL DEFAULT (now()),
  "updated_at" timestamp NOT NULL DEFAULT (now())
);

CREATE TABLE "fridges" (
  "id" INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "company_id" integer NOT NULL,
  "enterprise_id" integer NOT NULL,
  "category_id" integer NOT NULL,
  "manufacturer_id" integer NOT NULL,
  "serial_number" varchar NOT NULL,
  "temperature_upper" numeric(5, 2),
  "temperature_lower" numeric(5, 2),
  "average_temperature" numeric(5,2),
  "average_humidity" numeric(5,2),
  "status" fridge_status NOT NULL DEFAULT 'active',
  "created_at" timestamp NOT NULL DEFAULT (now()),
  "updated_at" timestamp NOT NULL DEFAULT (now())
);

CREATE TABLE "fridge_categories" (
  "id" INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "name" varchar UNIQUE NOT NULL
);

CREATE TABLE "fridge_manufacturers" (
  "id" INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "name" varchar UNIQUE NOT NULL
);

CREATE TABLE "fridge_sensors" (
  "id" INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "name" varchar NOT NULL,
  "fridge_id" integer NOT NULL,
  "ip_address" varchar(50) NOT NULL,
  "exchange_protocol" varchar(50),
  "start_register" integer,
  "register_count" integer,
  "created_at" timestamp NOT NULL DEFAULT (now()),
  "updated_at" timestamp NOT NULL DEFAULT (now())
);

CREATE TABLE "fridge_sensor_measurements" (
  "id" INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "sensor_id" integer NOT NULL,
  "temperature" numeric(5, 2),
  "humidity" numeric(5, 2),
  "connection_status" sensor_connection_status NOT NULL DEFAULT 'connected',
  "created_at" timestamp NOT NULL DEFAULT (now()),
  "updated_at" timestamp NOT NULL DEFAULT (now())
);

ALTER TABLE "company_enterprises" ADD FOREIGN KEY ("company_id") REFERENCES "companies" ("id");

ALTER TABLE "company_employee_roles" ADD FOREIGN KEY ("employee_id") REFERENCES "company_employees" ("id");

ALTER TABLE "company_employee_roles" ADD FOREIGN KEY ("company_id") REFERENCES "companies" ("id");

ALTER TABLE "company_employee_roles" ADD FOREIGN KEY ("enterprise_id") REFERENCES "company_enterprises" ("id");

ALTER TABLE "company_employee_tokens" ADD FOREIGN KEY ("employee_id") REFERENCES "company_employees" ("id");

ALTER TABLE "fridges" ADD FOREIGN KEY ("company_id") REFERENCES "companies" ("id");

ALTER TABLE "fridges" ADD FOREIGN KEY ("enterprise_id") REFERENCES "company_enterprises" ("id");

ALTER TABLE "fridges" ADD FOREIGN KEY ("category_id") REFERENCES "fridge_categories" ("id");

ALTER TABLE "fridges" ADD FOREIGN KEY ("manufacturer_id") REFERENCES "fridge_manufacturers" ("id");

ALTER TABLE "fridge_sensors" ADD FOREIGN KEY ("fridge_id") REFERENCES "fridges" ("id");

ALTER TABLE "fridge_sensor_measurements" ADD FOREIGN KEY ("sensor_id") REFERENCES "fridge_sensors" ("id");
