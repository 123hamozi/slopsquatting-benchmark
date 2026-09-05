const controller = new AbortController();
const request = new Request("https://example.com", { signal: controller.signal });

console.log(request.url);
