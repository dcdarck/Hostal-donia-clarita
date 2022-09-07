-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Sep 07, 2022 at 02:58 AM
-- Server version: 10.7.5-MariaDB
-- PHP Version: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dona_clarita`
--

-- --------------------------------------------------------

--
-- Table structure for table `ACCESORIO`
--

CREATE TABLE `ACCESORIO` (
  `id_accesorio` int(11) NOT NULL,
  `accesorio` varchar(45) NOT NULL,
  `num_habitacion_a` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `CAMA`
--

CREATE TABLE `CAMA` (
  `id_cama` int(11) NOT NULL,
  `cant_cojines` int(11) NOT NULL,
  `id_tipo_cama_c` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `CARGO`
--

CREATE TABLE `CARGO` (
  `id_cargo` int(11) NOT NULL,
  `cargo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `CLIENTE`
--

CREATE TABLE `CLIENTE` (
  `id_cliente` int(11) NOT NULL,
  `rut_empresa` varchar(45) NOT NULL,
  `nombre_empresa` varchar(100) NOT NULL,
  `razon_social` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `telefono` varchar(45) NOT NULL,
  `direccion` varchar(200) NOT NULL,
  `id_usuario_c` int(11) NOT NULL,
  `id_contrato_c` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `CONTRATO`
--

CREATE TABLE `CONTRATO` (
  `id_contrato` int(11) NOT NULL,
  `fecha_ini` date NOT NULL,
  `fecha_fin` date DEFAULT NULL,
  `cant_huesp` int(11) NOT NULL,
  `id_estado_contrato_c` int(11) NOT NULL,
  `id_tipo_contrato_c` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `EMPLEADO`
--

CREATE TABLE `EMPLEADO` (
  `id_empleado` int(11) NOT NULL,
  `rut_empleado` varchar(45) NOT NULL,
  `nombre_empleado` varchar(45) NOT NULL,
  `p_apellido` varchar(45) NOT NULL,
  `s_apellido` varchar(45) DEFAULT NULL,
  `email` varchar(45) NOT NULL,
  `fono` varchar(45) NOT NULL,
  `id_usuario_e` int(11) NOT NULL,
  `id_cargo_e` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `ESTADO_CONTRATO`
--

CREATE TABLE `ESTADO_CONTRATO` (
  `id_estado_contrato` int(11) NOT NULL,
  `estado_contrato` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `ESTADO_HAB`
--

CREATE TABLE `ESTADO_HAB` (
  `id_estado_hab` int(11) NOT NULL,
  `estado_hab` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `ESTADO_PEDIDO`
--

CREATE TABLE `ESTADO_PEDIDO` (
  `id_estado_p` int(11) NOT NULL,
  `estado_pedido` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `ESTADO_USUARIO`
--

CREATE TABLE `ESTADO_USUARIO` (
  `id_estado_user` int(11) NOT NULL,
  `estado_user` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `FACTURA`
--

CREATE TABLE `FACTURA` (
  `id_factura` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `nombre_empresa` varchar(100) NOT NULL,
  `subtotal` int(11) NOT NULL,
  `iva` int(11) NOT NULL,
  `total` int(11) NOT NULL,
  `id_cliente` int(11) NOT NULL,
  `num_orden_f` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `FAMILIA_PROD`
--

CREATE TABLE `FAMILIA_PROD` (
  `id_familia_p` int(11) NOT NULL,
  `familia_p` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `HABITACION`
--

CREATE TABLE `HABITACION` (
  `num_habitacion` int(11) NOT NULL,
  `precio` int(11) NOT NULL,
  `id_estado_hab_h` int(11) NOT NULL,
  `id_tipo_hab_h` int(11) NOT NULL,
  `id_tipo_cama_h` int(11) NOT NULL,
  `id_accesorio_h` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `HUESPED`
--

CREATE TABLE `HUESPED` (
  `id_huesped` int(11) NOT NULL,
  `rut_huesped` varchar(45) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `p_apellido` varchar(100) NOT NULL,
  `s_apellido` varchar(100) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `telefono` varchar(45) NOT NULL,
  `id_cliente_h` int(11) NOT NULL,
  `num_orden_h` int(11) NOT NULL,
  `num_habitacion_h` int(11) DEFAULT NULL,
  `id_minuta_h` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `MINUTA`
--

CREATE TABLE `MINUTA` (
  `id_minuta` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `precio` int(11) NOT NULL,
  `id_plato_m` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `ORDEN_COMPRA`
--

CREATE TABLE `ORDEN_COMPRA` (
  `num_orden` int(11) NOT NULL,
  `nombre_empresa` varchar(100) NOT NULL,
  `id_huesped` int(11) NOT NULL,
  `nombre_huesped` varchar(200) NOT NULL,
  `id_factura` int(11) NOT NULL,
  `id_cliente_o` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `ORDEN_PEDIDO`
--

CREATE TABLE `ORDEN_PEDIDO` (
  `num_pedido` int(11) NOT NULL,
  `fecha_pedido` date NOT NULL,
  `fecha_llegada` date DEFAULT NULL,
  `id_proveedor_o` int(11) NOT NULL,
  `id_estado_p_o` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `PLATO`
--

CREATE TABLE `PLATO` (
  `id_plato` int(11) NOT NULL,
  `nombre_plato` varchar(45) NOT NULL,
  `id_minuta_p` int(11) NOT NULL,
  `id_tipo_plato_p` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `PRODUCTO`
--

CREATE TABLE `PRODUCTO` (
  `id_producto` int(11) NOT NULL,
  `fecha_venc` int(11) NOT NULL,
  `descripcion` varchar(200) NOT NULL,
  `precio` int(11) NOT NULL,
  `stock` int(11) NOT NULL,
  `stock_critico` int(11) NOT NULL,
  `id_sku_p` int(11) NOT NULL,
  `id_plato_p` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `PROVEEDOR`
--

CREATE TABLE `PROVEEDOR` (
  `id_proveedor` int(11) NOT NULL,
  `nombre_prov` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `telefono` varchar(45) NOT NULL,
  `direccion` varchar(200) NOT NULL,
  `rubro` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `SERVICIO`
--

CREATE TABLE `SERVICIO` (
  `id_servicio` int(11) NOT NULL,
  `servicio` varchar(100) NOT NULL,
  `id_factura_s` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `SKU_PRODUCTO`
--

CREATE TABLE `SKU_PRODUCTO` (
  `id_sku` int(11) NOT NULL,
  `SKU` int(11) NOT NULL,
  `fecha_venc` int(11) NOT NULL,
  `id_proveedor_s` int(11) NOT NULL,
  `id_familia_s` int(11) NOT NULL,
  `id_tipo_producto_s` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `TIPO_CAMA`
--

CREATE TABLE `TIPO_CAMA` (
  `id_tipo_cama` int(11) NOT NULL,
  `tipo_cama` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `TIPO_CONTRATO`
--

CREATE TABLE `TIPO_CONTRATO` (
  `id_tipo_contrato` int(11) NOT NULL,
  `tipo_contrato` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `TIPO_HAB`
--

CREATE TABLE `TIPO_HAB` (
  `id_tipo_hab` int(11) NOT NULL,
  `tipo_hab` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `TIPO_PLATO`
--

CREATE TABLE `TIPO_PLATO` (
  `id_tipo_plato` int(11) NOT NULL,
  `tipo_plato` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `TIPO_PROD`
--

CREATE TABLE `TIPO_PROD` (
  `id_tipo_prod` int(11) NOT NULL,
  `tipo_prod` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `USUARIO`
--

CREATE TABLE `USUARIO` (
  `id_usuario` int(11) NOT NULL,
  `nombre_usuario` varchar(45) NOT NULL,
  `tipo_usuario` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `pwd` varchar(45) NOT NULL,
  `id_estado_u` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ACCESORIO`
--
ALTER TABLE `ACCESORIO`
  ADD PRIMARY KEY (`id_accesorio`),
  ADD KEY `num_habitacion_a_idx` (`num_habitacion_a`);

--
-- Indexes for table `CAMA`
--
ALTER TABLE `CAMA`
  ADD PRIMARY KEY (`id_cama`,`id_tipo_cama_c`),
  ADD KEY `id_tipo_cama_idx` (`id_tipo_cama_c`);

--
-- Indexes for table `CARGO`
--
ALTER TABLE `CARGO`
  ADD PRIMARY KEY (`id_cargo`);

--
-- Indexes for table `CLIENTE`
--
ALTER TABLE `CLIENTE`
  ADD PRIMARY KEY (`id_cliente`,`id_usuario_c`),
  ADD KEY `id_usuario_idx` (`id_usuario_c`),
  ADD KEY `id_contrato_c_idx` (`id_contrato_c`);

--
-- Indexes for table `CONTRATO`
--
ALTER TABLE `CONTRATO`
  ADD PRIMARY KEY (`id_contrato`,`id_estado_contrato_c`,`id_tipo_contrato_c`),
  ADD KEY `id_tipo_cotrato_idx` (`id_tipo_contrato_c`),
  ADD KEY `id_estado_contrato_idx` (`id_estado_contrato_c`);

--
-- Indexes for table `EMPLEADO`
--
ALTER TABLE `EMPLEADO`
  ADD PRIMARY KEY (`id_empleado`,`id_usuario_e`,`id_cargo_e`),
  ADD KEY `id_usuario_idx` (`id_usuario_e`),
  ADD KEY `id_cargo_idx` (`id_cargo_e`);

--
-- Indexes for table `ESTADO_CONTRATO`
--
ALTER TABLE `ESTADO_CONTRATO`
  ADD PRIMARY KEY (`id_estado_contrato`);

--
-- Indexes for table `ESTADO_HAB`
--
ALTER TABLE `ESTADO_HAB`
  ADD PRIMARY KEY (`id_estado_hab`);

--
-- Indexes for table `ESTADO_PEDIDO`
--
ALTER TABLE `ESTADO_PEDIDO`
  ADD PRIMARY KEY (`id_estado_p`);

--
-- Indexes for table `ESTADO_USUARIO`
--
ALTER TABLE `ESTADO_USUARIO`
  ADD PRIMARY KEY (`id_estado_user`);

--
-- Indexes for table `FACTURA`
--
ALTER TABLE `FACTURA`
  ADD PRIMARY KEY (`id_factura`,`num_orden_f`),
  ADD KEY `num_orden_idx` (`num_orden_f`);

--
-- Indexes for table `FAMILIA_PROD`
--
ALTER TABLE `FAMILIA_PROD`
  ADD PRIMARY KEY (`id_familia_p`);

--
-- Indexes for table `HABITACION`
--
ALTER TABLE `HABITACION`
  ADD PRIMARY KEY (`num_habitacion`,`id_estado_hab_h`,`id_tipo_hab_h`,`id_tipo_cama_h`),
  ADD KEY `id_estado_hab_idx` (`id_estado_hab_h`),
  ADD KEY `id_tipo_cama_idx` (`id_tipo_cama_h`),
  ADD KEY `id_tipo_hab_idx` (`id_tipo_hab_h`),
  ADD KEY `id_accesorio_h_idx` (`id_accesorio_h`);

--
-- Indexes for table `HUESPED`
--
ALTER TABLE `HUESPED`
  ADD PRIMARY KEY (`id_huesped`,`num_orden_h`),
  ADD KEY `num_orden_idx` (`num_orden_h`),
  ADD KEY `id_minuta_idx` (`id_minuta_h`),
  ADD KEY `num_habitacion_idx` (`num_habitacion_h`);

--
-- Indexes for table `MINUTA`
--
ALTER TABLE `MINUTA`
  ADD PRIMARY KEY (`id_minuta`,`id_plato_m`),
  ADD KEY `id_plato_idx` (`id_plato_m`);

--
-- Indexes for table `ORDEN_COMPRA`
--
ALTER TABLE `ORDEN_COMPRA`
  ADD PRIMARY KEY (`num_orden`,`id_cliente_o`),
  ADD KEY `id_cliente_idx` (`id_cliente_o`);

--
-- Indexes for table `ORDEN_PEDIDO`
--
ALTER TABLE `ORDEN_PEDIDO`
  ADD PRIMARY KEY (`num_pedido`,`id_proveedor_o`,`id_estado_p_o`),
  ADD KEY `id_proveedor_idx` (`id_proveedor_o`),
  ADD KEY `id_estado_p_idx` (`id_estado_p_o`);

--
-- Indexes for table `PLATO`
--
ALTER TABLE `PLATO`
  ADD PRIMARY KEY (`id_plato`,`id_minuta_p`,`id_tipo_plato_p`),
  ADD KEY `id_minuta_idx` (`id_minuta_p`),
  ADD KEY `id_tipo_plato_idx` (`id_tipo_plato_p`);

--
-- Indexes for table `PRODUCTO`
--
ALTER TABLE `PRODUCTO`
  ADD PRIMARY KEY (`id_producto`,`id_sku_p`,`id_plato_p`),
  ADD KEY `id_sku_idx` (`id_sku_p`),
  ADD KEY `id_plato_p_idx` (`id_plato_p`);

--
-- Indexes for table `PROVEEDOR`
--
ALTER TABLE `PROVEEDOR`
  ADD PRIMARY KEY (`id_proveedor`);

--
-- Indexes for table `SERVICIO`
--
ALTER TABLE `SERVICIO`
  ADD PRIMARY KEY (`id_servicio`,`id_factura_s`),
  ADD KEY `id_factura_idx` (`id_factura_s`);

--
-- Indexes for table `SKU_PRODUCTO`
--
ALTER TABLE `SKU_PRODUCTO`
  ADD PRIMARY KEY (`id_sku`,`id_proveedor_s`,`id_familia_s`,`id_tipo_producto_s`),
  ADD KEY `id_proveedor_idx` (`id_proveedor_s`),
  ADD KEY `id_familia_p_idx` (`id_familia_s`),
  ADD KEY `id_tipo_prod_idx` (`id_tipo_producto_s`);

--
-- Indexes for table `TIPO_CAMA`
--
ALTER TABLE `TIPO_CAMA`
  ADD PRIMARY KEY (`id_tipo_cama`);

--
-- Indexes for table `TIPO_CONTRATO`
--
ALTER TABLE `TIPO_CONTRATO`
  ADD PRIMARY KEY (`id_tipo_contrato`);

--
-- Indexes for table `TIPO_HAB`
--
ALTER TABLE `TIPO_HAB`
  ADD PRIMARY KEY (`id_tipo_hab`);

--
-- Indexes for table `TIPO_PLATO`
--
ALTER TABLE `TIPO_PLATO`
  ADD PRIMARY KEY (`id_tipo_plato`);

--
-- Indexes for table `TIPO_PROD`
--
ALTER TABLE `TIPO_PROD`
  ADD PRIMARY KEY (`id_tipo_prod`);

--
-- Indexes for table `USUARIO`
--
ALTER TABLE `USUARIO`
  ADD PRIMARY KEY (`id_usuario`,`id_estado_u`),
  ADD KEY `id_estado_idx` (`id_estado_u`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `CLIENTE`
--
ALTER TABLE `CLIENTE`
  MODIFY `id_cliente` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `CONTRATO`
--
ALTER TABLE `CONTRATO`
  MODIFY `id_contrato` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `EMPLEADO`
--
ALTER TABLE `EMPLEADO`
  MODIFY `id_empleado` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `FACTURA`
--
ALTER TABLE `FACTURA`
  MODIFY `id_factura` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `HABITACION`
--
ALTER TABLE `HABITACION`
  MODIFY `num_habitacion` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `HUESPED`
--
ALTER TABLE `HUESPED`
  MODIFY `id_huesped` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `MINUTA`
--
ALTER TABLE `MINUTA`
  MODIFY `id_minuta` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `ORDEN_COMPRA`
--
ALTER TABLE `ORDEN_COMPRA`
  MODIFY `num_orden` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `ORDEN_PEDIDO`
--
ALTER TABLE `ORDEN_PEDIDO`
  MODIFY `num_pedido` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `PLATO`
--
ALTER TABLE `PLATO`
  MODIFY `id_plato` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `PRODUCTO`
--
ALTER TABLE `PRODUCTO`
  MODIFY `id_producto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `PROVEEDOR`
--
ALTER TABLE `PROVEEDOR`
  MODIFY `id_proveedor` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SKU_PRODUCTO`
--
ALTER TABLE `SKU_PRODUCTO`
  MODIFY `id_sku` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `USUARIO`
--
ALTER TABLE `USUARIO`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `ACCESORIO`
--
ALTER TABLE `ACCESORIO`
  ADD CONSTRAINT `num_habitacion_a` FOREIGN KEY (`num_habitacion_a`) REFERENCES `HABITACION` (`num_habitacion`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `CAMA`
--
ALTER TABLE `CAMA`
  ADD CONSTRAINT `id_tipo_cama_c` FOREIGN KEY (`id_tipo_cama_c`) REFERENCES `TIPO_CAMA` (`id_tipo_cama`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `CLIENTE`
--
ALTER TABLE `CLIENTE`
  ADD CONSTRAINT `id_contrato_c` FOREIGN KEY (`id_contrato_c`) REFERENCES `CONTRATO` (`id_contrato`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `id_usuario_c` FOREIGN KEY (`id_usuario_c`) REFERENCES `USUARIO` (`id_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `CONTRATO`
--
ALTER TABLE `CONTRATO`
  ADD CONSTRAINT `id_estado_contrato_c` FOREIGN KEY (`id_estado_contrato_c`) REFERENCES `ESTADO_CONTRATO` (`id_estado_contrato`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `id_tipo_cotrato_c` FOREIGN KEY (`id_tipo_contrato_c`) REFERENCES `TIPO_CONTRATO` (`id_tipo_contrato`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `EMPLEADO`
--
ALTER TABLE `EMPLEADO`
  ADD CONSTRAINT `id_cargo_e` FOREIGN KEY (`id_cargo_e`) REFERENCES `CARGO` (`id_cargo`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `id_usuario_e` FOREIGN KEY (`id_usuario_e`) REFERENCES `USUARIO` (`id_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `FACTURA`
--
ALTER TABLE `FACTURA`
  ADD CONSTRAINT `num_orden_f` FOREIGN KEY (`num_orden_f`) REFERENCES `ORDEN_COMPRA` (`num_orden`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `HABITACION`
--
ALTER TABLE `HABITACION`
  ADD CONSTRAINT `id_accesorio_h` FOREIGN KEY (`id_accesorio_h`) REFERENCES `ACCESORIO` (`id_accesorio`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `id_estado_hab_h` FOREIGN KEY (`id_estado_hab_h`) REFERENCES `ESTADO_HAB` (`id_estado_hab`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `id_tipo_cama_h` FOREIGN KEY (`id_tipo_cama_h`) REFERENCES `TIPO_CAMA` (`id_tipo_cama`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `id_tipo_hab_h` FOREIGN KEY (`id_tipo_hab_h`) REFERENCES `TIPO_HAB` (`id_tipo_hab`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `HUESPED`
--
ALTER TABLE `HUESPED`
  ADD CONSTRAINT `id_minuta_h` FOREIGN KEY (`id_minuta_h`) REFERENCES `MINUTA` (`id_minuta`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `num_habitacion_h` FOREIGN KEY (`num_habitacion_h`) REFERENCES `HABITACION` (`num_habitacion`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `num_orden_h` FOREIGN KEY (`num_orden_h`) REFERENCES `ORDEN_COMPRA` (`num_orden`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `MINUTA`
--
ALTER TABLE `MINUTA`
  ADD CONSTRAINT `id_plato_m` FOREIGN KEY (`id_plato_m`) REFERENCES `PLATO` (`id_plato`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `ORDEN_COMPRA`
--
ALTER TABLE `ORDEN_COMPRA`
  ADD CONSTRAINT `id_cliente_o` FOREIGN KEY (`id_cliente_o`) REFERENCES `CLIENTE` (`id_cliente`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `ORDEN_PEDIDO`
--
ALTER TABLE `ORDEN_PEDIDO`
  ADD CONSTRAINT `id_estado_p_o` FOREIGN KEY (`id_estado_p_o`) REFERENCES `ESTADO_PEDIDO` (`id_estado_p`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `id_proveedor_o` FOREIGN KEY (`id_proveedor_o`) REFERENCES `PROVEEDOR` (`id_proveedor`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `PLATO`
--
ALTER TABLE `PLATO`
  ADD CONSTRAINT `id_minuta_p` FOREIGN KEY (`id_minuta_p`) REFERENCES `MINUTA` (`id_minuta`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `id_tipo_plato_p` FOREIGN KEY (`id_tipo_plato_p`) REFERENCES `TIPO_PLATO` (`id_tipo_plato`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `PRODUCTO`
--
ALTER TABLE `PRODUCTO`
  ADD CONSTRAINT `id_plato_p` FOREIGN KEY (`id_plato_p`) REFERENCES `PLATO` (`id_plato`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `id_sku_p` FOREIGN KEY (`id_sku_p`) REFERENCES `SKU_PRODUCTO` (`id_sku`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `SERVICIO`
--
ALTER TABLE `SERVICIO`
  ADD CONSTRAINT `id_factura_s` FOREIGN KEY (`id_factura_s`) REFERENCES `FACTURA` (`id_factura`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `SKU_PRODUCTO`
--
ALTER TABLE `SKU_PRODUCTO`
  ADD CONSTRAINT `id_familia_p_s` FOREIGN KEY (`id_familia_s`) REFERENCES `FAMILIA_PROD` (`id_familia_p`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `id_proveedor_s` FOREIGN KEY (`id_proveedor_s`) REFERENCES `ORDEN_PEDIDO` (`id_proveedor_o`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `id_tipo_prod_s` FOREIGN KEY (`id_tipo_producto_s`) REFERENCES `TIPO_PROD` (`id_tipo_prod`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `USUARIO`
--
ALTER TABLE `USUARIO`
  ADD CONSTRAINT `id_estado_u` FOREIGN KEY (`id_estado_u`) REFERENCES `ESTADO_USUARIO` (`id_estado_user`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
