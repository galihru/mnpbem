from mnpbem_particles import Sphere, sphere_volume

r = 25.0
sphere = Sphere(radius_nm=r)

print("Sphere volume from function:", sphere_volume(r), "nm^3")
print("Sphere volume from dataclass:", sphere.volume_nm3, "nm^3")
