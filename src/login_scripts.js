const axios = require("axios")
function login(){
    const token = document.getElementById('token').value;
    axios.get("http://localhost:5000/auth/token/"+token)
    .then( data => {
        const response = data.data;
        if( response.msg === 'GOOD_TOKEN')
        {
            const ps = response.data
            sessionStorage.setItem('token', token)
            sessionStorage.setItem('start_time', ps.start_time)
            sessionStorage.setItem('end_time', ps.end_time)
            sessionStorage.setItem('duration', ps.duration)
            sessionStorage.setItem('id', ps.id)
            sessionStorage.setItem('start_time', ps.start_time)
            sessionStorage.setItem('name', ps.name)

            window.location.href = 'lobby.html';
        }
        else if( response.msg === "BAD_TOKEN")
            alert("Token Probably Has Typos")
        else if( response.msg === "TOKEN_EXPIRE")
            alert("The Test has ended")
        else
            alert(response.msg)
    })
}