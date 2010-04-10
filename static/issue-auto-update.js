function updateStatus(code) {
	if (code == 1) {
		$("#op").attr("checked", "true");
	} else if (code == 2) {
		$("#og").attr("checked", "true");
	} else if (code == 4) {
		$("#c").attr("checked", "true");
	}
}

function updateAssigned(assignedTo) {
	$("#assigninput").attr("value", assignedTo);
}

function pull() {
	$.get(BASE_URL+'issuejson/'+ID+'/', function(data) {
		var issue = eval('(' + data + ')');
		//alert(issue.description);
		$("#desc").html(issue.description.replace("\\\\n", "cow"));
		$("#touched").html("Last Touched: " + issue.touched)
		log(overwriteInput == 1);
		log(lastUpdated + 300 < new Date().getTime());
		log(lastUpdated + 300 < new Date().getTime() || overwriteInput == 1);
		if (lastUpdated + 300 > new Date().getTime() || overwriteInput == 1) {
			log("cows2");
			updateStatus(issue.status);
			updateAssigned(issue.assigned);
			overwriteInput = 1;
		}
		//alert("it works");
	});
}

function noinputOverwrite (data) {
	log("cows");
	overwriteInput = 0;
	lastUpdated = new Date().getTime();
}

var overwriteInput = 1;
var lastUpdated = new Date().getTime();

function init() {
	$("input").bind("focusin", noinputOverwrite);
	$("textarea").bind("focusin", noinputOverwrite);
	$("input").bind("select", noinputOverwrite);
	setInterval(pull,1500);
}

var dont_log = true;
function log(what) {
	if( dont_log && typeof console != 'object')
		return;
	dont_log = false;
	console.log(what);
}
function dir(what) {
	if( dont_log && typeof console != 'object')
		return;
	dont_log = false;
	console.dir(what);
}

