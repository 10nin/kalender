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
-- Name: group_calendar; Type: TABLE; Schema: kalendar; Owner: postgres
--

CREATE TABLE kalendar.group_calendar (
    id integer NOT NULL,
    groupid integer NOT NULL,
    zoocalendarid integer NOT NULL,
    createdon timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    createdby character varying(50) DEFAULT 'SYSTEM'::character varying NOT NULL,
    lastupdateon timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    lastupdateby character varying(50) DEFAULT 'SYSTEM'::character varying
);


ALTER TABLE kalendar.group_calendar OWNER TO postgres;

--
-- Name: group_calendar_id_seq; Type: SEQUENCE; Schema: kalendar; Owner: postgres
--

CREATE SEQUENCE kalendar.group_calendar_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE kalendar.group_calendar_id_seq OWNER TO postgres;

--
-- Name: group_calendar_id_seq; Type: SEQUENCE OWNED BY; Schema: kalendar; Owner: postgres
--

ALTER SEQUENCE kalendar.group_calendar_id_seq OWNED BY kalendar.group_calendar.id;


--
-- Name: group_master; Type: TABLE; Schema: kalendar; Owner: postgres
--

CREATE TABLE kalendar.group_master (
    id integer NOT NULL,
    groupname character varying(200) NOT NULL,
    createdon timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    createdby character varying(50) DEFAULT 'SYSTEM'::character varying NOT NULL,
    lastupdateon timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    lastupdateby character varying(50) DEFAULT 'SYSTEM'::character varying,
    groupcode character varying(10) NOT NULL,
    zooid integer NOT NULL
);


ALTER TABLE kalendar.group_master OWNER TO postgres;

--
-- Name: group_master_id_seq; Type: SEQUENCE; Schema: kalendar; Owner: postgres
--

CREATE SEQUENCE kalendar.group_master_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE kalendar.group_master_id_seq OWNER TO postgres;

--
-- Name: group_master_id_seq; Type: SEQUENCE OWNED BY; Schema: kalendar; Owner: postgres
--

ALTER SEQUENCE kalendar.group_master_id_seq OWNED BY kalendar.group_master.id;


--
-- Name: login_information_master; Type: TABLE; Schema: kalendar; Owner: postgres
--

CREATE TABLE kalendar.login_information_master (
    id integer NOT NULL,
    groupid integer NOT NULL,
    passwordhash character varying(200) NOT NULL,
    passwordsalt character varying(200),
    createdon timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    createdby character varying(50) DEFAULT 'SYSTEM'::character varying NOT NULL,
    lastupdateon timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    lastupdateby character varying(50) DEFAULT 'SYSTEM'::character varying,
    roleid integer
);


ALTER TABLE kalendar.login_information_master OWNER TO postgres;

--
-- Name: login_infromation_master_id_seq; Type: SEQUENCE; Schema: kalendar; Owner: postgres
--

CREATE SEQUENCE kalendar.login_infromation_master_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE kalendar.login_infromation_master_id_seq OWNER TO postgres;

--
-- Name: login_infromation_master_id_seq; Type: SEQUENCE OWNED BY; Schema: kalendar; Owner: postgres
--

ALTER SEQUENCE kalendar.login_infromation_master_id_seq OWNED BY kalendar.login_information_master.id;


--
-- Name: opening_closing_pattern_master; Type: TABLE; Schema: kalendar; Owner: postgres
--

CREATE TABLE kalendar.opening_closing_pattern_master (
    id integer NOT NULL,
    opening time without time zone NOT NULL,
    closing time without time zone NOT NULL,
    createdon timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    createdby character varying(50) DEFAULT 'SYSTEM'::character varying NOT NULL,
    lastupdateon timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    lastupdateby character varying(50) DEFAULT 'SYSTEM'::character varying
);


ALTER TABLE kalendar.opening_closing_pattern_master OWNER TO postgres;

--
-- Name: opening_closing_pattern_master_id_seq; Type: SEQUENCE; Schema: kalendar; Owner: postgres
--

CREATE SEQUENCE kalendar.opening_closing_pattern_master_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE kalendar.opening_closing_pattern_master_id_seq OWNER TO postgres;

--
-- Name: opening_closing_pattern_master_id_seq; Type: SEQUENCE OWNED BY; Schema: kalendar; Owner: postgres
--

ALTER SEQUENCE kalendar.opening_closing_pattern_master_id_seq OWNED BY kalendar.opening_closing_pattern_master.id;


--
-- Name: role; Type: TABLE; Schema: kalendar; Owner: postgres
--

CREATE TABLE kalendar.role (
    id integer NOT NULL,
    rolename character varying(200) NOT NULL,
    createdon timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    createdby character varying(50) DEFAULT 'SYSTEM'::character varying,
    latestupdateon timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    latestupdateby character varying(50) DEFAULT 'SYSTEM'::character varying
);


ALTER TABLE kalendar.role OWNER TO postgres;

--
-- Name: role_id_seq; Type: SEQUENCE; Schema: kalendar; Owner: postgres
--

CREATE SEQUENCE kalendar.role_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE kalendar.role_id_seq OWNER TO postgres;

--
-- Name: role_id_seq; Type: SEQUENCE OWNED BY; Schema: kalendar; Owner: postgres
--

ALTER SEQUENCE kalendar.role_id_seq OWNED BY kalendar.role.id;


--
-- Name: zoo_calendar_master; Type: TABLE; Schema: kalendar; Owner: postgres
--

CREATE TABLE kalendar.zoo_calendar_master (
    id integer NOT NULL,
    zoomasterid integer NOT NULL,
    createdon timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    createdby character varying(50) DEFAULT 'SYSTEM'::character varying NOT NULL,
    lastupdateon timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    lastupdateby character varying(50) DEFAULT 'SYSTEM'::character varying,
    openingclosingid integer,
    calendarday date NOT NULL
);


ALTER TABLE kalendar.zoo_calendar_master OWNER TO postgres;

--
-- Name: zoo_calendar_master_id_seq; Type: SEQUENCE; Schema: kalendar; Owner: postgres
--

CREATE SEQUENCE kalendar.zoo_calendar_master_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE kalendar.zoo_calendar_master_id_seq OWNER TO postgres;

--
-- Name: zoo_calendar_master_id_seq; Type: SEQUENCE OWNED BY; Schema: kalendar; Owner: postgres
--

ALTER SEQUENCE kalendar.zoo_calendar_master_id_seq OWNED BY kalendar.zoo_calendar_master.id;


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
-- Name: group_calendar id; Type: DEFAULT; Schema: kalendar; Owner: postgres
--

ALTER TABLE ONLY kalendar.group_calendar ALTER COLUMN id SET DEFAULT nextval('kalendar.group_calendar_id_seq'::regclass);


--
-- Name: group_master id; Type: DEFAULT; Schema: kalendar; Owner: postgres
--

ALTER TABLE ONLY kalendar.group_master ALTER COLUMN id SET DEFAULT nextval('kalendar.group_master_id_seq'::regclass);


--
-- Name: login_information_master id; Type: DEFAULT; Schema: kalendar; Owner: postgres
--

ALTER TABLE ONLY kalendar.login_information_master ALTER COLUMN id SET DEFAULT nextval('kalendar.login_infromation_master_id_seq'::regclass);


--
-- Name: opening_closing_pattern_master id; Type: DEFAULT; Schema: kalendar; Owner: postgres
--

ALTER TABLE ONLY kalendar.opening_closing_pattern_master ALTER COLUMN id SET DEFAULT nextval('kalendar.opening_closing_pattern_master_id_seq'::regclass);


--
-- Name: role id; Type: DEFAULT; Schema: kalendar; Owner: postgres
--

ALTER TABLE ONLY kalendar.role ALTER COLUMN id SET DEFAULT nextval('kalendar.role_id_seq'::regclass);


--
-- Name: zoo_calendar_master id; Type: DEFAULT; Schema: kalendar; Owner: postgres
--

ALTER TABLE ONLY kalendar.zoo_calendar_master ALTER COLUMN id SET DEFAULT nextval('kalendar.zoo_calendar_master_id_seq'::regclass);


--
-- Name: zoo_master id; Type: DEFAULT; Schema: kalendar; Owner: postgres
--

ALTER TABLE ONLY kalendar.zoo_master ALTER COLUMN id SET DEFAULT nextval('kalendar.zoo_master_id_seq'::regclass);


--
-- Data for Name: group_calendar; Type: TABLE DATA; Schema: kalendar; Owner: postgres
--

COPY kalendar.group_calendar (id, groupid, zoocalendarid, createdon, createdby, lastupdateon, lastupdateby) FROM stdin;
\.


--
-- Data for Name: group_master; Type: TABLE DATA; Schema: kalendar; Owner: postgres
--

COPY kalendar.group_master (id, groupname, createdon, createdby, lastupdateon, lastupdateby, groupcode, zooid) FROM stdin;
28	testgroup	2018-05-22 09:59:47.93318	SYSTEM	\N	SYSTEM	09-0000-01	1
\.


--
-- Data for Name: login_information_master; Type: TABLE DATA; Schema: kalendar; Owner: postgres
--

COPY kalendar.login_information_master (id, groupid, passwordhash, passwordsalt, createdon, createdby, lastupdateon, lastupdateby, roleid) FROM stdin;
6	28	E124FE2AD89DD1FB4B1AADEE519E53127F708E94256DFA353E5C237D5289E0A78FE1950A819DACC8E0974D4ED5E08C8E28C0DE995CD17CF9CF21451FF3761EE6	7b9e1f292db9401e8b6b140a7710ca4c	2018-05-22 09:59:47.946983	SYSTEM	\N	SYSTEM	\N
\.


--
-- Data for Name: opening_closing_pattern_master; Type: TABLE DATA; Schema: kalendar; Owner: postgres
--

COPY kalendar.opening_closing_pattern_master (id, opening, closing, createdon, createdby, lastupdateon, lastupdateby) FROM stdin;
1	10:30:00	15:00:00	2018-05-21 12:29:03.77545	SYSTEM	2018-05-21 12:29:03.77545	SYSTEM
2	17:00:00	19:30:00	2018-05-21 12:29:03.77545	SYSTEM	2018-05-21 12:29:03.77545	SYSTEM
\.


--
-- Data for Name: role; Type: TABLE DATA; Schema: kalendar; Owner: postgres
--

COPY kalendar.role (id, rolename, createdon, createdby, latestupdateon, latestupdateby) FROM stdin;
\.


--
-- Data for Name: zoo_calendar_master; Type: TABLE DATA; Schema: kalendar; Owner: postgres
--

COPY kalendar.zoo_calendar_master (id, zoomasterid, createdon, createdby, lastupdateon, lastupdateby, openingclosingid, calendarday) FROM stdin;
1	2	2018-05-20 10:52:02.441805	SYSTEM	2018-05-20 10:52:02.441805	SYSTEM	1	2018-05-20
\.


--
-- Data for Name: zoo_master; Type: TABLE DATA; Schema: kalendar; Owner: postgres
--

COPY kalendar.zoo_master (id, zooname, createdon, createdby, latestupdateon, latestupdateby) FROM stdin;
1	ZOO1	2018-05-15 11:23:01.124755	SYSTEM	2018-05-15 11:23:01.124755	SYSTEM
3	ZOO3	2018-05-15 11:23:01.124755	SYSTEM	2018-05-15 11:23:01.124755	SYSTEM
2	ZOO2	2018-05-15 11:23:01.124755	SYSTEM	2018-05-15 11:23:01.124755	SYSTEM
\.


--
-- Name: group_calendar_id_seq; Type: SEQUENCE SET; Schema: kalendar; Owner: postgres
--

SELECT pg_catalog.setval('kalendar.group_calendar_id_seq', 1, true);


--
-- Name: group_master_id_seq; Type: SEQUENCE SET; Schema: kalendar; Owner: postgres
--

SELECT pg_catalog.setval('kalendar.group_master_id_seq', 28, true);


--
-- Name: login_infromation_master_id_seq; Type: SEQUENCE SET; Schema: kalendar; Owner: postgres
--

SELECT pg_catalog.setval('kalendar.login_infromation_master_id_seq', 6, true);


--
-- Name: opening_closing_pattern_master_id_seq; Type: SEQUENCE SET; Schema: kalendar; Owner: postgres
--

SELECT pg_catalog.setval('kalendar.opening_closing_pattern_master_id_seq', 2, true);


--
-- Name: role_id_seq; Type: SEQUENCE SET; Schema: kalendar; Owner: postgres
--

SELECT pg_catalog.setval('kalendar.role_id_seq', 1, false);


--
-- Name: zoo_calendar_master_id_seq; Type: SEQUENCE SET; Schema: kalendar; Owner: postgres
--

SELECT pg_catalog.setval('kalendar.zoo_calendar_master_id_seq', 1, true);


--
-- Name: zoo_master_id_seq; Type: SEQUENCE SET; Schema: kalendar; Owner: postgres
--

SELECT pg_catalog.setval('kalendar.zoo_master_id_seq', 3, true);


--
-- Name: group_calendar group_calendar_pkey; Type: CONSTRAINT; Schema: kalendar; Owner: postgres
--

ALTER TABLE ONLY kalendar.group_calendar
    ADD CONSTRAINT group_calendar_pkey PRIMARY KEY (id);


--
-- Name: group_master group_master_pkey; Type: CONSTRAINT; Schema: kalendar; Owner: postgres
--

ALTER TABLE ONLY kalendar.group_master
    ADD CONSTRAINT group_master_pkey PRIMARY KEY (id);


--
-- Name: login_information_master login_infromation_master_pkey; Type: CONSTRAINT; Schema: kalendar; Owner: postgres
--

ALTER TABLE ONLY kalendar.login_information_master
    ADD CONSTRAINT login_infromation_master_pkey PRIMARY KEY (id);


--
-- Name: opening_closing_pattern_master opening_closing_pattern_master_pkey; Type: CONSTRAINT; Schema: kalendar; Owner: postgres
--

ALTER TABLE ONLY kalendar.opening_closing_pattern_master
    ADD CONSTRAINT opening_closing_pattern_master_pkey PRIMARY KEY (id);


--
-- Name: role role_pkey; Type: CONSTRAINT; Schema: kalendar; Owner: postgres
--

ALTER TABLE ONLY kalendar.role
    ADD CONSTRAINT role_pkey PRIMARY KEY (id);


--
-- Name: zoo_calendar_master zoo_calendar_master_pkey; Type: CONSTRAINT; Schema: kalendar; Owner: postgres
--

ALTER TABLE ONLY kalendar.zoo_calendar_master
    ADD CONSTRAINT zoo_calendar_master_pkey PRIMARY KEY (id);


--
-- Name: zoo_master zoo_master_pkey; Type: CONSTRAINT; Schema: kalendar; Owner: postgres
--

ALTER TABLE ONLY kalendar.zoo_master
    ADD CONSTRAINT zoo_master_pkey PRIMARY KEY (id);


--
-- Name: group_master_groupcode_uindex; Type: INDEX; Schema: kalendar; Owner: postgres
--

CREATE UNIQUE INDEX group_master_groupcode_uindex ON kalendar.group_master USING btree (groupcode);


--
-- Name: login_information_master_groupid_uindex; Type: INDEX; Schema: kalendar; Owner: postgres
--

CREATE UNIQUE INDEX login_information_master_groupid_uindex ON kalendar.login_information_master USING btree (groupid);


--
-- Name: opening_closing_pattern_master_id_uindex; Type: INDEX; Schema: kalendar; Owner: postgres
--

CREATE UNIQUE INDEX opening_closing_pattern_master_id_uindex ON kalendar.opening_closing_pattern_master USING btree (id);


--
-- Name: role_id_uindex; Type: INDEX; Schema: kalendar; Owner: postgres
--

CREATE UNIQUE INDEX role_id_uindex ON kalendar.role USING btree (id);


--
-- Name: zoo_master_id_uindex; Type: INDEX; Schema: kalendar; Owner: postgres
--

CREATE UNIQUE INDEX zoo_master_id_uindex ON kalendar.zoo_master USING btree (id);


--
-- Name: group_calendar group_calendar_group_master_fk; Type: FK CONSTRAINT; Schema: kalendar; Owner: postgres
--

ALTER TABLE ONLY kalendar.group_calendar
    ADD CONSTRAINT group_calendar_group_master_fk FOREIGN KEY (groupid) REFERENCES kalendar.group_master(id);


--
-- Name: group_master group_master_zoo_master_id_fk; Type: FK CONSTRAINT; Schema: kalendar; Owner: postgres
--

ALTER TABLE ONLY kalendar.group_master
    ADD CONSTRAINT group_master_zoo_master_id_fk FOREIGN KEY (zooid) REFERENCES kalendar.zoo_master(id);


--
-- Name: login_information_master login_information_master_group_master_id_fk; Type: FK CONSTRAINT; Schema: kalendar; Owner: postgres
--

ALTER TABLE ONLY kalendar.login_information_master
    ADD CONSTRAINT login_information_master_group_master_id_fk FOREIGN KEY (groupid) REFERENCES kalendar.group_master(id);


--
-- Name: login_information_master login_infromation_master_role_id_fk; Type: FK CONSTRAINT; Schema: kalendar; Owner: postgres
--

ALTER TABLE ONLY kalendar.login_information_master
    ADD CONSTRAINT login_infromation_master_role_id_fk FOREIGN KEY (roleid) REFERENCES kalendar.role(id);


--
-- Name: zoo_calendar_master zoo_calendar_master_opening_closing_pattern_master_id_fk; Type: FK CONSTRAINT; Schema: kalendar; Owner: postgres
--

ALTER TABLE ONLY kalendar.zoo_calendar_master
    ADD CONSTRAINT zoo_calendar_master_opening_closing_pattern_master_id_fk FOREIGN KEY (openingclosingid) REFERENCES kalendar.opening_closing_pattern_master(id);


--
-- Name: zoo_calendar_master zoo_calendar_master_zoo_master_fk; Type: FK CONSTRAINT; Schema: kalendar; Owner: postgres
--

ALTER TABLE ONLY kalendar.zoo_calendar_master
    ADD CONSTRAINT zoo_calendar_master_zoo_master_fk FOREIGN KEY (zoomasterid) REFERENCES kalendar.zoo_master(id);


--
-- PostgreSQL database dump complete
--

