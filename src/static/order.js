function select_restaurant_changed(){
	selectedID=$("#select_restaurant").val();
	fillRestaurant(selectedID);
}

function fillRestaurant(id){
	dateSelector=$("#select_date");
	dateSelector.html("");
	$.getJSON('ajax/test.json', function(data) {
		var i=0;
		while(i<data.length){
			item=data[i];
			dateSelector.append("<option id='"+item.id+"'>"+item.Name+"</option>");
			i=i+1;
		}
	
	});

}