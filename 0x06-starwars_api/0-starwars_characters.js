#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/';
const movieID = process.argv[2];

function getChar (url, i) {
  if (url.length === i) {
    return;
  }
  request({ uri: url[i], json: true }, (error, respone) => {
    if (error) {
      console.log(error);
    } else {
      console.log(respone.body.name);
      getChar(url, i + 1);
    }
  });
}

request({ uri: `${url}films/${movieID}`, json: true }, (error, respone) => {
  if (error) {
    console.log(error);
  } else {
    const charLst = respone.body.characters;
    getChar(charLst, 0);
  }
});
