#!/usr/bin/node
const requests_ = require('request');
const URL_API = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  requests_(`${URL_API}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const charURL = JSON.parse(body).characters;
    const charName = charURL.map(
      url => new Promise((resolve, reject) => {
        requests_(url, (promiseErr, __, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
          }
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

    Promise.all(charName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
