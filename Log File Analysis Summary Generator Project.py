with open('Project Log File.txt', 'r') as f:
    count = 0
    for line in f:
        count += 1
with open('New Project Log File.txt', 'w') as wf:
    wf.write('Total lines in the log: ')
    wf.write(str(count))