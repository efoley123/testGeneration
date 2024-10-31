const http = require('http');
const fs = require('fs');
jest.mock('http');
jest.mock('fs');

const server = require('./server');

describe('Server and sendFile function tests', () => {
  let mockResponse;
  beforeEach(() => {
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

      const response = { end: jest.fn() };
      const filename = 'index.html';

      server.sendFile(response, filename);

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

      server.sendFile(response, filename);

      process.nextTick(() => {
        expect(fs.readFile).toHaveBeenCalledWith(filename, expect.any(Function));
        expect(response.end).not.toHaveBeenCalledWith(expect.any(String), 'utf-8');
        done();
      });
    });

    it('should handle null data gracefully', (done) => {
      fs.readFile.mockImplementation((filename, callback) => {
        callback(null, null);
      });

      const response = { end: jest.fn() };
      const filename = 'emptyfile.html';

      server.sendFile(response, filename);

      process.nextTick(() => {
        expect(fs.readFile).toHaveBeenCalledWith(filename, expect.any(Function));
        expect(response.end).toHaveBeenCalledWith('', 'utf-8');
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
      const sendFile = jest.spyOn(server, 'sendFile');

      http.createServer.mockImplementation((requestListener) => {
        requestListener(request, mockResponse);
        return { listen: jest.fn() };
      });

      server.init(); // Assuming there's an init function to start the server

      expect(sendFile).toHaveBeenCalledWith(mockResponse, expectedFile);
    });

    it('should return 404 for unknown URLs', () => {
      const request = { url: '/unknown' };
      http.createServer.mockImplementation((requestListener) => {
        requestListener(request, mockResponse);
        return { listen: jest.fn() };
      });

      server.init(); // Assuming there's an init function to start the server

      expect(mockResponse.end).toHaveBeenCalledWith('404 Error: File Not Found');
    });

    it('should handle server creation failure gracefully', () => {
      http.createServer.mockImplementation(() => {
        throw new Error("Server creation failed");
      });

      expect(() => server.init()).toThrow("Server creation failed");
    });
  });

  // Additional tests for edge cases and failure scenarios
});