-- For Use With FlyWithLua Plugin

-- load namespace
local socket = require("socket")
local json = require("json")

-- create a TCP socket and bind it to the local host, at any port
local server = assert(socket.bind("*", 1013))

-- find out which port the OS chose for us
local ip, port = server:getsockname()

-- print a message informing what's up
-- print("Please telnet to localhost on port " .. port)
-- print("After connecting, you have 10s to enter a line to be echoed")
-- loop forever waiting for clients

scenes={
    {name="scnSplash",
        obj={
            {
                name="bg",
                type="background",
                path="scnSplash_bg.png",
            },
            {
                name="bird",
                type="image",
                path="scnSplash_bird.png",
                x=0, 
                y=682,
            },
        }
    },
}

function OpenDU_loop()
  -- wait for a connection from any client
  local client = server:accept()
  -- make sure we don't block waiting for this client's line
  client:settimeout(10)
  -- receive the line
  local line, err = client:receive()
  -- if there was no error, send it back to the client
  local data = json.decode(scenes)
  
  if not err then client:send(data .. "\n") end
  -- done with client, close the object
  client:close()
end


do_often("OpenDU_loop()")