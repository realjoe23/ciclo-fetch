//Hecho por Rodrigo Esaú Villegas Nuño y José Luis Chávez Gómez
//Módulo general Jericalla plus.
`timescale 1ns/1ns

module ciclo_fetch(
	input                 clk,
	input 				  rst,
	output  [31:0]     salida
);

//Definimos registros para las conexiones.
wire [31:0] r1;		//Entrada del PC
wire [31:0] r2;		//Salida del PC, entrada de "ALU" y direccion de memoria

//Definición de todas las instancias que se van a utilizar.
PC 		 instancia_PC(.entrada(r1), .clk(clk), .rst(rst), .salida(r2));
mem_out  instancia_memoria(.direccion(r2), .datoLectura(salida));
ALU      instancia_ALU(.A(r2), .R(r1));
endmodule

module ciclo_fetch_TB();

reg              clk;
reg              rst;
wire  [31:0]  salida;

ciclo_fetch inst_TB(.clk(clk), .rst(rst), .salida(salida));

//Banco de pruebas.
//El conjunto de instrucciones está distribuido de la siguiente manera:

always #25 clk=~clk;
initial
	begin
		clk=0;
		rst=1;
		#50;
		rst=0;
		$readmemb("datos_binario.txt", inst_TB.instancia_memoria.memr_out);
		#250;
		$stop;
	end
endmodule
