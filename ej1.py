import svgwrite
from svgwrite import cm, mm

dwg = svgwrite.Drawing(filename='linitas.svg', debug=True)
hlines = dwg.add(dwg.g(id='hlines', stroke='gray'))
for y in range(20):
    hlines.add(dwg.line(start=(2*cm, (2+y)*cm), end=(18*cm, (2+y)*cm)))
vlines = dwg.add(dwg.g(id='vline', stroke='black'))
for x in range(17):
    vlines.add(dwg.line(start=((2+x)*cm, 2*cm), end=((2+x)*cm, 21*cm)))
shapes = dwg.add(dwg.g(id='shapes', fill='red'))

circle = dwg.circle(center=(5*cm, 5*cm), fill='black', r='2.5cm', stroke='blue', stroke_width=3)
circle['class'] = 'class1 class2'
shapes.add(circle)

circle = dwg.circle(center=(15*cm, 5*cm), fill='black', r='2.5cm', stroke='blue', stroke_width=3)
circle['class'] = 'class1 class2'
shapes.add(circle)

circle = dwg.circle(center=(10*cm, 10*cm), fill=svgwrite.rgb(255, 153, 153,), r='5.5cm', stroke='blue', stroke_width=3)
circle['class'] = 'class1 class2'
shapes.add(circle)

circle = dwg.circle(center=(8*cm, 8*cm), fill='white', r='.85cm', stroke='black', stroke_width=3)
circle['class'] = 'class1 class2'
shapes.add(circle)

circle = dwg.circle(center=(12*cm, 8*cm), fill='white', r='.85cm', stroke='black', stroke_width=3)
circle['class'] = 'class1 class2'
shapes.add(circle)

circle = dwg.circle(center=(8*cm, 8*cm), fill='black', r='.25cm', stroke='black', stroke_width=3)
circle['class'] = 'class1 class2'
shapes.add(circle)

circle = dwg.circle(center=(12*cm, 8*cm), fill='black', r='.25cm', stroke='black', stroke_width=3)
circle['class'] = 'class1 class2'
shapes.add(circle)

mouth = dwg.circle(center=(10*cm, 12*cm), fill='red', r='2.5cm', stroke='black', stroke_width=3)
mouth['class'] = 'class1 class2'
shapes.add(mouth)

mouth = dwg.circle(center=(10*cm, 11*cm), fill=svgwrite.rgb(255, 153, 153,), r='2.5cm', stroke=svgwrite.rgb(255, 153, 153,), stroke_width=3)
mouth['class'] = 'class1 class2'
shapes.add(mouth)

dwg.save()