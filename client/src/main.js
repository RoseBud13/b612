import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ToastPlugin from './components/toast'

const app = createApp(App)
app
    .use(router)
    .use(store)
    .use(ToastPlugin, {name: '$toast'})
    .mount('#app')
