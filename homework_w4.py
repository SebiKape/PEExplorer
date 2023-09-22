# Remember to save this script in the same directory as designTool.py

# AP-701 - Fundamentos de Projeto de Aeronaves
# Class: PEE31 2023
# Homework 3
# Group: PEExplorer
# Members:
#   Alan Augusto Tomaz
#   Caroline de Souza Faria Silva 
#   Mariana Tessmann Martins
#   Matheus Ribeiro Lira
#   Raphael Machado Cezar
#   Sebastian Mroginski Kapelius

# IMPORTS
import designTool as dt
import numpy as np
import pprint
import matplotlib.pyplot as plt

# AIRPLANE_TO_BE_SIMULATED (3 X 3 OR 2 X 3 X 2)
# This parameter chooses which airplane will be used throughout the code execution. The possible values are:
#   1 to 3 x 3 cross-section configuration airplane
#   2 to 2 x 3 x 2 cross-section configuration airplane
AIRPLANE_TO_BE_SIMULATED = 1

# 3 x 3 Cross-section configuration airplane
airplane_3_3 = {
'AR_h': 5.380,
 'AR_v': 1.730,
 'AR_w': 11,
 'Cht': 0.61,
 'Cvt': 0.08,
 'D_f': 4.07, #prestocabin,
 'D_n': 2.3,
 'L_f': 53.47, #prestocabin,
 'L_n': 5.725,
 'Lb_v': 0.458,
 'Lc_h': 4.4,
 'MLW_frac': 0.8, #0.9228915662650602
 'Mach_altcruise': 0.4,
 'Mach_cruise': 0.80,
 'S_w': 180,
 'W_crew': (2*240 + 5*220)*dt.lb2N,
 'W_payload': 230*195*dt.lb2N,
 'altitude_altcruise': 4572,
 'altitude_cruise': 10000,
 'altitude_landing': 0.0,
 'altitude_takeoff': 0.0,
 'b_ail_b_wing': 0.34,
 'b_flap_b_wing': 0.6,
 'b_slat_b_wing': 0.75,
 'block_range': 740800.0,
 'block_time': 8399.999999999998,
 'c_ail_c_wing': 0.27,
 'c_flap_c_wing': 0.3,
 'c_slat_c_wing': 0.1,
 'c_tank_c_w': 0.5,
 'clmax_w': 1.8, #unchanged
 'dihedral_h': 0.13369222070276564,
 'dihedral_w': 0.09634217471008,
 'distance_landing': 2300.0,
 'distance_takeoff': 2300.0,
 'engine': {'BPR': 12.5, # PW1134GA/2-JM
            'Cbase': 0.685/3600, #TSFC from Howe [2] Eq. 3.12a & PW1127G https://mediatum.ub.tum.de/doc/1283437/1283437.pdf
            'weight': 2858*dt.gravity,
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
 'sweep_w': 23*np.pi/180, # From week 2
 'taper_h': 0.296,
 'taper_v': 0.310,
 'taper_w': 0.258,
 'tcr_h': 0.1,
 'tcr_v': 0.1,
 'tcr_w': 0.123, # unchanged
 'tct_h': 0.1,
 'tct_v': 0.1,
 'tct_w': 0.096,
 'type': 'transport',
 'x_mlg': 26.5,
 'x_n': 20,
 'x_nlg': 6,
 'x_tailstrike': 41,
 'x_tank_c_w': 0.2,
 'xcg_crew': 5,
 'xcg_payload': 26,
 'xr_w': 21,#20,
 'y_mlg': 5,
 'y_n': 7,
 'z_lg': -3.6,
 'z_n': -1.9,
 'z_tailstrike': -0.8,
 'zr_h': 0,
 'zr_v': 0.8,
 'zr_w': -1.5}

# 2 x 3 x 2 Cross-section configuration airplane
airplane_2_3_2 = {'AR_h': 5.380,
 'AR_v': 1.730,
 'AR_w': 11.0,
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
 #'S_w': 200,
 'S_w': 139.566,
 'W_crew': (2*240+5*220)*dt.lb2N,
 'W_payload': 230*190*dt.lb2N,
 'altitude_altcruise': 4572, 
 'altitude_cruise': 10000, #8000.32,
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
 'engine': {'BPR': 8.6,
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
 'sweep_w': 30*np.pi/180, # From week 2
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

if AIRPLANE_TO_BE_SIMULATED == 2:
    print("Chosen airplane cross-section: 2 x 3 x 2")
    airplane = airplane_2_3_2
else:
    print("Chosen airplane cross-section: 3 x 3")
    airplane = airplane_3_3

# 2. Load a sample case already defined in designTools.py:
# (uncomment the line below)
# airplane = dt.standard_airplane('fokker100')

# Execute the geometry function
dt.geometry(airplane)

# Print updated dictionary
#print('airplane = ' + pprint.pformat(airplane))

# WEEK 4 HOMEWORK   
g = dt.gravity
MTOW = 103500 # kg
W0_guess = MTOW*g
T0_guess = 0.3*W0_guess
chosen_AR_w = 8
AR_upper_limit = 14
AR_lower_limit = 6
number_of_points = 1000
step = (AR_upper_limit - AR_lower_limit)/number_of_points

AR_vector = np.linspace(AR_lower_limit, AR_upper_limit, number_of_points)
W0_vector = []
W0_chosen_AR = 0
W_w = 0
W_h = 0
W_v = 0
W_f = 0
W_nlg = 0
W_mlg = 0
W_eng = 0
W_allelse = 0

for AR in AR_vector:
    airplane['AR_w'] = AR
    dt.geometry(airplane)
    W0, We, Wf, Mf_cruise, xcg_e = dt.weight(W0_guess, T0_guess, airplane)
    W0_vector.append(W0)
    if abs(AR - chosen_AR_w) <= step:
        W_w = airplane['W_w']
        W_h = airplane['W_h']
        W_v = airplane['W_v']
        W_f = airplane['W_f']
        W_mlg = airplane['W_mlg']
        W_nlg = airplane['W_nlg']
        W_eng = airplane['W_eng']
        W_allelse = airplane['W_allelse']
        W0_chosen_AR = W0

plt.figure(1)
plt.xlabel('Wing aspect ratio (ARw) [-]')
plt.ylabel('MTOW [N]')
plt.title('Wo x ARw')
plt.plot(AR_vector,W0_vector)
plt.show()


drags = [airplane['W_payload'],airplane['W_crew'],W_f,W_w,W_h,W_v,W_mlg,W_nlg,W_eng,W_allelse]
labels = ['Payload', 'Crew','Fuel','Wing','H. Stab.','V. Stab.','Main LG','Nose LG','Engine','All else']

plt.pie(drags, labels=labels)
plt.title('Airplane weight breakdown')
plt.show()