#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId + '/';

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const characters = JSON.parse(body).characters;
  let index = 0;

  function printCharacter () {
    if (index >= characters.length) {
      return;
    }

    request(characters[index], function (error, response, body) {
      if (error) {
        console.error(error);
        return;
      }

      console.log(JSON.parse(body).name);
      index++;
      printCharacter();
    });
  }

  printCharacter();
});
