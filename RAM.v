//Hecho por Rodrigo Esaú Villegas Nuño y Jose Luis Chávez Gómez
//Memoria de instrucciones

module mem_out(
	input  wire[31:0] direccion,
	output reg [31:0] datoLectura
);

reg [7:0]memr_out[0:999];

always@(*)
	begin
	datoLectura = {memr_out[direccion], memr_out[direccion+1], memr_out[direccion+2], memr_out[direccion+3]};
end
endmodule