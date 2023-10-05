import utilities as ut

path2txt = "..\output\heat-inp.txt"
length_path = 143.65
welding_vel = 16.67
elem_num = 102
t0 = length_path/welding_vel/elem_num # time of single step
print(f"Time per step: {t0}")
length_single_step = t0*welding_vel
num_steps = int(round(length_path/length_single_step))

with open(path2txt, "w") as file:
    ut.createMatTC4(file)
    ut.createHeatTransStep(file, 0, 0.01, 0.01, 0.01)
    ut.addBodyDFlux(file)
    ut.createIntModelChange(file, 0, 'r')
    file.write("**\n")
    file.write("** OUTPUT REQUESTS\n")
    file.write("**\n")
    file.write("*Restart, write, frequency=0\n")
    file.write("**\n")
    file.write("** FIELD OUTPUT: F-Output-1\n")
    file.write("**\n")
    file.write("*Output, field, variable=PRESELECT\n")
    file.write("**\n")
    file.write("** HISTORY OUTPUT: H-Output-1\n")
    file.write("**\n")
    file.write("*Output, history\n")
    file.write("*Contact Output\n")
    file.write("HTL, PPRESS\n")
    ut.endStep(file)
    for step_num in range(1, num_steps + 1):
        ut.createHeatTransStep(file, step_num, t0, t0, t0)
        ut.createIntModelChange(file,step_num,'a')
        ut.endStep(file)

    ut.createHeatTransStep(file, num_steps+1, t0, 17*t0, t0)
    ut.endStep(file)
    ut.createHeatTransStep(file, num_steps+2, 1, 1800, 60)
    ut.endStep(file)
    ut.createHeatTransStep(file, num_steps+3, 1, 1, 1)
    ut.endStep(file)

print(f"代码已写入到{path2txt}文件中，共包含{num_steps+4}个步骤。")
