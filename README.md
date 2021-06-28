# Python-Calculator
A simple python calculator able to memorize and operate with scalars, vectors and matrices.

** Memorize Variables **
It performs a simple memory system storing global variables
with variables names and values.

Any input to memorize variables is in the form:
*variable_name*=*variable_value*

where:
- *variable_name* can be any string and must be before = sign
- *variable_value* can be:
  - scalar with integr or float syntax 0,1,2,...,-1,-2,...0.1,-0.1,...
    e.g. 
    x = 1
    y = 2.5
    z = 3.1416
  - vector with syntax vector=(scalar1,scalar2,scalar3,...) 
    where , delimitator is used to separate vector elements.
    e.g.
    v=(1,2,3)
    w=(1.5,2.5,3.5,0.1)
  - matrix with syntax matrix=(scalar11,scalar12,...;scalar21,scalar22;...)
    where , delimitator is used to separate matrix elements on same row
    and ; delimitator is used to separate each rows

** Operate with variables **
Enter 'calc' to be able to sum, subtract, multiply scalars, vectors and matrices
or divide scalars.

Entering 'h' will give a set of auxiliary basic features and commands.

Please report any bug at robiamado@gmail.com
