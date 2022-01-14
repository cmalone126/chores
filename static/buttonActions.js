function choreComplete(id){
	let baseHTML = "https://10.0.0.205/services/chores/complete/";
	let callHTML = baseHTML + id;
	fetch(callHTML, {
		method: "POST"
		}).then(res => {
		console.log("Delete succeeded for id: " + id);
	});

	//Refresh the page
	location.reload()
}