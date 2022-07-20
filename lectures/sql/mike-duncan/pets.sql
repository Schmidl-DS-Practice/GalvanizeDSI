--
-- PostgreSQL database dump
--

-- Dumped from database version 10.12 (Ubuntu 10.12-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.12 (Ubuntu 10.12-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

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
-- Name: pets; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pets (
    id integer NOT NULL,
    name character varying,
    species character varying,
    age integer,
    gender character(1),
    owner character varying
);


ALTER TABLE public.pets OWNER TO postgres;

--
-- Name: pets_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pets_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pets_id_seq OWNER TO postgres;

--
-- Name: pets_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pets_id_seq OWNED BY public.pets.id;


--
-- Name: pets id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pets ALTER COLUMN id SET DEFAULT nextval('public.pets_id_seq'::regclass);


--
-- Data for Name: pets; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pets (id, name, species, age, gender, owner) FROM stdin;
1	Max	cat	8	M	Taryn
2	Belle	cat	10	F	Taryn
3	Bailey	dog	11	F	Kyrie
4	Daisy	cat	5	F	Kyrie
5	Kahlua	dog	7	F	Blair
6	Henley	dog	9	F	Megan
7	Salem	cat	1	F	Megan
8	Teeny	cat	1	F	Megan
\.


--
-- Name: pets_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.pets_id_seq', 8, true);


--
-- PostgreSQL database dump complete
--

