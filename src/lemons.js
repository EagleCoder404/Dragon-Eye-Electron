
function next(id){
	var num=id.charAt(id.length-1);
	var fin=id.split(num)[0]+(parseInt(num)+1);
	document.getElementById(id).style.visibility="hidden";
	document.getElementById(fin).style.visibility="visible";
	
}