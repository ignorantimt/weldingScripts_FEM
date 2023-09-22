import utilities as ut

path2txt = "..\output\disp-temp-inp.txt"
length_path = 143.65
welding_vel = 13.33
t0 = 0.105651
length_single_step = t0*welding_vel
num_steps = int(round(length_path/length_single_step))

with open(path2txt, "w") as file:
    ut.createMatTC4(file)
    file.write("**\n")
    file.write(f"** PREDEFINED FIELDS\n")
    file.write(f"** Name: Predefined Field-1   Type: Temperature\n")
    file.write(f"*Initial Conditions, type=TEMPERATURE, file=X:\\ABQ_ws\\singleBlade-heat-0917.odb, step=1, inc=1, midside\n")
    ut.createStaticStep(file, 0, 0.01, 0.01, 0.01)
    ut.createIntModelChange(file, 0, 'r')
    file.write("**\n")
    file.write("** BOUNDARY CONDITIONS\n")
    file.write("**\n")
    file.write(f"** Name: BC-3 Type: Displacement/Rotation\n")
    file.write("*Boundary\n")
    file.write("Set-fix-blade, PINNED\n")
    # file.write("Set-fix-blade, 3, 3\n")
    file.write(f"** Name: BC-left Type: Displacement/Rotation\n")
    file.write("*Boundary\n")
    file.write("Set-fix-left, PINNED\n")
    # file.write("Set-fix-left, 2, 2\n")
    # file.write("Set-fix-left, 3, 3\n")
    file.write(f"** Name: BC-right Type: Displacement/Rotation\n")
    file.write("*Boundary\n")
    file.write("Set-fix-right, 2, 2\n")

    ut.createPredefineTempField(file, step_num=0)

    ut.editSolveControl(file, 20)

    file.write(f"**\n")
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
    file.write("PPRESS\n")
    ut.endStep(file)
    for step_num in range(1, num_steps + 1):
        ut.createStaticStep(file, step_num, t0, t0, t0)
        ut.createIntModelChange(file,step_num,'a')
        ut.createPredefineTempField(file, step_num=step_num+1)
        ut.endStep(file)
    ut.createStaticStep(file, num_steps+1, t0, 17*t0, t0)
    ut.endStep(file)
    ut.createStaticStep(file, num_steps+2, 1, 1800, 60)
    ut.endStep(file)
    ut.createStaticStep(file, num_steps+3, 1, 1, 1)
    ut.endStep(file)

print(f"代码已写入到{path2txt}文件中，共包含{num_steps+4}个步骤。")
