#!/usr/bin/node

const request = require('request');

request(
  `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  (error, response, body) => {
    if (error) throw error;
    else {
      print_char(JSON.parse(body).characters, 0);
    }
  }
);

function print_char (person, idx) {
  if (idx >= person.length) {
    return;
  }
  request(person[idx], (error, response, body) => {
    if (error) throw error;
    else {
      console.log(JSON.parse(body).name);
      return print_char(person, ++idx);
    }
  });
}
