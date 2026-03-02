const axios = require('axios');

axios.get('https://api.github.com')
  .then(response => {
    console.log(`Статус відповіді GitHub API: ${response.status}`);
  })
  .catch(error => {
    console.error(error);
  });