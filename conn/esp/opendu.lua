-- For Use With FSUIPC

socket = require("socket");

-- Set the host name to the name of the PC running this Server
host = "*";

-- The port must match the port selected in the client and not clash with others.
port = "1013";


local function processdata(command)

	

end

server = assert(socket.bind(host, port));
ack = "it works\n";
while 1 do
    print("server: waiting for client connection...");
    control = server:accept();
    if control ~= nil then
    		print("server: client connected!");
    		while 1 do 
        		command = control:receive();
        		if command == nil then
            		print("server: client disconnected");
            		ipc.control(65794) -- Pause FS
             		break
        		end
        		assert(control:send(ack));       		
        		processdata(command)
    		end
    end
end