# A beginner Python project that reads a server log file and extracts error entries. 
# It identifies lines containing ERROR, collects the date and platform information, 
# and displays the errors along with their total count. 
# The script also handles cases where the input file cannot be found.
# Skills I applied: File handling, reading text files, loops, conditional statements (if/else), 
# exception handling (try/except), string methods (split), lists, tuples, f-strings.

def extract_errors(filename):
   
    error_list = []
    
    try:
        file = open(filename, 'r', encoding='utf-8')

        for line in file:

            if line.startswith('INFO'):
                continue

            if 'ERROR' in line:

                words = line.split()                
                date = words[0]
                platform = words[-1]
                error_record = (date, platform)
                error_list.append(error_record)
                
        file.close()
        
    except FileNotFoundError:
        print("Error: The file was not found. Please check the filename.")
        return []
        
    return error_list

print("Starting log analysis...")

found_errors = extract_errors('server_logs.txt')

if len(found_errors) > 0:
    print("Found critical errors:")
    
    for error in found_errors:
        date = error[0]
        platform = error[1]
        print(f"- Crash on {date} (Platform: {platform})")
        
    print(f"Total errors found: {len(found_errors)}")
else:
    print("No errors found or file is empty.")