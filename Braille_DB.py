import numpy as np
class Braille:
    B_A = np.matrix([[1,0],
                     [0,0],
                     [0,0]])
    B_B = np.matrix([[1,0],
                     [1,0],
                     [0,0]])
    B_C = np.matrix([[1, 1],
                     [0, 0],
                     [0, 0]])
    B_D = np.matrix([[1, 1],
                     [0, 1],
                     [0, 0]])
    B_E = np.matrix([[1, 0],
                     [0, 1],
                     [0, 0]])
    B_F = np.matrix([[1, 1],
                     [1, 0],
                     [0, 0]])
    B_G = np.matrix([[1, 1],
                     [1, 1],
                     [0, 0]])
    B_H = np.matrix([[1, 0],
                     [1, 1],
                     [0, 0]])
    B_I = np.matrix([[0, 1],
                     [1, 0],
                     [0, 0]])
    B_J = np.matrix([[0, 1],
                     [1, 1],
                     [0, 0]])

    B_K = np.matrix([[1, 0],
                     [0, 0],
                     [1, 0]])
    B_L = np.matrix([[1, 0],
                     [1, 0],
                     [1, 0]])
    B_M = np.matrix([[1, 1],
                     [0, 0],
                     [1, 0]])
    B_N = np.matrix([[1, 1],
                     [0, 1],
                     [1, 0]])
    B_O = np.matrix([[1, 0],
                     [0, 1],
                     [1, 0]])
    B_P = np.matrix([[1, 1],
                     [1, 0],
                     [1, 0]])
    B_Q = np.matrix([[1, 1],
                     [1, 1],
                     [1, 0]])
    B_R = np.matrix([[1, 0],
                     [1, 1],
                     [1, 0]])
    B_S = np.matrix([[0, 1],
                     [1, 0],
                     [1, 0]])
    B_T = np.matrix([[0, 1],
                     [1, 1],
                     [1, 0]])

    B_U = np.matrix([[1, 0],
                     [0, 0],
                     [1, 1]])
    B_V = np.matrix([[1, 0],
                     [1, 0],
                     [1, 1]])
    B_W = np.matrix([[0, 1],
                     [0, 1],
                     [1, 1]])
    B_X = np.matrix([[1, 1],
                     [0, 0],
                     [1, 1]])
    B_Y = np.matrix([[1, 1],
                     [0, 1],
                     [1, 1]])
    B_Z = np.matrix([[1, 0],
                     [0, 1],
                     [1, 1]])

letterb = {
    1: Braille.B_A,
    2: Braille.B_B,
    3: Braille.B_C,
    4: Braille.B_D,
    5: Braille.B_E,
    6: Braille.B_F,
    7: Braille.B_G,
    8: Braille.B_H,
    9: Braille.B_I,
    10: Braille.B_J,
    11: Braille.B_K,
    12: Braille.B_L,
    13: Braille.B_M,
    14: Braille.B_N,
    15: Braille.B_O,
    16: Braille.B_P,
    17: Braille.B_Q,
    18: Braille.B_R,
    19: Braille.B_S,
    20: Braille.B_T,
    21: Braille.B_U,
    22: Braille.B_V,
    23: Braille.B_W,
    24: Braille.B_X,
    25: Braille.B_Y,
    26: Braille.B_Z
}
letter={
    1:"a",
    2:"b",
    3:"c",
    4:"d",
    5:"e",
    6:"f",
    7:"g",
    8:"h",
    9:"i",
    10:"j",
    11:"k",
    12:"l",
    13:"m",
    14:"n",
    15:"o",
    16:"p",
    17:"q",
    18:"r",
    19:"s",
    20:"t",
    21:"u",
    22:"v",
    23:"w",
    24:"x",
    25:"y",
    26:"z"
}