--
-- PostgreSQL database dump
--

-- Dumped from database version 10.2 (Debian 10.2-1.pgdg90+1)
-- Dumped by pg_dump version 10.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: kalendar_db; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE kalendar_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.utf8' LC_CTYPE = 'en_US.utf8';


ALTER DATABASE kalendar_db OWNER TO postgres;

\connect kalendar_db

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: kalendar; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA kalendar;


ALTER SCHEMA kalendar OWNER TO postgres;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: zoo_master; Type: TABLE; Schema: kalendar; Owner: postgres
--

CREATE TABLE kalendar.zoo_master (
    id integer NOT NULL,
    zooname character varying(200) NOT NULL,
    createdon timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    createdby character varying(50) DEFAULT 'SYSTEM'::character varying NOT NULL,
    latestupdateon timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    latestupdateby character varying(50) DEFAULT 'SYSTEM'::character varying
);


ALTER TABLE kalendar.zoo_master OWNER TO postgres;

--
-- Name: zoo_master_id_seq; Type: SEQUENCE; Schema: kalendar; Owner: postgres
--

CREATE SEQUENCE kalendar.zoo_master_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE kalendar.zoo_master_id_seq OWNER TO postgres;

--
-- Name: zoo_master_id_seq; Type: SEQUENCE OWNED BY; Schema: kalendar; Owner: postgres
--

ALTER SEQUENCE kalendar.zoo_master_id_seq OWNED BY kalendar.zoo_master.id;


--
-- Name: zoo_master id; Type: DEFAULT; Schema: kalendar; Owner: postgres
--

ALTER TABLE ONLY kalendar.zoo_master ALTER COLUMN id SET DEFAULT nextval('kalendar.zoo_master_id_seq'::regclass);


--
-- Data for Name: zoo_master; Type: TABLE DATA; Schema: kalendar; Owner: postgres
--

COPY kalendar.zoo_master (id, zooname, createdon, createdby, latestupdateon, latestupdateby) FROM stdin;
\.


--
-- Name: zoo_master_id_seq; Type: SEQUENCE SET; Schema: kalendar; Owner: postgres
--

SELECT pg_catalog.setval('kalendar.zoo_master_id_seq', 1, false);


--
-- Name: zoo_master zoo_master_pkey; Type: CONSTRAINT; Schema: kalendar; Owner: postgres
--

ALTER TABLE ONLY kalendar.zoo_master
    ADD CONSTRAINT zoo_master_pkey PRIMARY KEY (id);


--
-- Name: zoo_master_id_uindex; Type: INDEX; Schema: kalendar; Owner: postgres
--

CREATE UNIQUE INDEX zoo_master_id_uindex ON kalendar.zoo_master USING btree (id);


--
-- PostgreSQL database dump complete
--

