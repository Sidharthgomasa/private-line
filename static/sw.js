// Minimal Service Worker to make the app installable
self.addEventListener('install', (e) => {
  console.log('[Service Worker] Install');
});

self.addEventListener('fetch', (e) => {
  // Just pass requests through (no offline caching for now)
  e.respondWith(fetch(e.request));
});
