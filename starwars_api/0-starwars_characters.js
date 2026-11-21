#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const characters = JSON.parse(body).characters;

  function printCharacter(index) {
    if (index >= characters.length) {
      return;
    }

    request(characters[index], (err, res, data) => {
      if (err) {
        console.error(err);
        return;
      }

      const character = JSON.parse(data);
      console.log(character.name);

      printCharacter(index + 1);
    });
  }

  printCharacter(0);
});