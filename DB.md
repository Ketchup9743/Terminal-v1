### Machine Name Declaration ###
machine_one = "Machine 1"
machine_two = "Machine 2"
machine_three = "Machine 3"
machine_four = "Machine 4"
### Port Name Declaration ###
port_one = 8800
port_two = 5000
port_three = 6600
port_four = 4300
### Memory / Storage Amount Declaration ###
total_memory = 512  ### Max Amount of RAM the machine can use ###
total_storage = 1032   ### Max Amount of Storage the machine can use ###
remaining_memory = 512
remaining_storage = 1032
print("")
print(f"                        Usage Statistics for {machine_one}:")
print("")
print("-----------------------------------------------------------------------------")
print("")
remaining_memory -= remaining_memory - 16
remaining_storage -= remaining_storage - 64
print(f"MEMORY USAGE - 16GB (REMAINING MEMORY - {remaining_memory}GB)")
print(f"STORAGE USAGE - 64GB (REMAINING STORAGE - {remaining_storage}GB)")
print("")
### Machine Two Program ###
print("=============================================================================")
print("")
print(f"                        Usage Statistics for {machine_two}:")
print("")
print("-----------------------------------------------------------------------------")
print("")
remaining_memory -= remaining_memory - 16
remaining_storage -= remaining_storage - 64
print(f"MEMORY USAGE - 48GB (REMAINING MEMORY - {remaining_memory}GB)")
print(f"STORAGE USAGE - 32GB (REMAINING STORAGE - {remaining_storage}GB)")
print("")
### Machine Three Program ###
print("=============================================================================")
print("")
print(f"                        Usage Statistics for {machine_three}:")
print("")
print("-----------------------------------------------------------------------------")
print("")
remaining_memory -= remaining_memory - 16
remaining_storage -= remaining_storage - 64
print(f"MEMORY USAGE - 128GB (REMAINING MEMORY - {remaining_memory}GB)")
print(f"STORAGE USAGE - 128GB (REMAINING STORAGE - {remaining_storage}GB)")
print("")
print("=============================================================================")
### Machine Four Program ###
print("")
print(f"                        Usage Statistics for {machine_four}:")
print("")
print("-----------------------------------------------------------------------------")
print("")
remaining_memory -= remaining_memory - 16
remaining_storage -= remaining_storage - 64
print(f"MEMORY USAGE - 64GB (REMAINING MEMORY - {remaining_memory}GB)")
print(f"STORAGE USAGE - 256GB (REMAINING STORAGE - {remaining_storage}GB)")
print("")
print("=============================================================================")
### Program Summary ###
used_memory = total_memory - remaining_memory
used_storage = total_storage - remaining_storage
print('')
print("                               USAGE SUMMARY:")
print("")
print("-----------------------------------------------------------------------------")
print("")
print(f'MEMORY USED - {used_memory}GB')
print(f'MEMORY REMAINING - {remaining_memory}GB')
print("")
print('------------------------------------------------------------------------------')
print("")
print(f'STORAGE USED - {used_storage}GB')
print(f'STORAGE REMAINING - {remaining_storage}GB')
print("")