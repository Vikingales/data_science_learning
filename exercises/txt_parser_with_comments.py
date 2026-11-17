def extract_errors(filename):
    # Create empty list to collect errors
    error_list = []
    
    # Use try/except, to prevent program fail, if there's no errors
    try:
        file = open(filename, 'r', encoding='utf-8')
        
        # Iterate file lines with cycle for
        for line in file:
            
            # string methods and conditionals
            # If string starts with INFO, skip it with continue
            if line.startswith('INFO'):
                continue
            
            # If there's word ERROR in line, process it
            if 'ERROR' in line:
                # Split the string into a list of words based on spaces
                # example: ['2026-11-10', '10:05', 'ERROR', 'App', 'crashed', 'on', 'Android']
                words = line.split()
                
                # Take the date (first word, index 0)
                date = words[0]
                # Take the platform (last word, index -1)
                platform = words[-1]
                
                # Make tuple
                error_record = (date, platform)
                
                # Add tuple into the list
                error_list.append(error_record)
                
        file.close()
        
    except FileNotFoundError:
        print("Error: The file was not found. Please check the filename.")
        return [] # return empty list in case of mistake
        
    return error_list

# --- Main part ---

print("Starting log analysis...")

# Call function with file name
found_errors = extract_errors('server_logs.txt')

# Check if we find smth
if len(found_errors) > 0:
    print("Found critical errors:")
    
    # Cycle for to see result
    for error in found_errors:
        date = error[0]
        platform = error[1]
        print(f"- Crash on {date} (Platform: {platform})")
        
    print(f"Total errors found: {len(found_errors)}")
else:
    print("No errors found or file is empty.")