command_str_list = []
i = 0

for model_type in [
    # "single_fidelity",  # 000 single_fidelity 0 0 0 0 random 1 True
    "multi_target",
    "multi_fidelity",
    "multi_fidelity_weight_sharing",
]:
    for descriptor_bias in [0, 10, 50]:
        # for polynomial_bias in [0, 2, 3]:
        # for polynomial_bias in [1]:
        # for polynomial_bias in [0, 1, 2, 3]:
        for polynomial_bias in [0]:
            for constant_bias in [0, 10, 50]:
                for gauss_noise in [0, 10, 50]:
                    for split_type in [
                        "random",
                        # "scaffold",
                        # "h298",
                        # "molwt",
                        # "atom",
                    ]:
                        # for lf_hf_size_ratio in [1, 10]:
                        # for lf_hf_size_ratio in [1, 10, 100]:
                        for lf_hf_size_ratio in [100]:
                            for lf_superset_of_hf in [
                                True,
                                # False,
                            ]:
                                command_str = f"{i:03} {model_type} {descriptor_bias} {polynomial_bias} {constant_bias} {gauss_noise} {split_type} {lf_hf_size_ratio} {lf_superset_of_hf}"
                                command_str_list.append(command_str)
                                i += 1

# with open("inputs.txt", "w") as f:
# with open("inputs2.txt", "w") as f:
# with open("inputs3.txt", "w") as f:
with open("inputs4.txt", "w") as f:
    for i, command_str in enumerate(command_str_list):
        if i == 0:
            f.write(command_str)
        else:
            f.write("\n" + command_str)
