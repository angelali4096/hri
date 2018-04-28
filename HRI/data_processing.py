import yaml
import os
import xlsxwriter

num_manual = 0
num_automatic = 0
num_forced = 0

manual_task_times = []
automatic_task_times = []
forced_task_times = []

partial_manual_task_times = []
partial_automatic_task_times = []
partial_forced_task_times = []
full_manual_task_times = []
full_automatic_task_times = []
full_forced_task_times = []

partial_manual_mode_switches = 0
partial_automatic_mode_switches = 0
partial_forced_mode_switches = 0
full_manual_mode_switches = 0
full_automatic_mode_switches = 0
full_forced_mode_switches = 0

partial_manual_mode_switches_l = []
partial_automatic_mode_switches_l = []
partial_forced_mode_switches_l = []
full_manual_mode_switches_l = []
full_automatic_mode_switches_l = []
full_forced_mode_switches_l = []

for f in os.listdir("data/"):
    print f
    with open("data/" + f, 'r') as stream:
        data = yaml.load(stream)
        num_moves = len(data) - 2
        last_move_str = "move" + str(num_moves)
        task_time = float(data[last_move_str]["time"]) - float(data["move0"]["time"])

        assistance_type = data["general info"]["assistance_type"]
        map_id = data["general info"]["map_id"]
        mode = data["move0"]["mode"]

        if assistance_type == 1:
            manual_task_times.append(task_time)
            if map_id == 1:
                full_manual_task_times.append(task_time)
            else:
                partial_manual_task_times.append(task_time)
        elif assistance_type == 2:
            automatic_task_times.append(task_time)
            if map_id == 1:
                full_automatic_task_times.append(task_time)
            else:
                partial_automatic_task_times.append(task_time)
        else:
            forced_task_times.append(task_time)
            if map_id == 1:
                full_forced_task_times.append(task_time)
            else:
                partial_forced_task_times.append(task_time)

        for i in range(0, num_moves + 1):
            move_str = "move" + str(i)
            if assistance_type == 1 and data[move_str]["keypress"] == "space":
                if map_id == 1:
                    full_manual_mode_switches = full_manual_mode_switches + 1
                else:
                    partial_manual_mode_switches = partial_manual_mode_switches + 1
                mode = data[move_str]["mode"]
            elif assistance_type == 2 and data[move_str]["keypress"] == "space":
                if map_id == 1:
                    full_automatic_mode_switches = full_automatic_mode_switches + 1
                else:
                    partial_automatic_mode_switches = partial_automatic_mode_switches + 1
            elif assistance_type == 3 and data[move_str]["keypress"] == "space":
                if map_id == 1:
                    full_forced_mode_switches = full_forced_mode_switches + 1
                else:
                    partial_forced_mode_switches = partial_forced_mode_switches + 1

        if assistance_type == 1 and map_id == 1:
            full_manual_mode_switches_l.append(full_manual_mode_switches)
            full_manual_mode_switches = 0
        elif assistance_type == 1 and map_id == 2:
            partial_manual_mode_switches_l.append(partial_manual_mode_switches)
            partial_manual_mode_switches = 0
        elif assistance_type == 2 and map_id == 1:
            full_automatic_mode_switches_l.append(full_automatic_mode_switches)
            full_automatic_mode_switches = 0
        elif assistance_type == 2 and map_id == 2:
            partial_automatic_mode_switches_l.append(partial_automatic_mode_switches)
            partial_automatic_mode_switches = 0
        elif assistance_type == 3 and map_id == 1:
            full_forced_mode_switches_l.append(full_forced_mode_switches)
            full_forced_mode_switches = 0
        else:
            partial_forced_mode_switches_l.append(partial_forced_mode_switches)
            partial_forced_mode_switches = 0

# avg_manual_task_time = sum(manual_task_times)/len(manual_task_times)
# avg_automatic_task_time = sum(automatic_task_times)/len(automatic_task_times)
# avg_forced_task_time = sum(forced_task_times)/len(forced_task_times)

avg_partial_manual_task_times = sum(partial_manual_task_times)/len(partial_manual_task_times)
avg_partial_automatic_task_times = sum(partial_automatic_task_times)/len(partial_automatic_task_times)
avg_partial_forced_task_times = sum(partial_forced_task_times)/len(partial_forced_task_times)
avg_full_manual_task_times = sum(full_manual_task_times)/len(full_manual_task_times)
avg_full_automatic_task_times = sum(full_automatic_task_times)/len(full_automatic_task_times)
avg_full_forced_task_times = sum(full_forced_task_times)/len(full_forced_task_times)

workbook = xlsxwriter.Workbook('mode_switching_data.xlsx')
worksheet = workbook.add_worksheet()

# row = 0
# col = 0
# worksheet.write(row, col, 'Times (Full Observability + Manual)')
# row = row + 1
# for t in full_manual_task_times:
#     worksheet.write(row, col, t)
#     row = row + 1

# row = 0
# col = 1
# worksheet.write(row, col, 'Times (Full Observability + Automatic)')
# row = row + 1
# for t in full_automatic_task_times:
#     worksheet.write(row, col, t)
#     row = row + 1

# row = 0
# col = 2
# worksheet.write(row, col, 'Times (Full Observability + Forced)')
# row = row + 1
# for t in full_forced_task_times:
#     worksheet.write(row, col, t)
#     row = row + 1

# row = 0
# col = 3
# worksheet.write(row, col, 'Times (Partial Observability + Manual)')
# row = row + 1
# for t in partial_manual_task_times:
#     worksheet.write(row, col, t)
#     row = row + 1

# row = 0
# col = 4
# worksheet.write(row, col, 'Times (Partial Observability + Automatic)')
# row = row + 1
# for t in partial_automatic_task_times:
#     worksheet.write(row, col, t)
#     row = row + 1

# row = 0
# col = 5
# worksheet.write(row, col, 'Times (Partial Observability + Forced)')
# row = row + 1
# for t in partial_forced_task_times:
#     worksheet.write(row, col, t)
#     row = row + 1

row = 0
col = 0
worksheet.write(row, col, 'Full Observability + Manual')
row = row + 1
for t in full_manual_mode_switches_l:
    worksheet.write(row, col, t)
    row = row + 1

row = 0
col = 1
worksheet.write(row, col, 'Full Observability + Automatic')
row = row + 1
for t in full_automatic_mode_switches_l:
    worksheet.write(row, col, t)
    row = row + 1

row = 0
col = 2
worksheet.write(row, col, 'Full Observability + Forced')
row = row + 1
for t in full_forced_mode_switches_l:
    worksheet.write(row, col, t)
    row = row + 1

row = 0
col = 3
worksheet.write(row, col, 'Partial Observability + Manual')
row = row + 1
for t in partial_manual_mode_switches_l:
    worksheet.write(row, col, t)
    row = row + 1

row = 0
col = 4
worksheet.write(row, col, 'Partial Observability + Automatic')
row = row + 1
for t in partial_automatic_mode_switches_l:
    worksheet.write(row, col, t)
    row = row + 1

row = 0
col = 5
worksheet.write(row, col, 'Partial Observability + Forced')
row = row + 1
for t in partial_forced_mode_switches_l:
    worksheet.write(row, col, t)
    row = row + 1

workbook.close()