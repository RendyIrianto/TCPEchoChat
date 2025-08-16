````markdown
# TCP Echo Chat

A simple multi-client chat app using Python sockets.

## How to Use

1. Start the server:
   ```bash
   python3 server.py
````

2. Start a client (in another terminal):

   ```bash
   python3 client.py
   ```

3. Enter your name and chat. Messages are broadcast to everyone.

4. Type `exit` (or `/exit` or `/quit`) to leave.
   Press `Ctrl+C` in the server terminal to stop the server.

## Notes

* Default host: `127.0.0.1`
* Default port: `65432`
* Run the server first, then connect clients.

