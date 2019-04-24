
"""  Water and Temperature Control Automation of a Plant 
Humidity Sensor Output Legend: 0%: 0(0000); 10%: 1(0001); 20%: 2(0010);
30%: 3(0011); 40%: 4(0100); 50%: 5(0101); 60%: 6(0110); 70%: 7(0111); 
80%: 13(1101); 90%: 14(1110); 100%: 15(1111)

Temperature Sensor Output Legend (Celsius): <17.5: 0(000); 20: 1(001);
22.5: 2(010); 25: 3(011); 27.5: 4(100); 30: 5(101); 32.5: 6(110); 35: 7(111); 

Water Pump: ON (1) or OFF (0)

A/C: Heating (11), Cooling (01) or OFF (00)
"""

import pyrtl
import matplotlib


start = pyrtl.Input(1, 'start')
reset = pyrtl.Input(1, 'reset')
water = pyrtl.Input(4, 'water')
temperature = pyrtl.Input(3, 'temperature')
pump = pyrtl.Output(1, 'pump')
ac = pyrtl.Output(2, 'ac')
state_water = pyrtl.Register(3, 'state_water') #S0 S1 S5 S6
state_temperature = pyrtl.Register(3, 'state_temperature') #S0 S1 S2 S3 S4


# First new step, let's enumerate a set of constant to serve as our states
S0, S1, S2, S3, S4, S5, S6 = [pyrtl.Const(x, bitwidth=3) for x in range(7)]

with pyrtl.conditional_assignment:
    with start:  # power is ON
		with reset:  # system in reset
			state_water.next |= S1
			state_temperature.next |= S1
		with pyrtl.otherwise: # functioning
			with (state_water == S0): # if previous state_water is power OFF
				state_water.next |= S1
				with (state_temperature == S0): 
					state_temperature.next |= S1
			with (state_water == S1):
				state_water.next |= S5
				with (state_temperature == S1):
					state_temperature.next |= S2
			with state_water == S5: # pump ON
				with water <= 14: # less than or equal to %90
					state_water.next |= S5
					with state_temperature == S2: #ac OFF
						with temperature < 2: # less than 22,5
							state_temperature.next |= S3
						with temperature > 5: # higher than 30
							state_temperature.next |= S4
						with pyrtl.otherwise: # between 22,5 and 30
							state_temperature.next |= S2
					with state_temperature == S3: # heat
						with temperature <= 5: # less than 30
							state_temperature.next |= S3
						with temperature > 5: # higher than 30
							state_temperature.next |= S2
					with state_temperature == S4: #cool
						with temperature <= 2: # less than 22.5
							state_temperature.next |= S2
						with temperature > 2: # higher than 22.5
							state_temperature.next |= S4
				with water > 14: # higher than %90
					state_water.next |= S6
					with state_temperature == S2: #ac OFF
						with temperature < 2: # less than 22,5
							state_temperature.next |= S3
						with temperature > 5: # higher than 30
							state_temperature.next |= S4
						with pyrtl.otherwise: # between 22,5 and 30
							state_temperature.next |= S2
					with state_temperature == S3: # heat
						with temperature <= 5: # less than 30
							state_temperature.next |= S3
						with temperature > 5: # higher than 30
							state_temperature.next |= S2
					with state_temperature == S4: #cool
						with temperature <= 2: # less than 22.5
							state_temperature.next |= S2
						with temperature > 2: # higher than 22.5
							state_temperature.next |= S4
			with state_water == S6: # pump OFF
				with water <= 5: # less than or equal to %50
					state_water.next |= S5
					with state_temperature == S2: #ac OFF
						with (temperature <= 5) | (temperature >= 2 ): # between 22,5 and 30
							state_temperature.next |= S2
						with temperature < 2: # less than 22,5
							state_temperature.next |= S3
						with temperature > 5: # higher than 30
							state_temperature.next |= S4
					with state_temperature == S3: # heat
						with temperature <= 5: # less than 30
							state_temperature.next |= S3
						with temperature > 5: # higher than 30
							state_temperature.next |= S2
					with state_temperature == S4: #cool
						with temperature <= 2: # less than 22.5
							state_temperature.next |= S2
						with temperature > 2: # higher than 22.5
							state_temperature.next |= S4
				with water > 5: # higher than %50
					state_water.next |= S6
					with state_temperature == S2: #ac OFF
						with (temperature <= 5) | (temperature >= 2 ): # between 22,5 and 30
							state_temperature.next |= S2
						with temperature < 2: # less than 22,5
							state_temperature.next |= S3
						with temperature > 5: # higher than 30
							state_temperature.next |= S4
					with state_temperature == S3: # heat
						with temperature <= 5: # less than 30
							state_temperature.next |= S3
						with temperature > 5: # higher than 30
							state_temperature.next |= S2
					with state_temperature == S4: #cool
						with temperature <= 2: # less than 22.5
							state_temperature.next |= S2
						with temperature > 2: # higher than 22.5
							state_temperature.next |= S4
			with pyrtl.otherwise:  
				state_water.next |= S1
				state_temperature.next |= S1
    with pyrtl.otherwise:
		state_water.next |= S0 # power OFF
		state_temperature.next |= S0

pump <<= (state_water == S1) | (state_water == S5)
# for S3 (heating): ac=11; for S4 (cooling): ac=01
ac <<= 3*(state_temperature == S3) + (state_temperature == S4) 



# Output to a Verilog file named 'fsm_plant.v'
with open('fsm_plant.v', 'w') as v_file:
   pyrtl.OutputToVerilog(v_file)

# Simulation
print("--- Simulation Results ---")
sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)


# Rather than just give some random inputs, let's specify some specific values.  Recall
# that the sim.step method takes a dictionary mapping inputs to their values.  We could just
# specify the input set directly as a dictionary.

sim_inputs = {
    'start':   '11111111111111111111100',
    'reset':   '01000000000000000000000',
	'water':   ['0', '1', '2','3', '4', '5','6','7','7', '13','14','14','15','15','14','13','7','6','5','4','3','3','3'],
	'temperature':   ['0', '1', '2','1', '2', '3','4','5','6', '6','6','5','4','4','3','3','4','5','6','1','1','1','1']
    }

for cycle in range(len(sim_inputs['start'])):
    sim.step({w: int(v[cycle]) for w, v in sim_inputs.items()})

# also, to make our input/output easy to reason about let's specify an order to the traces
sim_trace.render_trace(trace_list=['start', 'reset', 'water', 'pump', 'temperature','ac','state_water', 'state_temperature'])



# Output of TestBench to a Verilog file named 'fsm_plant_tb.v'
with open('fsm_plant_tb.v', 'w') as tbfile:
    pyrtl.output_verilog_testbench(dest_file=tbfile, simulation_trace=sim_trace)
    #print(tbfile.getvalue())   

# print("--- Optimized Single-bit Verilog for the Counter ---")
pyrtl.synthesize()
pyrtl.optimize()

# Output to a Verilog file named 'fsm_plant_opt.v'
with open('fsm_plant_opt.v', 'w') as vfile:
    pyrtl.OutputToVerilog(vfile)
    #print(vfile.getvalue())
	
# Exit Program
exit(0)