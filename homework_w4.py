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
import matplotlib.colors as mcolors

# AIRPLANE_TO_BE_SIMULATED (3 X 3 OR 2 X 3 X 2)
# This parameter chooses which airplane will be used throughout the code execution. The possible values are:
#   1 to 3 x 3 cross-section configuration airplane
#   2 to 2 x 3 x 2 cross-section configuration airplane
AIRPLANE_TO_BE_SIMULATED = 1

# 3 x 3 Cross-section configuration airplane
airplane_3_3 = {
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
'S_w': 178,
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
'engine': {'BPR': 4.9, # PW2040D #JT9D-7R4D
        'Cbase': 0.343/3600, #0.33
        'weight': 4053*dt.gravity, #3311*dt.gravity, #PW2040D 
        'T0': 48000, #40900
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

# 2 x 3 x 2 Cross-section configuration airplane
airplane_2_3_2 = {'AR_h': 5.380,
 'AR_v': 1.730,
 'AR_w': 9.17,
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
 'W_crew': (2*240 + 5*220)*dt.lb2N, #6*190*dt.lb2N,
 'W_payload': 230*195*dt.lb2N,
 'altitude_altcruise': 4572, 
 'altitude_cruise': 10000,
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
chosen_AR_w = 11
print('Chosen value of Wing AR:',chosen_AR_w)
AR_upper_limit = 14
AR_lower_limit = 6
step = 0.01

AR_vector = np.arange(6, 14 + step, step)
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
    if abs(AR - chosen_AR_w) < step/2:
        W_payload = airplane['W_payload']
        W_crew = airplane['W_crew']
        W_w = airplane['W_w']
        W_h = airplane['W_h']
        W_v = airplane['W_v']
        W_fuselage = airplane['W_f']
        W_fuel = Wf
        W_mlg = airplane['W_mlg']
        W_nlg = airplane['W_nlg']
        W_eng = airplane['W_eng']
        W_allelse = airplane['W_allelse']
        W0_chosen_AR = W0
        print('Weight distribution for AR_w =',chosen_AR_w)
        print('W0:', W0/g,'kg')
        print('Empty weight:', We/g,'kg')
        print('Payload weight:', W_payload/g,'kg')
        print('Crew weight:',W_crew/g)
        print('Fuel weight:', W_fuel/g,'kg')
        print('Wing weight:',W_w/g,'kg')
        print('Horizontal Stabilizer weight:',W_h/g,'kg')
        print('Vertical Stabilizer weight:',W_v/g,'kg')
        print('Main Landing Gear weight:',W_mlg/g,'kg')
        print('Nose Landing Gear weight:',W_nlg/g,'kg')
        print('Engine weight:',W_eng/g,'kg')
        print('Fuselage weight:',W_fuselage/g,'kg')
        print('All else weight:',W_allelse/g,'kg')

plt.figure(1)
plt.xlabel('Wing aspect ratio (ARw) [-]')
plt.ylabel('MTOW [N]')
plt.title('Wo x ARw')
plt.plot(AR_vector,W0_vector)
plt.show()


drags = [W_payload,W_crew,W_fuel,W_w,W_h,W_v,W_mlg,W_nlg,W_eng,W_fuselage,W_allelse]
labels = ['Payload', 'Crew','Fuel','Wing','H. Stab.','V. Stab.','Main LG','Nose LG','Engine','Fuselage','All else']

plt.pie(drags, labels=labels, autopct='%.1f%%', startangle=90, textprops={'size':'small'}, 
        colors=['tab:blue','tab:orange','tab:green','tab:red','tab:purple','tab:brown','tab:pink',
                'tab:gray','tab:olive','tab:cyan','gold'])
plt.title('Airplane weight breakdown')
plt.show()