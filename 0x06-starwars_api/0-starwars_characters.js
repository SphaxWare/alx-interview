#!/usr/bin/node

const request = require('request');

// Recursive function to request character names
const req = (arr, i) => {
  if (i === arr.length) return; // Base case: when all characters are processed
  request(arr[i], (err, response, body) => {
    if (err) {
      throw err; // Handle error
    } else {
      console.log(JSON.parse(body).name); // Parse and log character name
      req(arr, i + 1); // Recursive call to process next character
    }
  });
};

// Initial request to get the film's characters
request(
  `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  (err, response, body) => {
    if (err) {
      throw err; // Handle error
    } else {
      const chars = JSON.parse(body).characters; // Parse characters array
      req(chars, 0); // Start recursive processing
    }
  }
);
