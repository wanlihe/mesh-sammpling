

def main():
    l = 20
    h = 1

    nx = 80
    ny = 4

    dx = l / nx
    dy = h / ny

    n = nx * ny
    nc = ny + 1 + 1
    nf = ny

    force = -0.03 / nf

    with open('mesh.txt', 'w') as f:
        f.write('No._material_props:    4\n'
                '\tShear_modulus:   10.\n'
                '\tPoissons_ratio:  0.3\n'
                '\tMass_density:    1.0\n'
                '\tPlane_strain:    1\n'
                'No._coords_per_node:   2\n'
                'No._DOF_per_node:      2\n'
                'No._nodes:\t' + str((nx + 1) * (ny + 1)) + '\n'
                'Nodal_coords:\n')

        for j in range(ny + 1):
            for i in range(nx + 1):
                f.write('\t' + str(dx*i) + '\t' + str(dy*j) + '\n')

        f.write('No._elements:\t' + str(n) + '\n'
                'Max_no._nodes_on_any_one_element:   4\n'
                'element_identifier; no._nodes_on_element; connectivity:\n')

        for j in range(ny):
            for i in range(nx):
                c1 = int((nx + 1) * j + i + 1)
                c2 = int((nx + 1) * j + i + 2)
                c3 = int((nx + 1) * (j + 1) + i + 2)
                c4 = int((nx + 1) * (j + 1) + i + 1)
                f.write('\t1\t4\t'
                        + str(c1) + '\t'
                        + str(c2) + '\t'
                        + str(c3) + '\t'
                        + str(c4) + '\n')

        f.write('No._nodes_with_prescribed_DOFs:\t' + str(nc) + '\n'
                'Node_#, DOF#, Value:\n')

        for j in range(nc - 1):
            nn = int((nx + 1) * j + 1)
            f.write('\t' + str(nn) + '\t1\t0.0\n')
            if j == 0:
                f.write('\t' + str(nn) + '\t2\t0.0\n')

        f.write('No._elements_with_prescribed_loads:\t' + str(nf) + '\n'
                'Element_#, Face_#, Traction_components,\n')

        for j in range(nf):
            e = int(nx * (j + 1))
            f.write('\t' + str(e) + '\t2\t0.0\t' + str(force) + '\n')


if __name__ == '__main__':
    main()