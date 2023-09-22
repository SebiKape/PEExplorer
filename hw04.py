import designTool as dt
import matplotlib.pyplot as plt
import numpy as np
import pprint

# Load the standard airplane
# airplane = dt.standard_airplane('fokker100')
# 3 x 3 Cross-section configuration airplane
airplane_3_3 = {'AR_h': 5.380,
 'AR_v': 1.730,
 'AR_w': 12.17,
 'Cht': 1.219,
 'Cvt': 0.111,
 'D_f': 4.07, #prestocabin,
 'D_n': 1.5,
 'L_f': 53.47, #prestocabin,
 'L_n': 5.725,
 'Lb_v': 0.7,
 'Lc_h': 5.75,
 'MLW_frac': 0.9228915662650602,
 'Mach_altcruise': 0.4,
 'Mach_cruise': 0.80,
 'S_w': 139.566,
 'W_crew': 6860,
 'W_payload': 226292.5571,
 'altitude_altcruise': 4572,
 'altitude_cruise': 10004.32,
 'altitude_landing': 0.0,
 'altitude_takeoff': 0.0,
 'b_ail_b_wing': 0.34,
 'b_flap_b_wing': 0.6,
 'b_slat_b_wing': 0.0,
 'block_range': 740800.0,
 'block_time': 8399.999999999998,
 'c_ail_c_wing': 0.27,
 'c_flap_c_wing': 0.3,
 'c_slat_c_wing': 0.0,
 'c_tank_c_w': 0.4,
 'clmax_w': 1.8,
 'dihedral_h': 0.13369222070276564,
 'dihedral_w': 0.09634217471008,
 'distance_landing': 1800.0,
 'distance_takeoff': 1800.0,
 'engine': {'BPR': 12.04,
            'Cbase': None,
            'model': 'Howe turbofan'},
 'eta_h': 1.0,
 'flap_type': 'double slotted',
 'h_ground': 10.668000000000001,
 'k_exc_drag': 0.03,
 'loiter_time': 2700,
 'n_captains': 1,
 'n_copilots': 1,
 'n_engines': 2,
 'n_engines_under_wing': 2,
 'range_altcruise': 370400.0,
 'range_cruise': 7000000,
 'rho_f': 804,
 'slat_type': None,
 'sweep_h': 0.50614548307835557,
 'sweep_v': 0.64228116473391328,
 'sweep_w': 0.44156830075456538,
 'taper_h': 0.296,
 'taper_v': 0.310,
 'taper_w': 0.258,
 'tcr_h': 0.1,
 'tcr_v': 0.1,
 'tcr_w': 0.123,
 'tct_h': 0.1,
 'tct_v': 0.1,
 'tct_w': 0.096,
 'type': 'transport',
 'x_mlg': 23.2,
 'x_n': 23.2,
 'x_nlg': 10,
 'x_tailstrike': 43,
 'x_tank_c_w': 0.2,
 'xcg_crew': 2.5,
 'xcg_payload': 14.4,
 'xr_w': 20,
 'y_mlg': 2.47,
 'y_n': 7,
 'z_lg': -2.0,
 'z_n': -2.0,
 'z_tailstrike': -0.84,
 'zr_h': 0,
 'zr_v': 0.0,
 'zr_w': -1.5}

# 2 x 3 x 2 Cross-section configuration airplane
airplane_2_3_2 = {'AR_h': 5.380,
 'AR_v': 1.730,
 'AR_w': 10.17,
 'Cht': 1.219,
 'Cvt': 0.111,
 'D_f': 5.05, #prestocabin,
 'D_n': 1.5,
 'L_f': 50.73, #prestocabin,
 'L_n': 5.725,
 'Lb_v': 0.6,
 'Lc_h': 4.75,
 'MLW_frac': 0.9228915662650602,
 'Mach_altcruise': 0.4,
 'Mach_cruise': 0.80,
 'S_w': 139.566,
 'W_crew': 6860,
 'W_payload': 225630.0,
 'altitude_altcruise': 4572,
 'altitude_cruise': 10000.0,
 'altitude_landing': 0.0,
 'altitude_takeoff': 0.0,
 'b_ail_b_wing': 0.34,
 'b_flap_b_wing': 0.6,
 'b_slat_b_wing': 0.0,
 'block_range': 740800.0,
 'block_time': 8399.999999999998,
 'c_ail_c_wing': 0.27,
 'c_flap_c_wing': 0.3,
 'c_slat_c_wing': 0.0,
 'c_tank_c_w': 0.4,
 'clmax_w': 1.8,
 'dihedral_h': 0.13369222070276564,
 'dihedral_w': 0.09634217471008,
 'distance_landing': 1800.0,
 'distance_takeoff': 1800.0,
 'engine': {'BPR': 10.04,
            'Cbase': None,
            'model': 'Howe turbofan'},
 'eta_h': 1.0,
 'flap_type': 'double slotted',
 'h_ground': 10.668000000000001,
 'k_exc_drag': 0.03,
 'loiter_time': 2700,
 'n_captains': 1,
 'n_copilots': 1,
 'n_engines': 2,
 'n_engines_under_wing': 2,
 'range_altcruise': 370400.0,
 'range_cruise': 7000000,
 'rho_f': 804,
 'slat_type': None,
 'sweep_h': 0.50614548307835557,
 'sweep_v': 0.64228116473391328,
 'sweep_w': 0.44156830075456538,
 'taper_h': 0.296,
 'taper_v': 0.310,
 'taper_w': 0.258,
 'tcr_h': 0.1,
 'tcr_v': 0.1,
 'tcr_w': 0.123,
 'tct_h': 0.1,
 'tct_v': 0.1,
 'tct_w': 0.096,
 'type': 'transport',
 'x_mlg': 23.2,
 'x_n': 23.2,
 'x_nlg': 10,
 'x_tailstrike': 43,
 'x_tank_c_w': 0.2,
 'xcg_crew': 2.5,
 'xcg_payload': 14.4,
 'xr_w': 20,
 'y_mlg': 2.47,
 'y_n': 7,
 'z_lg': -2.0,
 'z_n': -2,
 'z_tailstrike': -0.84,
 'zr_h': 0,
 'zr_v': 0.0,
 'zr_w': -1.5}

AIRPLANE_CONFIGURATION = 1
# airplane['AR_w'] = 8.43
if AIRPLANE_CONFIGURATION == 1:
 airplane = airplane_3_3
else:
 airplane = airplane_2_3_2
# Execute the geometry function from the designTools module (dt)
dt.geometry(airplane)

# Call the plotting function to make sure the aircraft is correct
dt.plot3d(airplane)

# Execute the weight estimation module
W0_guess = 90000*9.81
T0_guess = 0.3*W0_guess
W0, We, Wf, Mf_cruise, xcg_e = dt.weight(W0_guess, T0_guess, airplane, CONSIDER_lOITER=True, CONSIDER_CRUISE2= True)

print('Weights. in Newtons:')

print('W0:',W0)
print('We:',We)
print('Wf:',Wf)
print('Wp:',airplane['W_payload'])
print('Wc:',airplane['W_crew'])

print('breakdown:')
for key in ['W_w','W_h','W_v','W_f','W_nlg','W_mlg','W_eng','W_allelse']:
    print(key+': ',airplane[key])

