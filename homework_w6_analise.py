import designTool as dt
import matplotlib.pyplot as plt
import numpy as np
import pprint

# Load the standard airplane
#airplane = dt.standard_airplane('fokker100')

# 3 x 3 Cross-section configuration airplane
airplane = {
'AR_h': 5.380,
 'AR_v': 1.730,
 'AR_w': 11,
 'Cht': 1.1,
 'Cvt': 0.09,
 'D_f': 4.07, #prestocabin,
 'D_n': 2,
 'L_f': 53.47, #prestocabin,
 'L_n': 3.73, #https://aircraft-database.com/database/engine-models/pw2040d
 'Lb_v': 0.48,
 'Lc_h': 5,
 'MLW_frac': 0.85,
 'Mach_altcruise': 0.4,
 'Mach_cruise': 0.80,
 'S_w': 168,
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
 'c_flap_c_wing': 0.3,
 'c_slat_c_wing': 0.1,
 'c_tank_c_w': 0.6,
 'clmax_w': 1.8, #unchanged
 'dihedral_h': 0.13369222070276564,
 'dihedral_w': 0.09634217471008,
 'distance_landing': 2300.0,
 'distance_takeoff': 2300.0,
 'engine': {'BPR': 5.9, # CFM56 6.4 #PW1100G 12.5
           'Cbase': 0.33/3600,
           'weight': 3311*dt.gravity, #CFM56 2585*dt.gravity
           'T0': 40900, 
           'model': 'Howe turbofan'},
 'eta_h': 1.0,
 'flap_type': 'triple slotted',
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
 'x_mlg': 26.3,
 'x_n': 20.6,
 'x_nlg': 7,
 'x_tailstrike': 40.4,
 'x_tank_c_w': 0.2,
 'xcg_crew': 5,
 'xcg_payload': 25,
 'xr_w': 19.7,#20,
 'y_mlg': 5,
 'y_n': 7.3,
 'z_lg': -3.3,
 'z_n': -1.9,
 'z_tailstrike': -0.8,
 'zr_h': 0,
 'zr_v': 0.8,
 'zr_w': -1.5}

g = dt.gravity
MTOW = 114795 # kg
W0_guess = MTOW*g
T0_PEExplorer = 2*airplane["engine"]["T0"]*dt.lb2N

range_cruise = airplane['range_cruise']
W_payload = airplane['W_payload']
W_crew = airplane['W_crew']


dt.geometry(airplane)
W0, We, Wf, Mf_cruise, xcg_e = dt.weight(W0_guess, T0_PEExplorer, airplane)

T0, T0vec, deltaS_wlan, CLmaxTO = dt.performance(W0, Mf_cruise, airplane)
T0_vector = np.multiply(T0vec,1.05)

if (T0_PEExplorer >= T0):
    Performance = "Yes"
else:
    Performance = "No"

print("MTOW (kg): ", W0/g)
print("Needed fuel for selected range: ", Wf/g)    
print('\tRequired thrust (1 engine) =',T0/dt.lb2N/2,'lbf')
print("given T0: ",airplane["engine"]["T0"],'lbf')
print("")
print("Airplane matches performance needs?: ", Performance)
print("")

# Execute the geometry function from the designTools module (dt)
airplane = dt.analyze(airplane = airplane,
                      print_log = True, # Plot results on the terminal screen
                      plot = True, # Generate 3D plot of the aircraft
                      W0_guess= W0
                      )

def check_constraints(airplane):
    print("Constraints check:")
    airplane_passed = True
    if airplane['deltaS_wlan'] < 0:
        airplane_passed = False
        print('deltaS_wlan < 0')
    if airplane['SM_fwd'] > 0.3:
        airplane_passed = False
        print('SM_fwd: ', airplane['SM_fwd'])
        print('SM_fwd > 0.3')
    if airplane['SM_aft'] < 0.05:
        airplane_passed = False
        print('SM_aft < 0.05')
    if airplane['CLv'] > 0.75:
        airplane_passed = False
        print('CLv > 0.75')
    if airplane['frac_nlg_fwd'] > 0.18:
        airplane_passed = False
        print('frac_nlg_fwd > 0.18')
    if airplane['frac_nlg_aft'] < 0.05:
        airplane_passed = False
        print('frac_nlg_aft < 0.05')
        print('frac_nlg_aft: ',airplane['frac_nlg_aft'])
    if airplane['alpha_tipback'] < 15*np.pi/180:
        airplane_passed = False
        print('alpha_tipback < 15 deg')
    if airplane['alpha_tailstrike'] < 10*np.pi/180:
        airplane_passed = False
        print('alpha_tailstrike < 10 deg')
        print('alpha_tailstrike: ',airplane['alpha_tailstrike']/(np.pi/180))
    if airplane['phi_overturn'] > 63*np.pi/180:
        airplane_passed = False
        print('phi_overturn > 63 deg')
    if airplane['b_tank_b_w'] > 0.95:
        airplane_passed = False
        print('b_tank_b_w > 0.95')
    
    if airplane_passed:
        print('Airplane passed the constraints!')
    wing_span = np.sqrt(airplane["AR_w"]*airplane["S_w"])
    print("wing span: ", wing_span, "m")
    return airplane_passed

airplane_passed = check_constraints(airplane)