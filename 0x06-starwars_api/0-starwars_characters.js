#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/';
const movieID = process.argv[2];

request({ uri: `${url}films/${movieID}`, json: true }, (error, respone) => {
  if (error) {
    console.log(error);
  } else {
    const charLst = respone.body.characters;
    charLst.forEach(el => {
      request({ url: el, json: true }, (error, respone) => {
        if (error) {
          console.log(error);
        } else {
          console.log(respone.body.name);
        }
      });
    });
  }
});
