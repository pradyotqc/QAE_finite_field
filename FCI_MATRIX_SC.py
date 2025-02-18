# # %%
# # file_path = file_path
# file_path = "C:/Users/prita/Desktop/DIRAC_H2_FCI/QAE_finite_field/FCIDUMP_dossss"
# # /content/drive/MyDrive/Colab Notebooks/QAE_finite_field/FCIDUMP_dossss
# # Read the file and store lines
# with open(file_path, "r") as file:
#     lines = file.readlines()

# # Ignore the first 6 lines
# lines = lines[6:]

# # Process the remaining lines
# integral_dict = {}
# for line in lines:
#     parts = line.split()
#     if len(parts) == 6:  # Ensure there are exactly 5 columns
#         integral_value = float(parts[0])
#         p, q, r, s = map(int, parts[2:])
#         key = f"({p}, {q}, {r}, {s})"
#         integral_dict[key] = integral_value

# # Print the parsed data
# for key, value in integral_dict.items():
#     print(f"{key}: {value}")

# %%
def SC_0(ref_state, integral_dict):
    sum_one = 0
    for i in ref_state:
        sum_one += integral_dict[f"({i}, {i}, {0}, {0})"]
    sum_two = 0
    for i in ref_state:
        for j in ref_state:
            if i != j:
                try:
                    sum_two += (integral_dict[f"({i}, {i}, {j}, {j})"])
                    # print(f"({i}, {i}, {j}, {j})")
                except KeyError:
                    pass  # Ignore the error and continue
                
                try:
                    sum_two -= (integral_dict[f"({i}, {j}, {j}, {i})"])
                    # print(f"({i}, {j}, {j}, {i})")
                except KeyError:
                    pass  # Ignore the error and continue
    # return sum_one+(0.5*sum_two)+integral_dict["(0, 0, 0, 0)"]
    return sum_one+(0.5*sum_two)

# %%
def SC_1(state_bra, state_ket, integral_dict):
    sum_one  = 0
    sum_two = 0
    m = list(set(state_ket) - set(state_bra))
    p = list(set(state_bra) - set(state_ket))
    for i in state_bra:
        for j in state_ket:
            if i not in state_ket and j not in state_bra:
                sum_one += integral_dict[f"({i}, {j}, {0}, {0})"]
    for i in state_bra:
        try:
            sum_two += integral_dict[f"({m[0]}, {p[0]}, {i}, {i})"]
        except KeyError:
            pass
        
        try:
            sum_two += integral_dict[f"({m[0]}, {i}, {i}, {p[0]})"]
        except KeyError:
            pass
    # return sum_one+sum_two+integral_dict["(0, 0, 0, 0)"]
    return sum_one+sum_two


# %%
def SC_2(state_bra, state_ket, integral_dict):
    m = list(set(state_ket) - set(state_bra))
    p = list(set(state_bra) - set(state_ket))
    sum_two = 0
    try: 
        sum_two += integral_dict[f"({m[0]}, {p[0]}, {m[1]}, {p[1]})"]
    except KeyError:
        pass
    try:
        sum_two += -integral_dict[f"({m[0]}, {p[1]}, {m[1]}, {p[0]})"]
    except KeyError:
        pass
    # return sum_two + integral_dict["(0, 0, 0, 0)"]
    return sum_two 


# %%
def Matrix_elements(state_bra, state_ket, integral_dict):
    # Find  difference elements
    difference = list(set(state_ket) - set(state_bra))
    if len(difference) == 0:
        value = SC_0(state_bra, integral_dict)# slater condon rule for 0 difference
        return value
    elif len(difference) == 1:
        value = SC_1(state_bra, state_ket, integral_dict)# slater condon rule for 1 difference
        return value
    elif len(difference) == 2:
        value = SC_2(state_bra, state_ket, integral_dict)# slater condon rule for 2 difference
        return value
    else:
        return 0

# # %%
# import numpy as np

# state_1 = [1, 2]
# state_2 = [3, 2]
# state_3 = [3, 4] 
# state_4 = [1, 4]
# states = [state_1, state_2, state_3, state_4]
# # Create a null matrix of dimension equal to the number of states
# num_states = len(states)
# matrix_elements = np.zeros((num_states, num_states))

# # Calculate the matrix elements
# for i, state_bra in enumerate(states):
#     for j, state_ket in enumerate(states):
#         matrix_elements[i, j] = Matrix_elements(state_bra, state_ket, integral_dict)

# print(matrix_elements)
    


# # %%
# import numpy as np

# #calculate the eigenvalues and eigenvectors
# eigenvalues, eigenvectors = np.linalg.eigh(matrix_elements)
# print("Eigenvalues:")
# print(eigenvalues)

# # %%
# eigenvalues+integral_dict["(0, 0, 0, 0)"]


