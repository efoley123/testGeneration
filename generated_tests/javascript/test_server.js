// Import the necessary modules and mock them
jest.mock('http');
jest.mock('fs');

const http = require('http');
const fs = require('fs');

// Assuming the server code is in a file named `server.js`
const server = require('./server');

describe('Server and sendFile function tests', () => {
  let mockResponse;
  beforeEach(() => {
    // Setup for each test
    mockResponse = {
      end: jest.fn(),
    };
    fs.readFile.mockClear();
    http.createServer.mockClear();
    mockResponse.end.mockClear();
  });

  describe('sendFile function', () => {
    it('should send the file content on successful read', (done) => {
      const mockContent = 'file content';
      fs.readFile.mockImplementation((filename, callback) => {
        callback(null, mockContent);
      });

      // Mock response to assert it was called correctly
      const response = { end: jest.fn() };
      const filename = 'index.html';

      require('./server').sendFile(response, filename);

      process.nextTick(() => {
        expect(fs.readFile).toHaveBeenCalledWith(filename, expect.any(Function));
        expect(response.end).toHaveBeenCalledWith(mockContent, 'utf-8');
        done();
      });
    });

    it('should not send any content if an error occurs', (done) => {
      fs.readFile.mockImplementation((filename, callback) => {
        callback(new Error('Failed to read file'), null);
      });

      const response = { end: jest.fn() };
      const filename = 'nonexistent.html';

      require('./server').sendFile(response, filename);

      process.nextTick(() => {
        expect(fs.readFile).toHaveBeenCalledWith(filename, expect.any(Function));
        expect(response.end).not.toHaveBeenCalledWith(expect.any(String), 'utf-8');
        done();
      });
    });
  });

  describe('HTTP Server request handling', () => {
    it.each([
      ['/', 'index.html'],
      ['/index.html', 'index.html'],
      ['/style.css', 'style.css'],
      ['/bunnies.png', 'bunnies.png'],
    ])('should serve the file content for url %s', (url, expectedFile) => {
      const request = { url };
      const sendFile = jest.spyOn(require('./server'), 'sendFile');

      http.createServer.mockImplementation((requestListener) => {
        requestListener(request, mockResponse);
        return { listen: jest.fn() };
      });

      require('./server');

      expect(sendFile).toHaveBeenCalledWith(mockResponse, expectedFile);
    });

    it('should return 404 for unknown URLs', () => {
      const request = { url: '/unknown' };
      http.createServer.mockImplementation((requestListener) => {
        requestListener(request, mockResponse);
        return { listen: jest.fn() };
      });

      require('./server');

      expect(mockResponse.end).toHaveBeenCalledWith('404 Error: File Not Found');
    });
  });

  // Add more tests as necessary to cover edge cases and other scenarios
});