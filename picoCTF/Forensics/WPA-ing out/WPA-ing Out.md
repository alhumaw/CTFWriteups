# WPA-ing Out

# Description

I thought that my password was super-secret, but it turns out that passwords passed over the AIR can be CRACKED, especially if I used the same wireless network password as one in the rockyou.txt credential dump.
Use this 'pcap file' and the rockyou wordlist. The flag should be entered in the picoCTF{XXXXXX} format.

# Hints

Finding the IEEE 802.11 wireless protocol used in the wireless traffic packet capture is easier with wireshark, the JAWS of the network.

Aircrack-ng can make a pcap file catch big air...and crack a password.

# Solution

This challenge involved knowing how to utilize aircrack-ng. Aircrack-ng is a widely-used network security tool that is primarily used for assessing the security of Wi-Fi networks.
Aircrack-ng provides multiple capabilities: packet capture, password cracking, and analysis of network vulnerabilities.

For this challenge in particular, we were tasked with utilizing aircrack-ng to crack the WPA password, in turn, decrypting all packets within the pcap file.
Here is the command which will crack the pcap WIDE open:

aircrack-ng -w rockyou.txt wpa-ing_out.pcap

The password we found was: mickeymouse.

This was the flag, but we can utilize this password to decrypt the pcap file if we wanted to!

In Wireshark, let's input our cracked password:

Edit->Preferences->Protocols->IEEE 802.11->Edit Decryption Keys->wpa-pwd->mickeymouse

Once done, all the traffic that was previously encrypted should be in cleartext.
