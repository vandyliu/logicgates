import schemdraw
from schemdraw import logic

# https://schemdraw.readthedocs.io/en/latest/gallery/logicgate.html#s-r-latch-gates

# S AND A
d = schemdraw.Drawing(unit=.5)
d += (AND1 := logic.And())

d += (A := logic.Dot().at(AND1.in1).label('A', 'left'))
d += (S := logic.Dot().at(AND1.in2).label('S', 'left'))

# NOT S AND A ????????
d = schemdraw.Drawing(unit=.5)
d += (AND1 := logic.And())

d += (A := logic.Dot().at(AND1.in1).label('A', 'left'))
d += (S := logic.Dot().at(AND1.in2).label('S', 'left'))

d.draw()
# d.save('output.png')