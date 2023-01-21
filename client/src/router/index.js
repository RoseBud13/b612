import { createWebHistory, createRouter } from 'vue-router'
import { storage } from '../utils/storage'

const history = createWebHistory();

const routes = [
  { path: '/', name: 'home', meta: {title: 'B612 | Home', showPortOnMobile: true}, component: () => import('../views/Home.vue') },
  { path: '/universe', name: 'universe',  meta: {title: 'B612 | Universe', showPortOnMobile: false}, component: () => import('../views/Universe/Universe.vue') },
  { 
    path: '/user/:username', 
    name: 'user',
    meta: {showPortOnMobile: false},
    component: () => import('../views/UserPage.vue') 
  },
];

const router = createRouter({ history, routes });

router.beforeEach((to) => {
  if (to.name == 'user') {
    let userInfo = storage.getAuthUserInfo();
    if (!userInfo.name) {
      return { name: 'home' };
    } else {
      document.title = `B612 | ${userInfo.name}`;
    }
  } else {
    document.title = `${to.meta.title}`;
  }
});

export default router;
