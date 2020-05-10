var config = {
    mode: "fixed_servers",
    rules: {
        singleProxy: {
            scheme: "http",
            host: "%(ip) s",
            port: % (port) s
        }
    }
}

chrome.proxy.settings.set({
    value: config,
    scope: "regular"
}, function () {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%(username) s",
            password: "%(password) s"
        }
    }
}

chrome.webRequest.onAuthRequired.addListener(
    callbackFn, {
        urls: ["<all_urls>"]
    },
    ['blocking']
)