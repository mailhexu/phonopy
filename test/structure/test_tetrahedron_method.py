import numpy as np
from phonopy.structure.tetrahedron_method import (
    get_all_tetrahedra_relative_grid_address,
    get_tetrahedra_integration_weight,
)


rel_ga_ref = [
    0,
    0,
    0,
    1,
    0,
    0,
    1,
    1,
    0,
    1,
    1,
    1,
    0,
    0,
    0,
    1,
    0,
    0,
    1,
    0,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    1,
    0,
    1,
    1,
    0,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    1,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    1,
    1,
    -1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    1,
    1,
    -1,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    1,
    0,
    1,
    0,
    -1,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    1,
    0,
    -1,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    -1,
    -1,
    0,
    0,
    -1,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    -1,
    -1,
    0,
    -1,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    1,
    1,
    0,
    0,
    0,
    -1,
    0,
    0,
    0,
    0,
    1,
    0,
    1,
    1,
    0,
    0,
    0,
    -1,
    0,
    0,
    0,
    0,
    1,
    0,
    -1,
    0,
    -1,
    0,
    0,
    -1,
    0,
    0,
    0,
    0,
    1,
    0,
    -1,
    0,
    -1,
    -1,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    -1,
    -1,
    0,
    0,
    -1,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    -1,
    -1,
    0,
    -1,
    0,
    0,
    0,
    0,
    -1,
    -1,
    -1,
    0,
    -1,
    -1,
    0,
    0,
    -1,
    0,
    0,
    0,
    -1,
    -1,
    -1,
    0,
    -1,
    -1,
    0,
    -1,
    0,
    0,
    0,
    0,
    -1,
    -1,
    -1,
    -1,
    0,
    -1,
    0,
    0,
    -1,
    0,
    0,
    0,
    -1,
    -1,
    -1,
    -1,
    0,
    -1,
    -1,
    0,
    0,
    0,
    0,
    0,
    -1,
    -1,
    -1,
    -1,
    -1,
    0,
    0,
    -1,
    0,
    0,
    0,
    0,
    -1,
    -1,
    -1,
    -1,
    -1,
    0,
    -1,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    1,
    0,
    0,
    1,
    1,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    1,
    0,
    1,
    1,
    0,
    0,
    0,
    -1,
    1,
    0,
    -1,
    1,
    1,
    -1,
    0,
    0,
    0,
    0,
    0,
    -1,
    0,
    1,
    -1,
    1,
    1,
    -1,
    0,
    0,
    0,
    0,
    0,
    -1,
    1,
    0,
    0,
    1,
    0,
    -1,
    1,
    1,
    0,
    0,
    0,
    0,
    1,
    0,
    -1,
    1,
    1,
    0,
    1,
    1,
    0,
    0,
    0,
    -1,
    0,
    1,
    0,
    0,
    1,
    -1,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    1,
    -1,
    1,
    1,
    0,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    -1,
    0,
    1,
    -1,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    1,
    1,
    -1,
    0,
    0,
    0,
    0,
    -1,
    0,
    1,
    0,
    -1,
    0,
    -1,
    0,
    0,
    0,
    0,
    0,
    -1,
    0,
    1,
    0,
    0,
    1,
    0,
    -1,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    -1,
    1,
    0,
    -1,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    1,
    0,
    1,
    0,
    -1,
    0,
    0,
    0,
    -1,
    1,
    0,
    0,
    0,
    -1,
    -1,
    0,
    0,
    0,
    0,
    0,
    -1,
    1,
    0,
    0,
    1,
    0,
    0,
    0,
    -1,
    0,
    0,
    0,
    0,
    -1,
    -1,
    1,
    -1,
    -1,
    0,
    0,
    -1,
    0,
    0,
    0,
    0,
    -1,
    -1,
    1,
    -1,
    -1,
    0,
    -1,
    0,
    0,
    0,
    0,
    1,
    -1,
    -1,
    0,
    0,
    -1,
    1,
    0,
    -1,
    0,
    0,
    0,
    1,
    0,
    0,
    1,
    -1,
    -1,
    1,
    0,
    -1,
    0,
    0,
    0,
    1,
    -1,
    -1,
    0,
    -1,
    0,
    1,
    -1,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    1,
    -1,
    -1,
    1,
    -1,
    0,
    0,
    0,
    0,
    0,
    -1,
    -1,
    0,
    0,
    -1,
    -1,
    0,
    0,
    0,
    0,
    0,
    0,
    -1,
    -1,
    0,
    -1,
    0,
    -1,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    1,
    1,
    0,
    1,
    0,
    0,
    0,
    -1,
    1,
    0,
    0,
    0,
    1,
    -1,
    0,
    0,
    0,
    0,
    0,
    -1,
    1,
    0,
    0,
    1,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    1,
    -1,
    1,
    0,
    -1,
    0,
    1,
    -1,
    0,
    0,
    0,
    0,
    0,
    -1,
    1,
    1,
    -1,
    1,
    0,
    -1,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    1,
    -1,
    1,
    1,
    -1,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    1,
    -1,
    1,
    1,
    0,
    1,
    0,
    0,
    0,
    0,
    -1,
    1,
    1,
    -1,
    1,
    0,
    0,
    1,
    0,
    0,
    0,
    1,
    -1,
    1,
    0,
    0,
    1,
    1,
    0,
    1,
    0,
    0,
    0,
    0,
    -1,
    1,
    0,
    -1,
    0,
    -1,
    0,
    0,
    0,
    0,
    0,
    0,
    -1,
    1,
    0,
    0,
    1,
    -1,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    -1,
    0,
    1,
    -1,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    1,
    0,
    0,
    1,
    -1,
    0,
    0,
    0,
    -1,
    0,
    -1,
    0,
    0,
    -1,
    -1,
    1,
    -1,
    0,
    0,
    0,
    -1,
    0,
    -1,
    -1,
    1,
    -1,
    -1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    -1,
    -1,
    1,
    -1,
    0,
    1,
    -1,
    0,
    0,
    0,
    0,
    1,
    0,
    -1,
    1,
    -1,
    0,
    1,
    -1,
    0,
    0,
    0,
    -1,
    1,
    0,
    -1,
    1,
    -1,
    -1,
    0,
    0,
    0,
    0,
    0,
    -1,
    1,
    0,
    0,
    1,
    0,
    -1,
    1,
    -1,
    0,
    0,
    0,
    0,
    0,
    -1,
    0,
    -1,
    0,
    1,
    -1,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    -1,
    1,
    -1,
    0,
    0,
    0,
    0,
    -1,
    0,
    -1,
    0,
    0,
    -1,
    0,
    -1,
    0,
    0,
    0,
    0,
    -1,
    0,
    -1,
    0,
    -1,
    0,
    -1,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    1,
    1,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    1,
    0,
    1,
    1,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    1,
    0,
    -1,
    0,
    1,
    -1,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    -1,
    0,
    1,
    0,
    0,
    1,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    -1,
    1,
    0,
    -1,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    -1,
    1,
    0,
    0,
    1,
    0,
    0,
    0,
    -1,
    -1,
    1,
    -1,
    -1,
    0,
    0,
    -1,
    0,
    0,
    0,
    0,
    -1,
    -1,
    1,
    -1,
    -1,
    0,
    -1,
    0,
    0,
    0,
    0,
    0,
    -1,
    -1,
    1,
    0,
    -1,
    1,
    0,
    -1,
    0,
    0,
    0,
    0,
    -1,
    -1,
    1,
    -1,
    0,
    1,
    -1,
    0,
    0,
    0,
    0,
    0,
    -1,
    -1,
    1,
    0,
    -1,
    1,
    0,
    0,
    1,
    0,
    0,
    0,
    -1,
    -1,
    1,
    -1,
    0,
    1,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    -1,
    1,
    0,
    -1,
    1,
    1,
    -1,
    0,
    0,
    0,
    0,
    0,
    -1,
    0,
    1,
    -1,
    1,
    1,
    -1,
    0,
    0,
    0,
    1,
    0,
    0,
    1,
    0,
    -1,
    1,
    1,
    -1,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    1,
    -1,
    1,
    1,
    -1,
    0,
    0,
    0,
    1,
    0,
    0,
    1,
    1,
    0,
    1,
    1,
    -1,
    0,
    0,
    0,
    0,
    1,
    0,
    1,
    1,
    0,
    1,
    1,
    -1,
    0,
    0,
    0,
    0,
    0,
    -1,
    0,
    1,
    -1,
    -1,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    1,
    -1,
    -1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    -1,
    1,
    0,
    -1,
    0,
    -1,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    1,
    0,
    -1,
    0,
    -1,
    0,
    0,
    0,
    0,
    0,
    0,
    -1,
    -1,
    -1,
    0,
    0,
    -1,
    0,
    0,
    0,
    0,
    0,
    0,
    -1,
    -1,
    -1,
    0,
    -1,
    0,
    0,
]


freqs = [7.75038996, 8.45225776]
tetra_freqs = [
    [8.31845176, 8.69248151, 8.78939432, 8.66179133],
    [8.31845176, 8.69248151, 8.57211855, 8.66179133],
    [8.31845176, 8.3073908, 8.78939432, 8.66179133],
    [8.31845176, 8.3073908, 8.16360975, 8.66179133],
    [8.31845176, 8.15781566, 8.57211855, 8.66179133],
    [8.31845176, 8.15781566, 8.16360975, 8.66179133],
    [8.31845176, 8.3073908, 8.16360975, 7.23665561],
    [8.31845176, 8.15781566, 8.16360975, 7.23665561],
    [8.31845176, 8.69248151, 8.57211855, 8.25247917],
    [8.31845176, 8.15781566, 8.57211855, 8.25247917],
    [8.31845176, 8.15781566, 7.40609306, 8.25247917],
    [8.31845176, 8.15781566, 7.40609306, 7.23665561],
    [8.31845176, 8.69248151, 8.78939432, 8.55165578],
    [8.31845176, 8.3073908, 8.78939432, 8.55165578],
    [8.31845176, 8.3073908, 7.56474684, 8.55165578],
    [8.31845176, 8.3073908, 7.56474684, 7.23665561],
    [8.31845176, 8.69248151, 8.60076148, 8.55165578],
    [8.31845176, 8.69248151, 8.60076148, 8.25247917],
    [8.31845176, 7.72920193, 8.60076148, 8.55165578],
    [8.31845176, 7.72920193, 8.60076148, 8.25247917],
    [8.31845176, 7.72920193, 7.56474684, 8.55165578],
    [8.31845176, 7.72920193, 7.56474684, 7.23665561],
    [8.31845176, 7.72920193, 7.40609306, 8.25247917],
    [8.31845176, 7.72920193, 7.40609306, 7.23665561],
]
iw_I_ref = [0.37259443, 1.79993056]
iw_J_ref = [0.05740597, 0.76331859]


def test_get_all_tetrahedra_relative_grid_address():
    rel_ga = get_all_tetrahedra_relative_grid_address()
    # for i, line in enumerate(rel_ga.reshape(-1, 12)):
    #     print("%03d: " % i + "".join(["%d, " % v for v in line]))
    np.testing.assert_array_equal(rel_ga.ravel(), np.array(rel_ga_ref).ravel())


def test_get_tetrahedra_integration_weight():
    iw_I = get_tetrahedra_integration_weight(freqs, tetra_freqs, function="I")
    iw_J = get_tetrahedra_integration_weight(freqs, tetra_freqs, function="J")
    np.testing.assert_allclose(iw_I_ref, iw_I, atol=1e-5)
    np.testing.assert_allclose(iw_J_ref, iw_J, atol=1e-5)


def test_get_tetrahedra_integration_weight_one_freq():
    iw_I = []
    iw_J = []
    for i in range(2):
        iw_I.append(
            get_tetrahedra_integration_weight(freqs[i], tetra_freqs, function="I")
        )
        iw_J.append(
            get_tetrahedra_integration_weight(freqs[i], tetra_freqs, function="J")
        )
    np.testing.assert_allclose(iw_I_ref, iw_I, atol=1e-5)
    np.testing.assert_allclose(iw_J_ref, iw_J, atol=1e-5)
