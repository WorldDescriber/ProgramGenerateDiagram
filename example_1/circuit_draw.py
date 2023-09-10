import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing(file='circuit_draw.svg') as d:
    d += elm.Switch().label('Switch')
    d += elm.LED().down().label('LED')
    d += elm.Line().left()
    d += elm.Battery().up().label('Battery')
