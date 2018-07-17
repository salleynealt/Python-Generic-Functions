# Returns a dictionary of Bar Chart x-postions.
# Takes Three parameters
#   pram_num_datasets => Number of datasets
#   prm_num_datapoints => Max number of datapoints to be seen
#   Optional prm_bar_width => Default set to 0.8
def fun_bar_x_values(pram_num_datasets,prm_num_datapoints,prm_bar_width = 0.8):
    rtn_dct_x_pos = {}
    x_values = []
    if pram_num_datasets >= 1 and prm_num_datapoints >= 1:
        for int_loop in range(pram_num_datasets):
            x_values = []
            for int_data_count in range(prm_num_datapoints):
                int_x_pos = round((pram_num_datasets * int_data_count) + (prm_bar_width * (int_loop + 1)),2) 
                x_values.append(int_x_pos)
            rtn_dct_x_pos[int_loop] = x_values 
    return rtn_dct_x_pos
