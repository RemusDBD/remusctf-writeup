import socket
import time

def send_answer(sock, answer):
    sock.send((answer + "\n").encode())

def receive_question(sock):
    return sock.recv(1024).decode().strip()

def play_game(sock):
    while True:
        question = receive_question(sock)
        if not question:
            break

        print(question)
        time.sleep(1)  # Delay to simulate human response time

        # Parse question to determine answer
        scenarios = question.split(", ")
        answer = ""
        for scenario in scenarios:
            if "GORGE" in scenario:
                answer += "STOP-"
            elif "PHREAK" in scenario:
                answer += "DROP-"
            elif "FIRE" in scenario:
                answer += "ROLL-"

        answer = answer.rstrip("-")  # Remove trailing dash
        print(f"What do you do? {answer}")

        # Send answer to server
        send_answer(sock, answer)
        time.sleep(1)  # Delay between sending answers

if __name__ == "__main__":
    HOST = '83.136.254.16'  # Change to the appropriate IP address
    PORT = 30083

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        banner = s.recv(1024).decode()
        print(banner)

        ready = input("Are you ready? (y/n): ")
        if ready.lower() == 'y':
            s.send(b'y\n')
            play_game(s)
        else:
            print("Exiting game.")
