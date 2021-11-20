import { createWebHistory, createRouter } from "vue-router";

const history = createWebHistory();

const routes = [
  { path: '/', meta: {title: 'B612'}, component: () => import('../views/Home.vue') },
];

const router = createRouter({ history, routes });

router.beforeEach((to) => {
  document.title = `${to.meta.title}`;
});

export default router;
