-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-11-2022 a las 16:26:01
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `rh3`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puesto`
--

CREATE TABLE `puesto` (
  `idPuesto` int(11) NOT NULL,
  `codPuesto` varchar(15) NOT NULL,
  `nomPuesto` varchar(50) NOT NULL,
  `reqFisicos` varchar(70) NOT NULL,
  `reqPsicologicos` varchar(70) NOT NULL,
  `responsabilidades` varchar(70) NOT NULL,
  `condicionesTrabajo` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `puesto`
--

INSERT INTO `puesto` (`idPuesto`, `codPuesto`, `nomPuesto`, `reqFisicos`, `reqPsicologicos`, `responsabilidades`, `condicionesTrabajo`) VALUES
(1, 'V009', 'SUPERVISOR DE TIENDA ', 'AGUDEZA VISUAL', 'MEMORIA A CORTO Y LARGO PLAZO', 'INVENTARIO', 'AGRADABLES'),
(3, 'v0008', 'OBRERO', 'AGUDEZA VISUAL', 'MEMORIA A CORTO Y LARGO PLAZO', 'INVENTARIO', 'AGRADABLES'),
(4, 'v010', 'PROGRAMADOR', 'NO NECESARIOS', 'NO NECESARIOS', 'NO ESPECIFICADAS', 'AGRADABLES'),
(5, 'p001', 'JEFE DE MERCADOTECNIA', 'NO NECESARIOS', 'MEMORIA A CORTO Y LARGO PLAZO', 'NO ESPECIFICADAS', 'AGRADABLES'),
(38, '8798787', 'PRODUCTOR', 'gggbfggbbgfgfb', 'gfbgfbfgbbgf', 'rrgffgrtgt', 'tgrgtrtgfggssss'),
(39, '8787856', 'hghghg', 'hgghg', 'hgggdg', 'gghnghg', 'hgghghg'),
(40, 'qqqq', '', 'qqqqq', '', 'q', ''),
(41, 'rr', 'rr', 'rr', 'rrr', 'rrr', 'ghgg'),
(42, 'rr', 'rr', 'rr', 'rrr', 'rrr', 'ghgg'),
(43, 'rr', 'rr', 'rr', 'rrr', 'rrr', 'ghgg'),
(44, 'rr', 'rr', 'rr', 'rrr', 'rrr', 'ghgg'),
(45, 'rr', 'rr', 'rr', 'rrr', 'rrr', 'ghgg'),
(50, '111111111111111', 'aaaaaaaaaaaa', 'hhh', 'x', 'x', 'xxx');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `puesto`
--
ALTER TABLE `puesto`
  ADD PRIMARY KEY (`idPuesto`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `puesto`
--
ALTER TABLE `puesto`
  MODIFY `idPuesto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
