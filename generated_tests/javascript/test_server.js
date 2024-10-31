const http = require('http');
const fs = require('fs');

jest.mock('fs');
jest.mock('http');

describe('Testing the HTTP server file serving functionality', () => {
  let server;

  beforeAll(() => {
    server = require('./server');
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
        expect(response.end).toHaveBeenCalledWith('Error: File not found', 'utf-8');
        done();
      });
    });
  });

  describe('HTTP server request handling', () => {
    beforeEach(() => {
      http.createServer.mockClear();
    });

    it('should return index.html content for root path', done => {
      const request = new http.IncomingMessage();
      request.url = '/';
      const response = new http.ServerResponse(request);
      response.end = jest.fn();

      fs.readFile.mockImplementation((path, callback) => {
        if (path === 'index.html') {
          callback(null, 'index content');
        }
      });

      http.createServer.mockImplementationOnce((requestListener) => {
        requestListener(request, response);
        return { 
          listen: jest.fn() 
        };
      });

      server.listen();

      setImmediate(() => {
        expect(response.end).toHaveBeenCalledWith('index content', 'utf-8');
        done();
      });
    });

    it('should return index.html content for "/index.html" path', done => {
      const request = new http.IncomingMessage();
      request.url = '/index.html';
      const response = new http.ServerResponse(request);
      response.end = jest.fn();

      fs.readFile.mockImplementation((path, callback) => {
        if (path === 'index.html') {
          callback(null, 'index content');
        }
      });

      http.createServer.mockImplementationOnce((requestListener) => {
        requestListener(request, response);
        return {
          listen: jest.fn()
        };
      });

      server.listen();

      setImmediate(() => {
        expect(response.end).toHaveBeenCalledWith('index content', 'utf-8');
        done();
      });
    });

    it('should return style.css content for "/style.css" path', done => {
      const request = new http.IncomingMessage();
      request.url = '/style.css';
      const response = new http.ServerResponse(request);
      response.end = jest.fn();

      fs.readFile.mockImplementation((path, callback) => {
        if (path === 'style.css') {
          callback(null, 'css content');
        }
      });

      http.createServer.mockImplementationOnce((requestListener) => {
        requestListener(request, response);
        return { 
          listen: jest.fn() 
        };
      });

      server.listen();

      setImmediate(() => {
        expect(response.end).toHaveBeenCalledWith('css content', 'utf-8');
        done();
      });
    });

    it('should return bunnies.png content for "/bunnies.png" path', done => {
      const request = new http.IncomingMessage();
      request.url = '/bunnies.png';
      const response = new http.ServerResponse(request);
      response.end = jest.fn();

      fs.readFile.mockImplementation((path, callback) => {
        if (path === 'bunnies.png') {
          callback(null, 'png content');
        }
      });

      http.createServer.mockImplementationOnce((requestListener) => {
        requestListener(request, response);
        return {
          listen: jest.fn()
        };
      });

      server.listen();

      setImmediate(() => {
        expect(response.end).toHaveBeenCalledWith('png content', 'utf-8');
        done();
      });
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

      server.listen();

      setImmediate(() => {
        expect(response.end).toHaveBeenCalledWith('404 Error: File Not Found', 'utf-8');
        done();
      });
    });
  });
});