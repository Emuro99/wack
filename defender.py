import subprocess
import time

def check_antivirus_status():
    # het commando om de Antivirus status op te halen
    powershell_command = r"Get-MpComputerStatus | Select-Object -ExpandProperty RealTimeProtectionEnabled"

    # Voer het PowerShell-commando uit
    result = subprocess.run(["powershell", "-Command", powershell_command], capture_output=True, text=True)

    
    if result.returncode == 0:
        antivirus_enabled = result.stdout.strip()
        if antivirus_enabled.lower() == 'true':
            print("Antivirus is ingeschakeld.")
        elif antivirus_enabled.lower() == 'false':
            print("Antivirus is uitgeschakeld.")
        else:
            print("Kan antivirusstatus niet bepalen.")
    else:
        print("Fout bij het uitvoeren van het PowerShell-commando.")

def turn_antivirus_off():
    # het commando om de Anti virus uit te zetten.
    powershell_command = r"Set-MpPreference -DisableRealtimeMonitoring $true"

    try:
        subprocess.run(["powershell", "-command", powershell_command])
    except:
        print("Fout bij het uitvoeren van het PowerShell-commando.")
