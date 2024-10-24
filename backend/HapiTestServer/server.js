// Import the Hapi module to create a server
const Hapi = require('@hapi/hapi');

// Create a new Hapi server instance + define the server's connection settings (host and port)
const server = Hapi.server({
    host: 'localhost',  // Set the host to 'localhost'
    port: 3000          // Set the port to 3000
});

// Define a route that will handle incoming HTTP GET requests to the root URL ('/')
server.route({
    method: 'GET',   // HTTP method (GET request)
    path: '/',       // URL path ('/' for the root)
    handler: (request, h) => {  // Define the handler function for this route
        return 'TEST';  // Respond with the string 'TEST' when this route is accessed
    }
});


// Start the server and handle any potential errors
const init = async () => {
    try {
        await server.start();  // Start the server
        console.log('Server running at:', server.info.uri);  // Log the server URI on success
    } catch (err) {
        console.error(err);  // Log errors if the server fails to start
        process.exit(1);  // Exit the process with a failure code
    }
}
//initialize server
init();