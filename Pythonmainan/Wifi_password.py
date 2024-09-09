import subprocess
def get_saved_wifi_profiles():

    command = 'netsh wlan show profile'
    result = subprocess.run (command, capture_output=True, text=True, shell=True)
    print (f"the result {result}\n")
    profiles = []

    for line in result.stdout.split("\n"):
        if "All User Profile" in line:
            profile_name = line.split(":")[1].strip()
            profiles.append (profile_name)
    return profiles

def get_wifi_password (profile_name):
    '''
    Get the Wi-fi password for a given profile name.
    '''
    command = f"netsh wlan show profile name=\"{profile_name}\" key=clear"
    result = subprocess.run (command, capture_output = True, text=True, shell=True)

    for line in result.stdout.split("\n"):
        if "Key Content" in line:
            return line.split (":")[1].strip()
        
    return None

def main():
    profiles = get_saved_wifi_profiles()
    if profiles:
        print (" Wifi Names Password: ")
        for profile in profiles:
            password = get_wifi_password(profile)
            print (f"{profile} : {password if password else 'password not found'}")
    else:
        print ("No wifi profiles found.")

if __name__ == "__main__":
    main()