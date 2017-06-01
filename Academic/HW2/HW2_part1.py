import math as m
'''
Calculate the total oxygen needed for journey to Mars as:
Volume of capsule (volume_sphere(a)) * percent of oxygen in air (0.21) * percent used a day (0.41) *300 days

'''
def volume_sphere(cap_radius):
   volume = m.pi * cap_radius ** 3 *(4/3)
   return volume
a = float(input('Radius of capsule (m) ==> '))
print(a)

oxy_needed = float((volume_sphere(a))* 0.21 * 0.41 * 300.00)
'''
Amount of oxygen held in cylinder:
volume of cylinder (volume_cylinder(b,c)) * 210
'''

def volume_cylinder(radius,height):
   volume = m.pi * (radius**2) * height
   return volume
b = float(input('Radius of oxygen reservoir (m) ==> '))
print(b)
c = float(input('Height of oxygen reservoir (m) ==> '))
print(c)

oxy_held = float(volume_cylinder(b,c) * 210)

'''
Number of oxygen tanks needed:
oxy_needed/oxy_held
'''
d = m.ceil(oxy_needed/oxy_held)

'''
outputs
'''

print()
print('Oxygen needed for the trip is {:.3f}m^3.'.format(oxy_needed))
print('Each cylinder holds ', round(oxy_held,3), 'm^3 at 3000 psi.', sep='')
print('The trip will require',d,'reservoir tanks.')
