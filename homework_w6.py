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

# print("\n \n \n ")
# print("===========================================")
# print("COMPARAÇÃO COM TABELA DE VALORES HISTÓRICOS")
# print("===========================================")
# print("Código      |     Tabela valores históricos")
# print("===========================================")
# print("MTOW (kg): ",airplane['W0']/dt.gravity, "| 103500")
# print("Empty Weight (kg): ",airplane['We']/dt.gravity, "| 51080")
# print("Payload Weight (kg): ",airplane['W_payload']/dt.gravity, "| 28174")
# print("Range (km): ",airplane['range_cruise']/1000, "| 7000")
# print("Cruise Mach: ",airplane['Mach_cruise'], "| 0.8")
# print("Cruise altitude (m): ",airplane['altitude_cruise'], "| 11704.32")
# print("Takeoff distance (m): ",airplane['distance_takeoff'], "| 2300")
# print("Landing distance (m): ",airplane['distance_landing'], "| 1573.46")
# print("------------------ASAS---------------------")
# print("S_w (m²): ",airplane['S_w'], "| 139.566")
# print("AR_w: ",airplane['AR_w'], "| 9.17")
# print("Taper_w: ",airplane['taper_w'], "| 0.258")
# print("Sweep_w (°): ",airplane['sweep_w']*180/np.pi, "| 25.3")
# print("Dihedral_w (°): ",airplane['dihedral_w']*180/np.pi, "| 5.52")
# print("----------Empenagem Horizontal--------------")
# print("S_h (m²): ",airplane['S_h'], "| 36.6")
# print("AR_h: ",airplane['AR_h'], "| 5.38")
# print("Taper_h: ",airplane['taper_h'], "| 0.296")
# print("Sweep_h (°): ",airplane['sweep_h']*180/np.pi, "| 29")
# print("Dihedral_h (°): ",airplane['dihedral_h']*180/np.pi, "| 7.66")
# print("Lc_h: ",airplane['Lc_h'], "| 4.77")
# print("Cht: ",airplane['Cht'], "| 1.219")
# print("------------Empenagem Vertical--------------")
# print("S_v (m²): ",airplane['S_v'], "| 28.8")
# print("AR_v: ",airplane['AR_v'], "| 1.73")
# print("Taper_v: ",airplane['taper_v'], "| 0.31")
# print("Sweep_v (°): ",airplane['sweep_v']*180/np.pi, "| 36.8")
# print("Lb_v: ",airplane['Lb_v'], "| 0.557")
# print("Cvt: ",airplane['Cvt'], "| 0.111")
# print("-----------------Fuselagem------------------")
# print("Fuselage length (m): ",airplane['L_f'], "| 47.462")
# print("Fuselage diameter (m): ",airplane['D_f'], "| 3.833")
# #print("Cockpit length / Diameter: ",airplane[''], "| 1.494")
# print("Tail cone length / Diameter: ",((airplane['L_f']-airplane['x_tailstrike'])/(airplane['D_f'])), "| 3.229")
# print("Total maximum thrust or power (N): ",airplane['T0'], "| 316268.56")
# print("Engine TSFC (lb/lbf/h): ",airplane['engine']['Cbase']*3600, "| 0.510")
# #print("Wing loading (kg/m²): ",airplane[''], "| 741.6")
# print("Thrust-to-weight ratio: ",airplane['T0']/airplane['W0'], "| 0.312")