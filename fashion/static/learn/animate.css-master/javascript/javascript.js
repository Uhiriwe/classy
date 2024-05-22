const newstring=(str)=>
 	str.length<3 ? str:str.slice(0,3)+str.slice(-3);
 	console.log(newstring('abc'));
 	console.log(newstring('abcdef'));
 	console.log(newstring('abc123abc123'));
 	console.log(newstring('ab'));



