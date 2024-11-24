import socket
import time
import argparse

HOST = "101.35.209.40"
PORT = 1088

# the message returned by server if the number is invalid
INVALID_MESSAGE = "你喂的太多了，小鹿们吃不下了"


def connect_to_server(host, port, timeout):
    """
    connect to server and return the socket
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((host, port))
        return s
    except socket.error:
        return None


def send_y_and_discard_response(s):
    """
    send "y" to server and receive the reponse
    """
    try:
        # receive the initial prompt
        _ = receive_full_response(s, timeout=0)

        # send "y"
        s.sendall(b"y\n")

        # receive the prompt of inputing number
        _ = receive_full_response(s, timeout=0)

    except socket.error:
        return False
    return True


def send_number(s, number):
    """
    send to number to server
    """
    try:
        s.sendall(f"{number}\n".encode())
    except socket.error:
        return False
    return True


def receive_full_response(s, timeout):
    """
    receive the response in loop, ensure the response is fully received
    """
    s.settimeout(timeout)
    response = ""
    while True:
        try:
            data = s.recv(4096)
            if not data:
                # the connection is end
                break
            response += data.decode("utf-8", errors="ignore")
        except socket.timeout:
            # timeout
            break
        except socket.error:
            # other errors
            break
    return response.strip()


def receive_number_response(s, timeout):
    """
    receive the response after inputing number
    """
    response = receive_full_response(s, timeout)
    return response


def binary_search_threshold(
    host, port, initial_low, initial_high, connect_timeout, response_timeout
):
    """
    use binary search to find number
    """
    low = initial_low
    high = initial_high
    threshold = -1
    attempts = 0

    while low <= high:
        mid = (low + high) // 2
        attempts += 1

        print(f"Attempt times: {attempts}\nNumber:\n{mid}")

        s = connect_to_server(host, port, connect_timeout)
        if not s:
            print("Fail to connect to server! Retry after 2 second.")
            time.sleep(2)
            continue

        try:
            success = send_y_and_discard_response(s)
            if not success:
                s.close()
                print('Fail to send "y"! Retry after 2 second.')
                time.sleep(2)
                continue

            success = send_number(s, mid)
            if not success:
                s.close()
                print("Fail to send number! Retry after 2 second.")
                time.sleep(2)
                continue

            response = receive_number_response(s, response_timeout)

            if response:
                if INVALID_MESSAGE in response:
                    high = mid - 1
                    print(
                        f"Too bigger.\nThreshold is updated to:\n{threshold}\nContinue to find smaller number.\n"
                    )
                else:
                    threshold = mid
                    low = mid + 1
                    print(
                        f"Too low.\nThreshold is updated to:\n{threshold}\nContinue to find bigger number.\n"
                    )
            else:
                threshold = mid
                low = mid + 1
                print(
                    f"Too low.\nThreshold is updated to:\n{threshold}\nContinue to find bigger number.\n"
                )

        finally:
            s.close()
            # Wait a second and try another time.
            time.sleep(1)

    return threshold


def main():
    """
    main function. Start to find the number.
    """
    parser = argparse.ArgumentParser(
        description="Use binary search to find the number."
    )
    parser.add_argument(
        "--connect-timeout",
        type=int,
        default=1,
        help="The waiting time for connecting server. Default to 1 second.",
    )
    parser.add_argument(
        "--response-timeout",
        type=int,
        default=1,
        help="The waiting time for getting response from server. Default to 1 second.",
    )
    parser.add_argument(
        "--low",
        type=int,
        default=16000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
        help="The low of range.",
    )
    parser.add_argument(
        "--high",
        type=int,
        default=17000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
        help="The high of range.",
    )
    args = parser.parse_args()

    print(
        f"----------Binary Search Start----------\nLow: {args.low}\nHigh: {args.high}\n"
    )

    threshold = binary_search_threshold(
        HOST, PORT, args.low, args.high, args.connect_timeout, args.response_timeout
    )

    if threshold != -1:
        print(f"Find the number:\n{threshold}")
        print(f"Time: {time.ctime()}")
    else:
        print("Could find the number!")


if __name__ == "__main__":
    print(f"Time: {time.ctime()}")
    main()
