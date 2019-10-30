window.onload = function () {
	function updateLabel() {
		var enabled = chrome.extension.getBackgroundPage().enabled;
		document.getElementById('toggle_button').value = enabled ? "Turn Off" : "Turn On";
	}
	//changing status of button
	document.getElementById('toggle_button').onclick = function () {
		var background = chrome.extension.getBackgroundPage();
		background.enabled = !background.enabled;
		if (document.getElementById('toggle_button').value == "Turn Off") {
			chrome.browserAction.setBadgeText({ text: "OFF" });
		}
		else if (document.getElementById('toggle_button').value == "Turn On") {
			chrome.browserAction.setBadgeText({ text: "ON" });
		}
		updateLabel();
	};
	updateLabel();
}