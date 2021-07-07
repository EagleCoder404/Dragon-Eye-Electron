const axios = require("axios")
const path = require("path");

const Datastore = require("nedb")
const db = new Datastore({filename:"sessions.db", autoload:true})


function login(){
    const token = document.getElementById('token').value;
    const backend = createStudentApi(token)
    backend.interceptors.response.use(undefined, err => {
        const error = err.response;
        if (error.status===401)
            swal("Authentication Error")
        });
    backend.get("http://dragon-eye.herokuapp.com/auth/token")
    .then( data => {
        const response = data.data;
        if( response.msg === 'GOOD_TOKEN')
        {

            db.find({_id:token},(err, docs) => {
                if (docs.length == 0)
                    db.insert({_id:token, configured:false})
            })

            const ps = response.data
            sessionStorage.setItem('token', token)
            sessionStorage.setItem('start_time', ps.start_time)
            sessionStorage.setItem('end_time', ps.end_time)
            sessionStorage.setItem('duration', ps.duration)
            sessionStorage.setItem('id', ps.id)
            sessionStorage.setItem('start_time', ps.start_time)
            sessionStorage.setItem('name', ps.name)
            
            if(ps.submitted === true)
            {
                
                swal("You have submitted already");
                return;
            }
            window.location.href = 'lobby.html';
        }
        else if( response.msg === "BAD_TOKEN")
            swal("Token Probably Has Typos")
        else if( response.msg === "TOKEN_EXPIRE")
            swal("The Test has ended")
        else
            swal(response.msg)
    }).catch( r => console.log(r) )
    
	document.getElementById("lobby").style.display="block";
}