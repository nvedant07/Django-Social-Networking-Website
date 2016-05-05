
function func()
{
var li1 = document.getElementById("link1");
var li2 = document.getElementById("link2");
var output=document.getElementById("out");

li1.addEventListener("input",fn);
li2.addEventListener("input",fn);
	function fn(){
		var l1 = link1.value;
		var l2 = link2.value;
		output.innerHTML = l1+l2;

	}
	 
}