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
import matplotlib.pyplot as plt
import airplane_handler

airplane = airplane_handler.load_airplane('airplane.txt')

# 2. Load a sample case already defined in designTools.py:
# (uncomment the line below)
# airplane = dt.standard_airplane('fokker100')

# Execute the geometry function
dt.geometry(airplane)

# Print updated dictionary
#print('airplane = ' + pprint.pformat(airplane))

# WEEK 5 HOMEWORK   
g = dt.gravity
MTOW = airplane['W0']/g # kg
W0_guess = airplane['W0']
T0_guess = 0.3*W0_guess
original_Sw = airplane['S_w']

step = 1
Sw_vector = np.arange(120, 240 + step, step)
T0_vector = []
W0_vector = []
deltaS_wlan_min = 1e3
Sw_at_deltaS_min = 0
W0_min = np.infty
Sw_at_W0_min = 0
T0_at_W0_min = 0

# Current project point
W0_current = airplane['W0']
Sw_current = airplane['S_w']
T0_current = airplane['engine']['T0']
current_airplane = airplane.copy()


for S_w in Sw_vector:
    # update wing area value on airplane
    airplane['S_w'] = S_w
    dt.geometry(airplane)

    # thrust matching
    dt.thrust_matching(W0_guess, T0_guess, airplane)

    # append T0vec and W0 for specific value of S_w
    T0_vector.append(airplane['T0vec'])
    W0_vector.append(airplane['W0'])
    #print(airplane['deltaS_wlan'],deltaS_wlan_min)
    # Finding S_w where Del ta_S_wlan = 0
    if np.abs(airplane['deltaS_wlan']) < deltaS_wlan_min:
        #print(airplane['deltaS_wlan'],deltaS_wlan_min)
        deltaS_wlan_min = np.abs(airplane['deltaS_wlan'])
        Sw_at_deltaS_min = S_w

    # Finding S_w where W0 is minimum
    if airplane['W0'] < W0_min:
        W0_min = airplane['W0']
        T0_at_W0_min = airplane['T0']
        Sw_at_W0_min = S_w

# Restoring original value of Wing area
airplane['S_w'] = original_Sw
dt.geometry(airplane)

T0_vector = np.array(T0_vector)
T0_vector = 1.05*T0_vector # Thrust safety margin

#print('Sw_deltaSmin',Sw_at_deltaS_min)
#print('deltaSmin',deltaS_wlan_min)


# T0vec x S_w
plt.figure(1)

# Design point of Benchmark Airplanes

# Airbus A321LR
T0_A321LR = 64320*dt.lb2N
W0_A321LR = 97000*g
Sw_A321LR = 122

# Boeing 757
T0_B757 = 87000*dt.lb2N
W0_B757 = 123603*g
Sw_B757 = 171.077

# Boeing 737 MAX 10
T0_B737 = 62000*dt.lb2N
W0_B737 = 89765*g
Sw_B737 = 125.621

# PEExplorer
# Chosen engine: PW2040D
T0_PEExplorer = T0_current*dt.lb2N*2 #2*40900*dt.lb2N
W0_PEExplorer = W0_current
Sw_PEExplorer = Sw_current

print('AIRPLANE\'s CURRENT PROJECT POINT:')
print('\tW0 =',W0_current,'N')
print('\tS_w =',Sw_current,'m²')
print('\tCurrent T0 =',T0_current*dt.lb2N*2,'N')
print('\tCurrent thrust (1 engine) =',T0_current,'lbf')

print('AIRPLANE\'s OPTIMAL PROJECT POINT (min W0):')
print('\tminimum W0 =',W0_min,'N')
print('\tS_w at minimum W0 =',Sw_at_W0_min,'m²')
print('\tT0 at minimum W0 =',T0_at_W0_min,'N')
print('\tRequired thrust (1 engine) =',T0_at_W0_min/dt.lb2N/2,'lbf')

# Plots 
for i in range (0,len(T0_vector[0])):
    plt.plot(Sw_vector, T0_vector[:,i])

plt.plot(Sw_PEExplorer,T0_PEExplorer, 'o')
plt.plot(Sw_A321LR, T0_A321LR, 'o')
plt.plot(Sw_B757, T0_B757,'o')
plt.plot(Sw_B737, T0_B737,'o')
plt.axvline(Sw_at_deltaS_min, linestyle = 'dashed', color = 'black')
legend = [
    'takeoff',
    'cruise',
    'FAR25.111',
    'FAR25.121a',
    'FAR25.121b',
    'FAR25.121c',
    'FAR25.119',
    'FAR25.121d',
    'PEExplorer',
    'A321LR',
    'B757-300',
    'B737 max 10',
    'ΔS_landing = 0'
]

plot_optimum = 0 #int(input('Deseja plotar o ponto ótimo na curva T0 x S_w? (0 para Não e 1 para Sim): '))
if plot_optimum == 1:
    plt.plot(Sw_at_W0_min,T0_at_W0_min, 'o')
    legend.append('PEExplorer (ponto ótimo)')

plt.legend(legend)

plt.xlabel('Wing area [m²]')
plt.ylabel('T0 [N]')
plt.title('T0 x Wing area')

plt.figure(2)
plt.plot(Sw_vector,W0_vector)
plt.xlabel('Wing area [m²]')
plt.ylabel('W0 [N]')
plt.title('W0 x Wing area')
plt.show()
change_Sw = 0 #int(input('Deseja atualizar o dicionário para uma nova área da asa? (0 para Não e 1 para Sim): '))
if change_Sw == 1:
    print(current_airplane['S_w'])
    current_airplane['S_w'] = float(input('Digite o valor da asa, em m²: '))
    dt.geometry(current_airplane)
    dt.thrust_matching(W0_current, T0_current, current_airplane)
    airplane_handler.save_airplane(current_airplane, 'airplane.txt')
else:
    print('O dicionário não será atualizado.')