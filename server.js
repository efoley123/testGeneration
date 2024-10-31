const http = require('http'),
      fs   = require('fs'),
      port = 3000

const sendFile = function( response, filename ) {
   fs.readFile( filename, function( err, content ) {
     response.end( content, 'utf-8' )
   })
}

const server = http.createServer( function( request,response ) {
  switch( request.url ) {
    case '/':
      sendFile( response, 'index.html' )
      break
    case '/index.html':
      sendFile( response, 'index.html' ) //comment added here
      break
    case '/style.css':
      sendFile(response, 'style.css')
      break
    case '/bunnies.png':
      sendFile(response,'bunnies.png')
      break
    default:
      response.end( '404 Error: File Not Found' )
  }
})

server.listen( process.env.PORT || port )


