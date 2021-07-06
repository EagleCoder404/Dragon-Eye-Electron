
function next(id){
	var num=id.charAt(id.length-1);
	var fin=id.split(num)[0]+(parseInt(num)+1);
	document.getElementById(id).style.visibility="hidden";
	document.getElementById(fin).style.visibility="visible";
	
}

function createStudentApi(token){
	const axios = require("axios");
	const axios_instance = axios.create({
		baseURL: "http://dragon-eye.herokuapp.com/session",
		headers:{
			'Authorization': `Bearer ${token}`
		}
	});
	return axios_instance
}

function runPython(path, args){
    const {PythonShell} = require("python-shell")

    let options = {
        args: args
      };
	  
	PythonShell.run(path, options, function (err, results) {
		if (err){ ; console.log(results); throw err;}
		console.log(results);
	});
}