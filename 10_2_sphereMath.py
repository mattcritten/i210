from math import pow, pi
import my_mod_math as mmm

sphereRadius = float(input("Enter the radius of the sphere: "))
sphereCircumference = 2 * pi * sphereRadius
sphereArea = 4 * pi * pow(sphereRadius, 2)
sphereVolume = mmm.volume_of_sphere(sphereRadius)

print(f"The circumference of the sphere is {sphereCircumference:.2f}")
print(f"The area of the sphere is {sphereArea:.2f}")
print(f"The volume of the sphere is {sphereVolume:.2f}")
