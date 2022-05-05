import { createWebHistory, createRouter } from "vue-router";

const history = createWebHistory();

const routes = [
  { path: '/', name: 'home', meta: {title: 'B612 | Home', showPort: true}, component: () => import('../views/Home.vue') },
  { path: '/universe', name: 'universe',  meta: {title: 'B612 | Universe', showPort: false}, component: () => import('../views/Universe.vue') },
];

const router = createRouter({ history, routes });

router.beforeEach((to) => {
  document.title = `${to.meta.title}`;
});

export default router;
