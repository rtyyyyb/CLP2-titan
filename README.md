# CLP2-titan
an assembly language for my minecraft titan computer

titan:
titan is a mincraft computer with the final goal to being able to opt preform any other 
computer in terms of storage, graphics, memory and many other areas. the main parts ws 
of the computer includes: 
-16kilobyte prom (16386 bytes)
-16bit fixed point GPU (GCGP)
-16bit or 16bit point CPU (RLP16)
-8kilobyte RAM (8192 bytes)  
general specs are:
-16bit
-16kb rom
-0.5kb icache
-8kb ram
-32 16bit general purpose CPU registers
-32 16bit general purpose GPU registers
-16bit fixed point (8x8) GPU alu 
-96x128 plot reset refresh display 
CLP2: 
CLP2 is an assembely language that is a evolution off CLP which i dont have much documentation
on. i am working on a URCL to CLP2 compiler that i will use to compile bigger programs to 
run on titan. the compiler can compile: all core instructions, register defines and i am 
currently working on making it easier to use for any user and also working on labes for jumps
to do list:
-labels
-ease of use improvements
-assembely to barrel converter 
NOTE:
if you wish to use the compiler in its current state you will have to change the file path to 
the file path you wish to compile manualy. it will start the compile as soo as you start the 
program and will return the cpu time when finished (must be mor than 10ns)
