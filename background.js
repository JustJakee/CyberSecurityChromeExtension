//This script listens for requests to websites that are in blocked_domains.js and blocks them.
chrome.browserAction.setBadgeText({ text: "ON" });
var enabled = true;
chrome.webRequest.onBeforeRequest.addListener(
	function (details) {
		return { cancel: enabled };
	},
	{ urls: blocked_domains },
	["blocking"]
);