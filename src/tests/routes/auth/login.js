const axios = require('axios')


// what the fuck await have to be used in a async function


/**
const res = await axios.post('http://127.0.0.1:5000/login', {

 auth : {

		username : 'goopho',
		password: '123456'
 }

});

res.status; //200

 **/


axios({
  url: 'http://127.0.0.1:5000/login',
  method: 'post',
  auth: {
		  username : 'goopho',
		  password : '123456'
  }
})
