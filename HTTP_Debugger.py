import socket 
import ssl 
import os 
import platform
import time
import requests 
from timeit import default_timer as timer

host = None 
port = None 
s = socket.socket() #Creating a TCP/IP, IPv4 socket 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Setting socket flags to allow for client socket reusability without waiting for TIME_WAIT.


def main(): 
    global host 
    global port 
    print("""This is a socket HTTP/S connection test.
This program will test the connection to port 80 and 443 of a host.
Port 80 is used for HTTP and port 443 is used for HTTPS.
                                                                """)
    client_input = input("""Press Enter to continue or input any key to exit...
>>> """) 
    clear_terminal()
    client_input = client_input.replace(" ", "") #Removing spaces from input to beautify
    if client_input == "":
        print("Continuing...")
        del client_input #Deleting the input to prevent memory leaks.
        time.sleep(2)
        clear_terminal()
        start = True 
        while start == True:
            client_input = input("""Please give a valid host!
>>> """) 
            client_input = client_input.replace(" ", "")
            if client_input == "":
                print("You didn't input anything at all!")
                del client_input 
                time.sleep(2)
                clear_terminal()
                continue
            elif client_input != "" and len(client_input) <= 63: 
                clear_terminal()
                print("Let's see if your host is valid, please be patient...")
                if client_input[0:7] == "http://":
                    start_index = 0 
                    end_index = 7 
                    http_strip = client_input[:start_index] + client_input[end_index:]
                    del client_input 
                    time.sleep(2) 
                    client_input = http_strip
                    del http_strip 
                elif client_input[0:8] == "https://":
                    start_index = 0 
                    end_index = 8 
                    https_strip = client_input[:start_index] + client_input[end_index:]
                    del client_input
                    time.sleep(2)
                    client_input = https_strip
                    del https_strip 
                client_input = client_input.translate(str.maketrans("","", "/:"))
                #print(client_input) #Debugging
                host_test = True 
                while host_test == True: 
                    try:
                        test_URL = "https://" + client_input
                        connect_test = requests.get(test_URL)
                        if connect_test.status_code == 200: 
                            print("Okay! This is a valid host!")
                            time.sleep(2)
                            host = client_input 
                            host_test = False
                            start = False 
                        else: 
                            print("This is an invalid host, sorry. Maybe you had a typo!")
                            time.sleep(2)
                            clear_terminal()
                            host_test = False 
                    except requests.exceptions.ConnectionError: 
                        print("""The host isn't accepting connections, sorry...
Maybe you tried to access a restricted area or didn't type in your host correctly.""")
                        print(client_input) #Debugging
                        time.sleep(2)
                        clear_terminal()
                        host_test = False 
                    except requests.exceptions.MissingSchema: 
                        print("""Your input isn't testable as a host!
Maybe try adding a sub-domain(e.g. www)
or the top-level domain (e.g. .com,.edu,.org)""")
                        time.sleep(2)
                        clear_terminal()
                        host_test = False 
            elif len(client_input) > 63: 
                print("Due to DNS limitations your character count must be <= 63! I apologize!") 
                del client_input 
                time.sleep(2)
                clear_terminal()
                continue
        start = False
        clear_terminal()
        client_input = input("""Do you want to test the connection to port 80 or 443?
Enter 80 for HTTP or 443 for HTTPS.
>>> """)
        client_input = client_input.replace(" ", "")
        if client_input == "80":
            print("Testing connection to port 80...")
            time.sleep(2)
            clear_terminal()
            port_80_connect()
            del client_input 
            client_input = input("""Enter 80 to receive a HTTP response before closing connection.
Or enter anything else to close the connection.
>>> """)
            client_input = client_input.replace(" ", "")
            if client_input == "80":
                print("Receiving HTTP response...")
                time.sleep(2)
                clear_terminal()
                try:
                    response = requests.get(f'http://{host}')
                    print(f"HTTP response: {response.status_code}")
                    input(""" 
Press anything to continue to reponse content!
>>> """)
                    clear_terminal()
                    print(f"Response content: {response.content}")
                    input(""" 
Press anything to continue to reponse headers!
>>> """)
                    clear_terminal()
                    print(f"Response headers: {response.headers}")
                except requests.exceptions.RequestException:
                    print(f"Something went wrong while sending HTTP request!")
                input("""
Press or type anything to exit and close connection.
>>> """)
                clear_terminal()
                s.close() 
                print("Socket connection successfully closed!")
                time.sleep(1.5)
                start = True 
                clear_terminal()
                while start == True: 
                    client_input = input("""Do you want to test a connection again? (Y/N)
>>> """)
                    if client_input == 'Y' or client_input == 'y':
                        host = None 
                        start = False
                        clear_terminal()
                        main()
                    elif client_input == 'N' or client_input == 'n': 
                        start = False 
                        exit() 
                    else: 
                        print("Invalid input!")
                        clear_terminal() 
                        continue 
            else: 
                print("Closing connection...")
                s.close() #Closing the socket connection.
                time.sleep(2)
                clear_terminal()
                print("Connection closed.")
                start = True
                while start == True: 
                    client_input = input("""Do you want to test a connection again? (Y/N)
>>> """)
                    if client_input == 'Y' or client_input == 'y':
                        host = None
                        start = False
                        clear_terminal()
                        main()
                    elif client_input == 'N' or client_input == 'n': 
                        start = False 
                        exit() 
                    else: 
                        print("Invalid input!")
                        clear_terminal()
                        continue

        elif client_input == "443":
            print("Testing connection to port 443...")
            time.sleep(2)
            clear_terminal()
            port_443_connect()
            del client_input 
            client_input = input("""Enter 443 to receive a HTTPS response before closing connection.
Or enter anything else to close the connection.
>>> """)
            client_input = client_input.replace(" ", "")
            if client_input == "443":
                print("Receiving HTTPS response...")
                time.sleep(2)
                clear_terminal()
                try:
                    response = requests.get(f'https://{host}')
                    print(f"HTTPS response: {response.status_code}")
                    input(""" 
Press anything to continue to reponse content!
>>> """)
                    clear_terminal()
                    print(f"Response content: {response.content}")
                    input(""" 
Press anything to continue to reponse headers!
>>> """)
                    clear_terminal()
                    print(f"Response headers: {response.headers}")
                except requests.exceptions.RequestException:
                    print(f"The website doesn't support valid TLS.")
                input("""
Press or type anything to exit and close connection.
>>> """)
                clear_terminal()
                s.close() 
                print("Socket connection successfully closed!")
                time.sleep(1.5)
                start = True 
                clear_terminal()
                while start == True: 
                    client_input = input("""Do you want to test a connection again? (Y/N)
>>> """)
                    if client_input == 'Y' or client_input == 'y':
                        host = None 
                        start = False
                        clear_terminal()
                        main()
                    elif client_input == 'N' or client_input == 'n': 
                        start = False 
                        exit() 
                    else: 
                        print("Invalid input!")
                        continue
            else: 
                print("Closing connection...")
                s.close() #Closing the socket connection.
                time.sleep(2)
                clear_terminal()
                print("Connection closed.")
                time.sleep(1.5)
                start = True 
                while start == True: 
                    client_input = input("""Do you want to test a connection again? (Y/N)
>>> """)
                    if client_input == 'Y' or client_input == 'y':
                        host = None
                        start = False
                        clear_terminal()
                        main()
                    elif client_input == 'N' or client_input == 'n': 
                        start = False 
                        exit() 
                    else: 
                        print("Invalid input!")
                        clear_terminal()
                        continue
            
        else: 
            print("Invalid input. Please enter 80 or 443.")
            start = True 
            time.sleep(2)
            clear_terminal()
            while start == True: 
                client_input = input("""Do you want to test a connection again? (Y/N)
>>> """)
                if client_input == 'Y' or client_input == 'y':
                    host = None
                    start = False
                    main()
                elif client_input == 'N' or client_input == 'n': 
                    start = False 
                    exit() 
                else: 
                    print("Invalid input!")
                    continue
    else:
        print("Exiting...")
        time.sleep(1.5)
        exit()


def timefunc(func):
    def wrapper(*args, **kwargs):
        start = timer() 
        result = func(*args, **kwargs)
        end = timer()
        message = print(f"it took {end-start} seconds to form a connection.")
        message 
        return result 
    return wrapper

@timefunc #Wraps the connection function into the timefunc to time the connection
def port_80_connect(): 
    global s 
    global host #The web server's hostname or IP address. 
    s = socket.socket() #Resets socket state
    port = 80  
    result = s.connect_ex((host, port)) #Connects and returns error code (0 if successful).
    print(f"Result is {result}, if 0 this means a connection has been successfully formed!")
    if result == 0: #If the connection was successful, result will be 0.
        print(f"Connected to {host} on port {port}.")
    else: #If the connection failed, result will be non-zero.
        print(f"Failed to connect to {host} on port {port}.")


@timefunc
def port_443_connect():
    global s 
    global host 
    s = socket.socket()
    port = 443 
    ssl_context = ssl.create_default_context() #Create a default SSL context.
    result = s.connect_ex((host, port)) #Connect to the server on port 443.
    result
    s = ssl_context.wrap_socket(s, server_hostname=host) #Wrap the socket with SSL.
    print(f"""Result is {result}, if 0 this means a connection has been successfully formed!
          Connected to {host} on port {port}.
          And grabbed server's SSL certificate! 
          {s.getpeercert()}""")


def clear_terminal():
    # Check the operating system and clear the terminal accordingly
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux" or platform.system() == "Darwin": # For MacOS and Linux
        os.system("clear")
    else:
        print("\n" * 100) #For unindentified systems to get 100 new lines of code in terminal.


if __name__ == "__main__":
    print(main())
