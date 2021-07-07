

function configure(){
	document.getElementById("config").innerHTML="Hang On...";
    const {PythonShell} = require("python-shell")
    let options = {
        args: ['Abhilash']
      };
      
      PythonShell.run('src/configuration.py', options, function (err, results) {
        if (err) throw err;
        console.log(results);
		if(results[results.length-1]==="success"){
			document.getElementById("config").innerHTML="SUCCESS"
			document.getElementById("config").style.backgroundcolor="green"
			swal("DEPENDENCIES INSTALLED SUCCESSFULLY");
			document.getElementById("config").style.visibility="hidden";
			document.getElementById("tick1").src="checked.png";
			document.getElementById('tick1div').style.boxshadow="0px 4px 8px 0px green";
		}else{
			var message="PLEASE INSTALL THESE PACKAGES MANUALLY\n";
			for(var i=0;i<results.length-2;i++){
				message=message+results[i]+"\n"
			}
			swal(message);	
		}
      });
}

function training(){
	if(document.getElementById("config").style.visibility!="hidden"){
		swal("COMPLETE STEP 1 TO PROCEED FURTHER.")

	}else{
	document.getElementById("face").innerHTML="Hang On...";
    const {PythonShell} = require("python-shell")
    let options = {
        args: ['Abhilash']
      };
      
      PythonShell.run('facial/training.py', options, function (err, results) {
        if (err) throw err;
        console.log(results);
		document.getElementById("face").style.visibility="hidden";
		swal("FACE MODEL SUCCESSFULLY CREATED.")
		document.getElementById("tick2").src="checked.png";
		document.getElementById('tick2div').style['boxshadow']="0px 4px 8px 0px green";
		document.getElementById("facemess").innerHTML=">> 1400 face instances captured and model is successfully trained..."
      });
	}

}
