//Hecho por Rodrigo Esaú Villegas Nuño y José Luis Chávez Gómez
//Unidad de operaciones

module ALU(
    input wire [31:0] A,
    output reg [31:0] R
);

always@(*) 
	begin
		R = A + 4;     //Aumenta a PC 4 unidades
	end
endmodule
