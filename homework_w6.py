import designTool as dt
import matplotlib.pyplot as plt
import numpy as np
import airplane_handler

# Load the standard airplane
#airplane = dt.standard_airplane('fokker100')

# Load airplane from file
airplane = airplane_handler.load_airplane('airplane.txt')

g = dt.gravity
MTOW = airplane['W0']/g # kg
W0_guess = airplane['W0']
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
airplane = dt.analyze(airplane,
                      print_log = True, # Plot results on the terminal screen
                      plot = False, # Generate 3D plot of the aircraft
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
dt.plot3d(airplane)
#airplane_handler.save_airplane(airplane,'airplane.txt')