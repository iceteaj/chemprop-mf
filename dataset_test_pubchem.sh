python multifidelity_end2end.py \
--model_type multi_fidelity \
--data_file /home/kpg/multifidelity/mf_benchmark/chemprop/tests/data/pubchem_AID1445_sd_dr_0.1.csv \
--hf_col_name DR \
--lf_col_name SD \
--scale_data True \
--save_test_plot False \
--num_epochs 3 \
--export_train_and_val False \
--add_descriptor_bias_to_make_lf 0 \
--add_pn_bias_to_make_lf 0 \
--add_constant_bias_to_make_lf 0 \
--add_gauss_noise_to_make_lf 0 \
--split_type random \
--lf_hf_size_ratio 1 \
--lf_superset_of_hf True \
--seed 0 > dataset_test_pubchem.out 2>&1