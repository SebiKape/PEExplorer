import airplane_handler
import numpy as np
import designTool as dt


# Salva o dicionário carregado no python na versão txt

airplane = {
'AR_h': 5.380,
'AR_v': 1.730,
'AR_w': 10.5,
'Cht': 1.1,
'Cvt': 0.09,
'D_f': 4.07, #prestocabin,
'D_n': 2,
'L_f': 53.41, #prestocabin,
'L_n': 3.73, #https://aircraft-database.com/database/engine-models/pw2040d
'Lb_v': 0.51,
'Lc_h': 5,
'MLW_frac': 0.85,
'Mach_altcruise': 0.4,
'Mach_cruise': 0.80,
'S_w': 178, #178
'W_crew': (2*240 + 5*220)*dt.lb2N,
'W_payload': 230*195*dt.lb2N,
'altitude_altcruise': 4572,
'altitude_cruise': 11000,
'altitude_landing': 0.0,
'altitude_takeoff': 0.0,
'b_ail_b_wing': 0.34,
'b_flap_b_wing': 0.6,
'b_slat_b_wing': 0.75,
'block_range': 740800.0,
'block_time': 8399.999999999998,
'c_ail_c_wing': 0.27,
'c_flap_c_wing': 0.2,
'c_slat_c_wing': 0.1,
'c_tank_c_w': 0.6,
'clmax_w': 1.8, #unchanged
'dihedral_h': 0.13369222070276564,
'dihedral_w': 0.09634217471008,
'distance_landing': 2300.0,
'distance_takeoff': 2300.0,
'engine': {'BPR': 5.9, # PW2040D #JT9D-7R4D 4.9
        'Cbase': 0.33/3600, #0.33
        'weight':  3311*dt.gravity,   #4053*dt.gravity #JT9D-7R4D #3311*dt.gravity, #PW2040D 
        'T0': 40900, #PW2040D #40900 #JT9D-7R4D 48000
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
'slat_type': 'slat',
'sweep_h': 0.70,
'sweep_v': 0.64228116473391328,
'sweep_w': 25*np.pi/180, # From week 2
'taper_h': 0.296,
'taper_v': 0.310,
'taper_w': 0.3,
'tcr_h': 0.1,
'tcr_v': 0.1,
'tcr_w': 0.123, # unchanged
'tct_h': 0.1,
'tct_v': 0.1,
'tct_w': 0.085,
'type': 'transport',
'x_mlg': 26.7,
'x_n': 20.6,
'x_nlg': 7,
'x_tailstrike': 43.24,
'x_tank_c_w': 0.2,
'xcg_crew': 5,
'xcg_payload': 25,
'xr_w': 19.6,#20,
'y_mlg': 5,
'y_n': 7.3,
'z_lg': -3.7,
'z_n': -1.9,
'z_tailstrike': -0.7,
'zr_h': 0,
'zr_v': 0.8,
'zr_w': -1.5}

dt.analyze(airplane)

airplane_handler.save_airplane(airplane, 'airplane.txt')