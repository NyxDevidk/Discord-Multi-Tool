// DMS Website - Service Worker
// Versão 2.0 - NYX DEV

const CACHE_NAME = 'dms-website-v2.0.0';
const STATIC_CACHE = 'dms-static-v2.0.0';
const DYNAMIC_CACHE = 'dms-dynamic-v2.0.0';

// Arquivos para cache estático
const STATIC_FILES = [
    '/',
    '/index.html',
    '/css/style.css',
    '/js/main.js',
    '/images/logo.svg',
    '/images/favicon.svg',
    '/manifest.json',
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css',
    'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap'
];

// Estratégia de cache: Cache First, Network Fallback
async function cacheFirst(request) {
    const cachedResponse = await caches.match(request);
    if (cachedResponse) {
        return cachedResponse;
    }
    
    try {
        const networkResponse = await fetch(request);
        if (networkResponse.ok) {
            const cache = await caches.open(DYNAMIC_CACHE);
            cache.put(request, networkResponse.clone());
        }
        return networkResponse;
    } catch (error) {
        // Retorna uma página offline se disponível
        if (request.destination === 'document') {
            return caches.match('/offline.html');
        }
        throw error;
    }
}

// Estratégia de cache: Network First, Cache Fallback
async function networkFirst(request) {
    try {
        const networkResponse = await fetch(request);
        if (networkResponse.ok) {
            const cache = await caches.open(DYNAMIC_CACHE);
            cache.put(request, networkResponse.clone());
        }
        return networkResponse;
    } catch (error) {
        const cachedResponse = await caches.match(request);
        if (cachedResponse) {
            return cachedResponse;
        }
        throw error;
    }
}

// Instalação do Service Worker
self.addEventListener('install', (event) => {
    console.log('[SW] Installing Service Worker...');
    
    event.waitUntil(
        caches.open(STATIC_CACHE)
            .then((cache) => {
                console.log('[SW] Caching static files...');
                return cache.addAll(STATIC_FILES);
            })
            .then(() => {
                console.log('[SW] Static files cached successfully');
                return self.skipWaiting();
            })
            .catch((error) => {
                console.error('[SW] Error caching static files:', error);
            })
    );
});

// Ativação do Service Worker
self.addEventListener('activate', (event) => {
    console.log('[SW] Activating Service Worker...');
    
    event.waitUntil(
        caches.keys()
            .then((cacheNames) => {
                return Promise.all(
                    cacheNames.map((cacheName) => {
                        if (cacheName !== STATIC_CACHE && cacheName !== DYNAMIC_CACHE) {
                            console.log('[SW] Deleting old cache:', cacheName);
                            return caches.delete(cacheName);
                        }
                    })
                );
            })
            .then(() => {
                console.log('[SW] Service Worker activated successfully');
                return self.clients.claim();
            })
    );
});

// Interceptação de requisições
self.addEventListener('fetch', (event) => {
    const { request } = event;
    const url = new URL(request.url);
    
    // Ignora requisições para APIs externas
    if (url.origin !== self.location.origin) {
        // Para recursos externos (CDNs), usa Network First
        if (url.hostname.includes('cdnjs.cloudflare.com') || 
            url.hostname.includes('fonts.googleapis.com') ||
            url.hostname.includes('fonts.gstatic.com')) {
            event.respondWith(networkFirst(request));
            return;
        }
        // Para outras requisições externas, não faz cache
        return;
    }
    
    // Estratégias de cache baseadas no tipo de recurso
    if (request.destination === 'document') {
        // Para páginas HTML, usa Network First
        event.respondWith(networkFirst(request));
    } else if (request.destination === 'style' || 
               request.destination === 'script' || 
               request.destination === 'image') {
        // Para CSS, JS e imagens, usa Cache First
        event.respondWith(cacheFirst(request));
    } else {
        // Para outros recursos, usa Network First
        event.respondWith(networkFirst(request));
    }
});

// Sincronização em background
self.addEventListener('sync', (event) => {
    console.log('[SW] Background sync triggered:', event.tag);
    
    if (event.tag === 'background-sync') {
        event.waitUntil(doBackgroundSync());
    }
});

// Push notifications
self.addEventListener('push', (event) => {
    console.log('[SW] Push notification received');
    
    const options = {
        body: event.data ? event.data.text() : 'Nova atualização do DMS disponível!',
        icon: '/images/logo.svg',
        badge: '/images/logo.svg',
        vibrate: [100, 50, 100],
        data: {
            dateOfArrival: Date.now(),
            primaryKey: 1
        },
        actions: [
            {
                action: 'explore',
                title: 'Ver Detalhes',
                icon: '/images/icon-explore.png'
            },
            {
                action: 'close',
                title: 'Fechar',
                icon: '/images/icon-close.png'
            }
        ]
    };
    
    event.waitUntil(
        self.registration.showNotification('DMS - Discord Management Suite', options)
    );
});

// Clique em notificação
self.addEventListener('notificationclick', (event) => {
    console.log('[SW] Notification clicked:', event.action);
    
    event.notification.close();
    
    if (event.action === 'explore') {
        event.waitUntil(
            clients.openWindow('/')
        );
    }
});

// Função para sincronização em background
async function doBackgroundSync() {
    try {
        // Aqui você pode implementar sincronização de dados
        // Por exemplo, enviar dados offline salvos
        console.log('[SW] Background sync completed');
    } catch (error) {
        console.error('[SW] Background sync failed:', error);
    }
}

// Função para limpar caches antigos
async function cleanOldCaches() {
    const cacheNames = await caches.keys();
    const currentCaches = [STATIC_CACHE, DYNAMIC_CACHE];
    
    for (const cacheName of cacheNames) {
        if (!currentCaches.includes(cacheName)) {
            await caches.delete(cacheName);
            console.log('[SW] Deleted old cache:', cacheName);
        }
    }
}

// Função para atualizar cache estático
async function updateStaticCache() {
    const cache = await caches.open(STATIC_CACHE);
    
    for (const file of STATIC_FILES) {
        try {
            const response = await fetch(file);
            if (response.ok) {
                await cache.put(file, response);
            }
        } catch (error) {
            console.error('[SW] Error updating cache for:', file, error);
        }
    }
}

// Mensagens do cliente
self.addEventListener('message', (event) => {
    console.log('[SW] Message received:', event.data);
    
    if (event.data && event.data.type === 'SKIP_WAITING') {
        self.skipWaiting();
    }
    
    if (event.data && event.data.type === 'GET_VERSION') {
        event.ports[0].postMessage({ version: CACHE_NAME });
    }
    
    if (event.data && event.data.type === 'CLEAR_CACHE') {
        event.waitUntil(cleanOldCaches());
    }
    
    if (event.data && event.data.type === 'UPDATE_CACHE') {
        event.waitUntil(updateStaticCache());
    }
});

// Log de inicialização
console.log('[SW] DMS Service Worker loaded successfully!');
console.log('[SW] Version:', CACHE_NAME);
console.log('[SW] Static files to cache:', STATIC_FILES.length); 