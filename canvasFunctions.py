import json
import subprocess
import numpy as np

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def get_master_table_list():
    # change this function to read from a file ???
    
    with open('/data/informatica/canvas/master_table_list.txt') as f:
        lines = f.read().splitlines()
    
    # remove any lines commented out 
    cleanedlines = [c for c in lines if c[0] != '#']
    
    return sorted(cleanedlines)

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

def unpack_canvas_data(table_list):
    print('---------')
    print('Unpack Canvas Data ')
    print('---------')
    for table in table_list:
        print('---------')
        print(table)
        command = 'canvasDataCli unpack -c /data/informatica/canvas/config.js -f ' + table
        # subprocess.run(command, shell='true')  
        subprocess.call(command, shell='true')  
        # print(command)


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

def clean_canvas_files(table_list):
    ucf = '/data/informatica/canvas/UnpackedCanvasFiles/'
    print('---------')
    print('Clean Canvas Files ')
    print('---------')
    for table in table_list:
        print('---------')
        print(table)
        command = "sed 's#\\\\N##g'" + ' ' + ucf + table + '.txt > clean.txt'
        # print(command)
        # command = 'canvasDataCli unpack -c config.js -f ' + table
        # subprocess.run(command, shell='true')  
        subprocess.call(command, shell='true')  
        command = 'mv clean.txt ' + ucf + table + '.txt'
        # print(command)
        subprocess.call(command, shell='true')  


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# [] check last updated date?
# [] Send an email with any problems
def check_for_issues(canvas_table, master_table):
    if (not np.array_equal(canvas_table, master_table)):
        print('--------- ERROR')
        print('ERROR: Masterlist and CanvasList do not match!')
        print('--------- ERROR')
        # print('The Master Table List is not the same as Canvas Table List')
        not_in_canvas_list = np.setdiff1d(master_table, canvas_table)
        not_in_master_list = np.setdiff1d(canvas_table, master_table)
        if (len(not_in_master_list) > 0):
            print('The following tables are not in our master list:')
            print(not_in_master_list)
            print(' ')
        
        if (len(not_in_canvas_list) > 0):
            print('The following tables are not in the Canvas list:')
            print(not_in_canvas_list)
            print(' ')    
    
    
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------



# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def sync_data_from_canvas():
    print('---------')
    print('Lets Sync Data From Canvas ')
    print('---------')
    command = 'canvasDataCli sync -c /data/informatica/canvas/config.js'
    # subprocess.run(command, shell='true') 
    subprocess.call(command, shell='true') 
    
    
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------





# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def get_canvas_table_list():
    json_file_path = '/data/informatica/canvas/CanvasFiles/schema.json'
    
    with open(json_file_path) as f:
        canvasschema = json.load(f)
    
    # for table in canvasschema['schema']:   
        # canvas_table.append(table)    
    
    # canvas_table = list(canvasschema['schema'].keys())
    return sorted(list(canvasschema['schema'].keys()))

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

