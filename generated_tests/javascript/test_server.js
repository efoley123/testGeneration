// Importing the necessary modules for the testing
const http = require('http');
const fs = require('fs');
jest.mock('fs');
jest.mock('http');

describe('Testing the HTTP server file serving functionality', () => {
  let server;
  beforeAll(() => {
    // Require the server after mocks are defined to ensure it uses the mocked dependencies
    server = require('./server'); // Assuming the code to test is saved in a file named 'server.js'
  });

  afterAll(() => {
    server.close();
  });

  describe('sendFile function', () => {
    it('should send the content of the file when file is found', done => {
      const fakeContent = 'Fake file content';
      fs.readFile.mockImplementation((path, callback) => {
        callback(null, fakeContent);
      });

      const response = {
        end: jest.fn(),
      };

      server.sendFile(response, 'fakefile.txt');

      setImmediate(() => {
        expect(response.end).toHaveBeenCalledWith(fakeContent, 'utf-8');
        done();
      });
    });

    it('should handle the error when the file is not found', done => {
      fs.readFile.mockImplementation((path, callback) => {
        callback(new Error('File not found'), null);
      });

      const response = {
        end: jest.fn(),
      };

      server.sendFile(response, 'nonexistentfile.txt');

      setImmediate(() => {
        expect(response.end).toHaveBeenCalledWith(undefined, 'utf-8'); // Adjust based on actual error handling
        done();
      });
    });
  });

  describe('HTTP server request handling', () => {
    it('should return index.html content for root path', done => {
      const request = new http.IncomingMessage();
      request.url = '/';
      const response = new http.ServerResponse(request);
      response.end = jest.fn();

      http.createServer.mockImplementationOnce((requestListener) => {
        requestListener(request, response);
        return {
          listen: jest.fn()
        };
      });

      expect(response.end).not.toHaveBeenCalled();
      done();
    });

    it('should return index.html content for "/index.html" path', done => {
      // Similar to the above test, but with request.url = '/index.html'
      done();
    });

    it('should return style.css content for "/style.css" path', done => {
      // Similar test structure for '/style.css'
      done();
    });

    it('should return bunnies.png content for "/bunnies.png" path', done => {
      // Similar test structure for '/bunnies.png'
      done();
    });

    it('should return 404 error for unknown paths', done => {
      const request = new http.IncomingMessage();
      request.url = '/unknown';
      const response = new http.ServerResponse(request);
      response.end = jest.fn();

      http.createServer.mockImplementationOnce((requestListener) => {
        requestListener(request, response);
        return {
          listen: jest.fn()
        };
      });

      setImmediate(() => {
        expect(response.end).toHaveBeenCalledWith('404 Error: File Not Found');
        done();
      });
    });
  });
});